import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
  #(+)degree is left. Opposition to rplidar_A1.png
  #rospy.loginfo("deg : %0.3f" %msg.ranges[0])
    global d
    print("deg 0 : %0.3f" %msg.ranges[0]) #front
    print("deg +78 : %0.3f" %msg.ranges[78])
    print("deg +90 : %0.3f" %msg.ranges[90])# left
    print("deg +137 : %0.3f" %msg.ranges[137])
    print("deg +223(-137) : %0.3f" %msg.ranges[223])
    print("deg +270(-90) : %0.3f" %msg.ranges[270]) # right
    print("deg +282(-78) : %0.3f" %msg.ranges[282])

rospy.init_node('value_test')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
