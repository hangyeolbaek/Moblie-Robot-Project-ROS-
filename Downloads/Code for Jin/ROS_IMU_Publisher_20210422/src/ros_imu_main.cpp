#include <Arduino.h>
#include <stdio.h>
#include <string.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float32.h>

char data_publisher[5];
char data_publisher_msg[10];
/*************************************************************************/
/*                                IMU Main Part                          */
/*************************************************************************/
#include <Wire.h>
#include <Kalman.h> // Source: https://github.com/TKJElectronics/KalmanFilter

#define RESTRICT_PITCH // Comment out to restrict roll to ±90deg instead - please read: http://www.freescale.com/files/sensors/doc/app_note/AN3461.pdf

Kalman kalmanX; // Create the Kalman instances
Kalman kalmanY;

/* IMU Data */
double accX, accY, accZ;
double gyroX, gyroY, gyroZ;
int16_t tempRaw;

double gyroXangle, gyroYangle; // Angle calculate using the gyro only
double compAngleX, compAngleY; // Calculated angle using a complementary filter
double kalAngleX, kalAngleY; // Calculated angle using a Kalman filter

uint32_t timer;
uint8_t i2cData[14]; // Buffer for I2C data
/*------------------ I2C functions ---------------------*/
const uint8_t IMUAddress = 0x68; // AD0 is logic low on the PCB
const uint16_t I2C_TIMEOUT = 1000; // Used to check for errors in I2C communication

uint8_t i2cWrite(uint8_t registerAddress, uint8_t *data, uint8_t length, bool sendStop);
uint8_t i2cWrite(uint8_t registerAddress, uint8_t data, bool sendStop);
uint8_t i2cRead(uint8_t registerAddress, uint8_t *data, uint8_t nbytes);

uint8_t i2cWrite(uint8_t registerAddress, uint8_t data, bool sendStop) {
  return i2cWrite(registerAddress, &data, 1, sendStop); // Returns 0 on success
}

uint8_t i2cWrite(uint8_t registerAddress, uint8_t *data, uint8_t length, bool sendStop) {
  Wire.beginTransmission(IMUAddress);
  Wire.write(registerAddress);
  Wire.write(data, length);
  uint8_t rcode = Wire.endTransmission(sendStop); // Returns 0 on success
  if (rcode) {
    Serial.print(F("i2cWrite failed: "));
    Serial.println(rcode);
  }
  return rcode; // See: http://arduino.cc/en/Reference/WireEndTransmission
}

uint8_t i2cRead(uint8_t registerAddress, uint8_t *data, uint8_t nbytes) {
  uint32_t timeOutTimer;
  Wire.beginTransmission(IMUAddress);
  Wire.write(registerAddress);
  uint8_t rcode = Wire.endTransmission(false); // Don't release the bus
  if (rcode) {
    Serial.print(F("i2cRead failed: "));
    Serial.println(rcode);
    return rcode; // See: http://arduino.cc/en/Reference/WireEndTransmission
  }
  Wire.requestFrom(IMUAddress, nbytes, (uint8_t)true); // Send a repeated start and then release the bus after reading
  for (uint8_t i = 0; i < nbytes; i++) {
    if (Wire.available())
      data[i] = Wire.read();
    else {
      timeOutTimer = micros();
      while (((micros() - timeOutTimer) < I2C_TIMEOUT) && !Wire.available());
      if (Wire.available())
        data[i] = Wire.read();
      else {
        Serial.println(F("i2cRead timeout"));
        return 5; // This error value is not already taken by endTransmission
      }
    }
  }
  return 0; // Success
}
/*------------------end of I2C functions------------------*/
/*************************************************************************/
/*                                IMU PART ENDS                          */
/*************************************************************************/

/*************************************************************************/
/*                                ROS Main Part                          */
/*************************************************************************/
ros::NodeHandle  nh;

/*-----------------------Publisher Part Start--------------------*/
std_msgs::Float32 float32_msg;



ros::Publisher imu_angle("imu_angle", &float32_msg);
ros::Publisher imu_acc("imu_acc", &float32_msg);
ros::Publisher imu_gyro("imu_gyro", &float32_msg);
/*-----------------------Publisher Part Ends---------------------*/

/*-----------------------Subscriber Part Start--------------------*/
#ifndef LED_BUILTIN
#define LED_BUILTIN 13
#endif

#define M_LEFT_PWM 6
#define M_LEFT_FR 7
#define M_RIGHT_PWM 5
#define M_RIGHT_FR 4

void turnWheel( const std_msgs::Float32 &wheel_power,
                unsigned int pwm_pin,
                unsigned int fr_pin ) {
    float factor = max(min(wheel_power.data, 1.0f), -1.0f);
    if( factor >= 0 ) {
        digitalWrite(fr_pin, LOW);
        analogWrite(pwm_pin, (unsigned int)(255 * factor));
    } else {
        digitalWrite(fr_pin, HIGH);
        analogWrite(pwm_pin, (unsigned int)(255 * abs(factor)));
    }
}
void rightWheelCb( const std_msgs::Float32 &wheel_power ) {
    //nh.loginfo("Wheel Power - Right");
    //char result[8];
    //dtostrf(wheel_power.data, 6, 2, result);
    //nh.loginfo(result);
    turnWheel( wheel_power, M_RIGHT_PWM, M_RIGHT_FR );
}
void leftWheelCb( const std_msgs::Float32 &wheel_power ) {
    //nh.loginfo("Wheel Power - Left");
    turnWheel( wheel_power, M_LEFT_PWM, M_LEFT_FR );
}

ros::Subscriber<std_msgs::Float32> sub_right("wheel_power_right", &rightWheelCb );
//ros::Subscriber<std_msgs::Float32> sub_left("sma_2_power",
//                                           &leftWheelCb );

ros::Subscriber<std_msgs::Float32> sub_left("wheel_power_left", &leftWheelCb );
/*-----------------------Subscriber Part Ends----------------------*/

void setup()
{
  /*************************************************************************/
  /*                         IMU Main Part Setup                           */
  /*************************************************************************/
  Wire.begin();
  #if ARDUINO >= 157
  Wire.setClock(400000UL); // Set I2C frequency to 400kHz
  #else
  TWBR = ((F_CPU / 400000UL) - 16) / 2; // Set I2C frequency to 400kHz
  #endif

  i2cData[0] = 7; // Set the sample rate to 1000Hz - 8kHz/(7+1) = 1000Hz
  i2cData[1] = 0x00; // Disable FSYNC and set 260 Hz Acc filtering, 256 Hz Gyro filtering, 8 KHz sampling
  i2cData[2] = 0x00; // Set Gyro Full Scale Range to ±250deg/s
  i2cData[3] = 0x00; // Set Accelerometer Full Scale Range to ±2g
  while (i2cWrite(0x19, i2cData, 4, false)); // Write to all four registers at once
  while (i2cWrite(0x6B, 0x01, true)); // PLL with X axis gyroscope reference and disable sleep mode

  while (i2cRead(0x75, i2cData, 1));
  if (i2cData[0] != 0x68) { // Read "WHO_AM_I" register
    Serial.print(F("Error reading sensor"));
    while (1);
  }

  delay(100); // Wait for sensor to stabilize

  /* Set kalman and gyro starting angle */
  while (i2cRead(0x3B, i2cData, 6));
  accX = (int16_t)((i2cData[0] << 8) | i2cData[1]);
  accY = (int16_t)((i2cData[2] << 8) | i2cData[3]);
  accZ = (int16_t)((i2cData[4] << 8) | i2cData[5]);

  // Source: http://www.freescale.com/files/sensors/doc/app_note/AN3461.pdf eq. 25 and eq. 26
  // atan2 outputs the value of -π to π (radians) - see http://en.wikipedia.org/wiki/Atan2
  // It is then converted from radians to degrees
  #ifdef RESTRICT_PITCH // Eq. 25 and 26
  double roll  = atan2(accY, accZ) * RAD_TO_DEG;
  double pitch = atan(-accX / sqrt(accY * accY + accZ * accZ)) * RAD_TO_DEG;
  #else // Eq. 28 and 29
  double roll  = atan(accY / sqrt(accX * accX + accZ * accZ)) * RAD_TO_DEG;
  double pitch = atan2(-accX, accZ) * RAD_TO_DEG;
  #endif

  kalmanX.setAngle(roll); // Set starting angle
  kalmanY.setAngle(pitch);
  gyroXangle = roll;
  gyroYangle = pitch;
  compAngleX = roll;
  compAngleY = pitch;

  timer = micros();
  /*************************************************************************/
  /*                          IMU Setup Part Ends                          */
  /*************************************************************************/

  /*************************************************************************/
  /*                         Motor Main Part Setup                         */
  /*************************************************************************/
  // initialize LED digital pin as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, HIGH);

  pinMode(M_LEFT_PWM, OUTPUT);
  pinMode(M_LEFT_FR, OUTPUT);
  pinMode(M_RIGHT_PWM, OUTPUT);
  pinMode(M_RIGHT_FR, OUTPUT);

  // Init motors to stop
  digitalWrite(M_LEFT_FR, LOW);
  digitalWrite(M_RIGHT_FR, LOW);
  analogWrite(M_LEFT_PWM, 0);
  analogWrite(M_RIGHT_PWM, 0);

  /*************************************************************************/
  /*                              ROS Main Setup                           */
  /*************************************************************************/
  nh.initNode();

  /*-------------Publisher Part Start--------------*/
  nh.advertise(imu_angle);
  nh.advertise(imu_acc);
  nh.advertise(imu_gyro);
  /*-------------Publisher Part Ends---------------*/

  /*-------------Subscriber Part Start--------------*/
  nh.subscribe(sub_right);
  nh.subscribe(sub_left);
  /*-------------Subscriber Part Ends---------------*/
}



void loop()
{
  /*************************************************************************/
  /*                             IMU Loop Part                             */
  /*************************************************************************/
  while (i2cRead(0x3B, i2cData, 14));
  accX = (int16_t)((i2cData[0] << 8) | i2cData[1]);
  accY = (int16_t)((i2cData[2] << 8) | i2cData[3]);
  accZ = (int16_t)((i2cData[4] << 8) | i2cData[5]);
  tempRaw = (int16_t)((i2cData[6] << 8) | i2cData[7]);
  gyroX = (int16_t)((i2cData[8] << 8) | i2cData[9]);
  gyroY = (int16_t)((i2cData[10] << 8) | i2cData[11]);
  gyroZ = (int16_t)((i2cData[12] << 8) | i2cData[13]);;

  double dt = (double)(micros() - timer) / 1000000; // Calculate delta time
  timer = micros();

  // Source: http://www.freescale.com/files/sensors/doc/app_note/AN3461.pdf eq. 25 and eq. 26
  // atan2 outputs the value of -π to π (radians) - see http://en.wikipedia.org/wiki/Atan2
  // It is then converted from radians to degrees
#ifdef RESTRICT_PITCH // Eq. 25 and 26
  double roll  = atan2(accY, accZ) * RAD_TO_DEG;
  double pitch = atan(-accX / sqrt(accY * accY + accZ * accZ)) * RAD_TO_DEG;
#else // Eq. 28 and 29
  double roll  = atan(accY / sqrt(accX * accX + accZ * accZ)) * RAD_TO_DEG;
  double pitch = atan2(-accX, accZ) * RAD_TO_DEG;
#endif

  double gyroXrate = gyroX / 131.0; // Convert to deg/s
  double gyroYrate = gyroY / 131.0; // Convert to deg/s

#ifdef RESTRICT_PITCH
  // This fixes the transition problem when the accelerometer angle jumps between -180 and 180 degrees
  if ((roll < -90 && kalAngleX > 90) || (roll > 90 && kalAngleX < -90)) {
    kalmanX.setAngle(roll);
    compAngleX = roll;
    kalAngleX = roll;
    gyroXangle = roll;
  } else // the most important line here 90 is the reference to convert it into vertical
    kalAngleX = 90-kalmanX.getAngle(roll, gyroXrate, dt); // Calculate the angle using a Kalman filter

  if (abs(kalAngleX) > 90)
    gyroYrate = -gyroYrate; // Invert rate, so it fits the restriced accelerometer reading
  kalAngleY = kalmanY.getAngle(pitch, gyroYrate, dt);
#else
  // This fixes the transition problem when the accelerometer angle jumps between -180 and 180 degrees
  if ((pitch < -90 && kalAngleY > 90) || (pitch > 90 && kalAngleY < -90)) {
    kalmanY.setAngle(pitch);
    compAngleY = pitch;
    kalAngleY = pitch;
    gyroYangle = pitch;
  } else
    kalAngleY = kalmanY.getAngle(pitch, gyroYrate, dt); // Calculate the angle using a Kalman filter

  if (abs(kalAngleY) > 90)
    gyroXrate = -gyroXrate; // Invert rate, so it fits the restriced accelerometer reading
  kalAngleX = kalmanX.getAngle(roll, gyroXrate, dt); // Calculate the angle using a Kalman filter
#endif

  gyroXangle += gyroXrate * dt; // Calculate gyro angle without any filter
  gyroYangle += gyroYrate * dt;
  //gyroXangle += kalmanX.getRate() * dt; // Calculate gyro angle using the unbiased rate
  //gyroYangle += kalmanY.getRate() * dt;

  compAngleX = 0.93 * (compAngleX + gyroXrate * dt) + 0.07 * roll; // Calculate the angle using a Complimentary filter
  compAngleY = 0.93 * (compAngleY + gyroYrate * dt) + 0.07 * pitch;

  // Reset the gyro angle when it has drifted too much
  if (gyroXangle < -180 || gyroXangle > 180)
    gyroXangle = kalAngleX;
  if (gyroYangle < -180 || gyroYangle > 180)
    gyroYangle = kalAngleY;

  /* Print Data */
#if 0 // Set to 1 to activate
  Serial.print(accX); Serial.print("\t");
  Serial.print(accY); Serial.print("\t");
  Serial.print(accZ); Serial.print("\t");

  Serial.print(gyroX); Serial.print("\t");
  Serial.print(gyroY); Serial.print("\t");
  Serial.print(gyroZ); Serial.print("\t");

  Serial.print("\t");
#endif
  //unsigned long short_time=millis();
  //Serial.print(roll); Serial.print("\t");
 // Serial.print(gyroXangle); Serial.print("\t");
 // Serial.print(compAngleX); Serial.print("\t");
 /*----------------This part is for serial----------------*/
 /*
 Serial.print("     roll Angle : ");
 Serial.print(kalAngleX-90);
 Serial.print("     acc : ");
 Serial.print(accX/9.8);
 Serial.print("     gyro : ");
 Serial.print(gyroX/9.8);
 Serial.print("     millis() : ");
 Serial.print(dt);
 //Serial.print("     spped :      ");
 //Serial.print(gyroX);
 Serial.print("\t");

  Serial.print("\t");
  */
 // Serial.print(pitch); Serial.print("\t");
 // Serial.print(gyroYangle); Serial.print("\t");
 // Serial.print(compAngleY); Serial.print("\t");
  //Serial.print(kalAngleY); Serial.print("\t");

#if 0 // Set to 1 to print the temperature
  Serial.print("\t");

  double temperature = (double)tempRaw / 340.0 + 36.53;
  Serial.print(temperature); Serial.print("\t");
#endif

  //Serial.print("\r\n");
  //delay(2);

  /*************************************************************************/
  /*                             IMU Loop Part Ends                            */
  /*************************************************************************/

  /*-------------Publisher Part Start--------------*/
  {
    //float32_msg.data = kalAngleX-90; // angle
    float32_msg.data = kalAngleX; // angle
    imu_angle.publish( &float32_msg );
    nh.loginfo("Published angle x messages");
  }
  /*-------------Publisher Part Start--------------*/
  {
    //float32_msg.data = gyroX/9.8; // gyro
    float32_msg.data = gyroX/9.8; // gyro
    imu_gyro.publish( &float32_msg );
      //strcat(data_publisher_msg,sprintf(data_publisher, "%g", gyroX/9.8));
    nh.loginfo("Published gyro messages");
  }

  {
    //float32_msg.data = accX/9.8; // acc
    float32_msg.data = accX/9.8; // acc
    imu_acc.publish( &float32_msg );
    nh.loginfo("Published acc messages");
  }

  /*-------------Publisher Part Ends---------------*/


  //nh.loginfo( "Published a lot of messages" );

  nh.spinOnce();
  delay(200);
}
