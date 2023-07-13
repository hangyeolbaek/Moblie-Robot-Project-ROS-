#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32
from simple_pid import PID

pid = PID(1, 0.1, 0.05, setpoint=20)
pid.sample_time = 0.01  # Update every 0.01 seconds
pid.output_limits = (0, 1)    # Output value will be between 0 and 1

class Foo(object):
    def __init__(self):
        self.value = 0
        self.data= 0
        self.imu_angle = 0
        self.imu_gyro = 0
        self.imu_acc = 0

        rospy.init_node('listener', anonymous=True)
        rospy.loginfo('Waiting for imu topic %s to be published...', 'imu_angle')
        rospy.loginfo('%s topic is now available!', 'imu_angle')

        self.pwm_pub_left  = rospy.Publisher('wheel_power_left',  Float32, queue_size=10)
        self.pwm_pub_right = rospy.Publisher('wheel_power_right', Float32, queue_size=10)

        rospy.Subscriber("imu_angle", Float32, self.imu_angle_fun)
        rospy.Subscriber("imu_gyro", Float32, self.imu_gyro_fun)
        rospy.Subscriber("imu_acc", Float32, self.imu_acc_fun)
        
        #self.pwm_pub_left.publish(0.5)
        #self.pwm_pub_right.publish(0.5)
        #rospy.spin()
        
        r = rospy.Rate(10)
        while not rospy.is_shutdown():
            control = pid(self.imu_angle)
            rospy.loginfo("control input is %s ",control)
            self.pwm_pub_right.publish(control)
            #self.pwm_pub_left.publish(0.0)
            #self.pwm_pub_right.publish(0.0)
            #rospy.loginfo(rospy.get_caller_id() + "I heard %s %s %s", self.imu_angle, self.imu_gyro, self.imu_acc )
            rospy.loginfo(rospy.get_caller_id() + "I heard %s %s %s", self.imu_angle, self.imu_gyro, self.imu_acc )
            r.sleep()

    def imu_angle_fun(self, data):
        #rospy.loginfo(rospy.get_caller_id() + "I heard imu angle %s", data.data)
        self.imu_angle = data.data

    def imu_gyro_fun(self, data):
        #rospy.loginfo(rospy.get_caller_id() + "I heard imu gyro %s", data.data)
        self.imu_gyro = data.data

    def imu_acc_fun(self, data):
        #rospy.loginfo(rospy.get_caller_id() + "I heard imu acc %s", data.data)
        self.imu_acc = data.data
   
    
if __name__ == '__main__':
    try:    
        foo = Foo()
    except rospy.ROSInterruptException:  
        pass