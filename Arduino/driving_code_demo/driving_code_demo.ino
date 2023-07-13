#include <ros.h>
#include <std_msgs/String.h> //ros topic message type

ros::NodeHandle  nh;

std_msgs::String str_msg;

int Dir1Pin_A = 24;  
int Dir2Pin_A = 22;  
int speedPin_A = 3;
//front_left 

int Dir1Pin_B = 28;
int Dir2Pin_B = 26;
int speedPin_B = 2;
//front_right

int Dir1Pin_C = 32;
int Dir2Pin_C = 30;
int speedPin_C = 5;
//rear_left

int Dir1Pin_D = 36;
int Dir2Pin_D = 34;
int speedPin_D = 4;
//rear_right

int Dir1Pin_E = 40;
int Dir2Pin_E = 38;
int speedPin_E = 6;

String receive_value;

void front();
void front_slow();
void back();
void back_slow();
void left();
void left_slow();
void right();
void right_slow();
void motor_stop();
void riftup();
void riftdown();
void turn_around();
void turn_left();
void turn_right();
void left_real_slow();
void right_real_slow();

void driving(const std_msgs::String& str_msg);

ros::Subscriber<std_msgs::String> sub("driving", &driving);

void setup() {
  // put your setup code here, to run once:
  pinMode(Dir1Pin_A, OUTPUT);
  pinMode(Dir2Pin_A, OUTPUT);
  pinMode(speedPin_A, OUTPUT);

  pinMode(Dir1Pin_B, OUTPUT);
  pinMode(Dir2Pin_B, OUTPUT);
  pinMode(speedPin_B, OUTPUT);

  pinMode(Dir1Pin_C, OUTPUT);
  pinMode(Dir2Pin_C, OUTPUT);
  pinMode(speedPin_C, OUTPUT);

  pinMode(Dir1Pin_D, OUTPUT);
  pinMode(Dir2Pin_D, OUTPUT);
  pinMode(speedPin_D, OUTPUT);

  pinMode(Dir1Pin_E, OUTPUT);
  pinMode(Dir2Pin_E, OUTPUT);
  pinMode(speedPin_E, OUTPUT);

  nh.initNode();
  nh.subscribe(sub);
}

void driving(const std_msgs::String& str_msg)
{
  receive_value = str_msg.data;
  if ((receive_value)=="front")
    front();
  else if ((receive_value)=="front_slow")
    front_slow();
  else if ((receive_value)=="right")
    right();
  else if ((receive_value)=="right_slow")
    right_slow();
  else if ((receive_value)=="right_real_slow")
    right_real_slow();
  else if ((receive_value)=="left")
    left();
  else if ((receive_value)=="left_slow")
    left_slow();
  else if ((receive_value)=="left_real_slow")
    left_real_slow();
  else if ((receive_value)=="back")
    back();
  else if ((receive_value)=="back_slow")
    back_slow();
  else if ((receive_value)=="riftup")
    riftup();
  else if ((receive_value)=="riftdown")
    riftdown();
  else if ((receive_value)=="error")
    motor_stop();
  else if ((receive_value)=="motor_stop")
    motor_stop();
  else if ((receive_value)=="turn_around")
    turn_around();
  else if ((receive_value)=="turn_left")
    turn_left();
  else if ((receive_value)=="turn_right")
    turn_right();
  else
    motor_stop();
    
  //motor_stop();
}

void front()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 255);

  digitalWrite(Dir1Pin_B, LOW);
  digitalWrite(Dir2Pin_B, HIGH);
  analogWrite(speedPin_B, 255);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 255);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 255);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  
}

void front_slow()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 100);

  digitalWrite(Dir1Pin_B, LOW);
  digitalWrite(Dir2Pin_B, HIGH);
  analogWrite(speedPin_B, 120);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 100);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 120);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  
}

void back()
{
  digitalWrite(Dir1Pin_A, LOW);
  digitalWrite(Dir2Pin_A, HIGH);
  analogWrite(speedPin_A, 255);

  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 255);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 255);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 255);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
}

void back_slow()
{
  digitalWrite(Dir1Pin_A, LOW);
  digitalWrite(Dir2Pin_A, HIGH);
  analogWrite(speedPin_A, 100);

  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 120);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 100);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 120);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
}

void left()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 255);

  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 255);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 255);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 255);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
}

void left_real_slow()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
//  analogWrite(speedPin_A, 170);
  analogWrite(speedPin_A, 120);

  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
//  analogWrite(speedPin_B, 140);
  analogWrite(speedPin_B, 70);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
//  analogWrite(speedPin_C, 140);
  analogWrite(speedPin_C, 70);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
//  analogWrite(speedPin_D, 170);
  analogWrite(speedPin_D, 120);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
}

void left_slow()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 150);

  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 150);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 150);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 150);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  
}

void right()
{
  digitalWrite(Dir1Pin_A, LOW);
  digitalWrite(Dir2Pin_A, HIGH);
  analogWrite(speedPin_A, 255);

  digitalWrite(Dir1Pin_B, LOW);
  digitalWrite(Dir2Pin_B, HIGH);
  analogWrite(speedPin_B, 255);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 255);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 255);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  
}

void right_real_slow()
{
  digitalWrite(Dir1Pin_A, LOW);
  digitalWrite(Dir2Pin_A, HIGH);
  analogWrite(speedPin_A, 70);

  digitalWrite(Dir1Pin_B, LOW);
  digitalWrite(Dir2Pin_B, HIGH);
  analogWrite(speedPin_B, 120);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 120);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 70);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0); 
}

void right_slow()
{
  digitalWrite(Dir1Pin_A, LOW);
  digitalWrite(Dir2Pin_A, HIGH);
  analogWrite(speedPin_A, 145);

  digitalWrite(Dir1Pin_B, LOW);
  digitalWrite(Dir2Pin_B, HIGH);
  analogWrite(speedPin_B, 160);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 160);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 140);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0); 
}

void riftup()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 0);

  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 0);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 0);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 0);

  digitalWrite(Dir1Pin_E, HIGH);
  digitalWrite(Dir2Pin_E, LOW);
  analogWrite(speedPin_E, 255);
  //delay(10000);
}

void riftdown()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 0);
  
  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 0);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 0);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 0);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 255);
  //delay(10000);
}

void motor_stop()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 0);
  
  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 0);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 0);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 0);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  //delay(255);
}

void turn_around()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 255);
  
  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 255);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 255);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 255);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  //delay(0);//turn_around_right
}

void turn_left()
{
  digitalWrite(Dir1Pin_A, LOW);
  digitalWrite(Dir2Pin_A, HIGH);
  analogWrite(speedPin_A, 50);
  
  digitalWrite(Dir1Pin_B, LOW);
  digitalWrite(Dir2Pin_B, HIGH);
  analogWrite(speedPin_B, 70);

  digitalWrite(Dir1Pin_C, LOW);
  digitalWrite(Dir2Pin_C, HIGH);
  analogWrite(speedPin_C, 50);

  digitalWrite(Dir1Pin_D, LOW);
  digitalWrite(Dir2Pin_D, HIGH);
  analogWrite(speedPin_D, 70);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  //delay();//turn_left
}

void turn_right()
{
  digitalWrite(Dir1Pin_A, HIGH);
  digitalWrite(Dir2Pin_A, LOW);
  analogWrite(speedPin_A, 50);
  
  digitalWrite(Dir1Pin_B, HIGH);
  digitalWrite(Dir2Pin_B, LOW);
  analogWrite(speedPin_B, 70);

  digitalWrite(Dir1Pin_C, HIGH);
  digitalWrite(Dir2Pin_C, LOW);
  analogWrite(speedPin_C, 50);

  digitalWrite(Dir1Pin_D, HIGH);
  digitalWrite(Dir2Pin_D, LOW);
  analogWrite(speedPin_D, 70);

  digitalWrite(Dir1Pin_E, LOW);
  digitalWrite(Dir2Pin_E, HIGH);
  analogWrite(speedPin_E, 0);
  //delay();//turn_left
}

void loop() {
  // put your main code here, to run repeatedly:
/*
digitalWrite(Dir1Pin_A, HIGH);
digitalWrite(Dir2Pin_A, LOW);
analogWrite(speedPin_A, 255);//front HIGH LOW


digitalWrite(Dir1Pin_B, HIGH);
digitalWrite(Dir2Pin_B, LOW);
analogWrite(speedPin_B, 75);//back HIGH LOW


digitalWrite(Dir1Pin_C, HIGH);
digitalWrite(Dir2Pin_C, LOW);
analogWrite(speedPin_C, 75);//front HIGH LOW


digitalWrite(Dir1Pin_D, HIGH);
digitalWrite(Dir2Pin_D, LOW);
analogWrite(speedPin_D, 75);//back HIGH LOW
delay(750);
*/

  nh.spinOnce();
  //delay(100);
}
