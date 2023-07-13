import rospy
from sensor_msgs.msg import LaserScan

global deg0, deg78, deg90, deg137, deg223, deg270, deg282

def callback(msg):
  #(+)degree is left. Opposition to rplidar_A1.png
  #rospy.loginfo("deg : %0.3f" %msg.ranges[0])
    deg0=("%0.3f" %msg.ranges[0]) #front
    deg78=("%0.3f" %msg.ranges[78])
    deg90=("%0.3f" %msg.ranges[90])# left
    deg137=("%0.3f" %msg.ranges[137])
    deg223=("%0.3f" %msg.ranges[223])
    deg270=("%0.3f" %msg.ranges[270]) # right
    deg282=("%0.3f" %msg.ranges[282])

    #if (((deg0 >= 0.15) and (deg0 <= 8.00)) and ((deg78 >= 0.24) and (deg78 <= 8.00)) and ((deg90 >= 0.24) and (deg90 <= 8.00)) and ((deg137 >= 0.40) and (deg137 <= 8.00)) and ((deg223 >= 0.40) and (deg223 <= 8.00)) and ((deg270 >= 0.24) and (deg270 <= 8.00)) and ((deg282 >= 0.24) and (deg282 <= 8.00))):

    print(deg0)
    print(deg78)
    print(deg90)
    print(deg137)
    print(deg223)
    print(deg270)
    print(deg282)

    if (((msg.ranges[0] >= 0.15) and (msg.ranges[0] <= 8.00)) and ((msg.ranges[78] >= 0.24) and (msg.ranges[78] <= 8.00)) and ((msg.ranges[90] >= 0.24) and (msg.ranges[90] <= 8.00)) and ((msg.ranges[137] >= 0.40) and (msg.ranges[137] <= 8.00)) and ((msg.ranges[223] >= 0.40) and (msg.ranges[223] <= 8.00)) and ((msg.ranges[270] >= 0.24) and (msg.ranges[270] <= 8.00)) and ((msg.ranges[282] >= 0.24) and (msg.ranges[282] <= 8.00))):
        print("value = 1")
    else:
        print("value = 0")


rospy.init_node('pub_value')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
