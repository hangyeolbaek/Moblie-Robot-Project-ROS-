#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from sensor_msgs.msg import LaserScan

def callback(msg):
  #(+)degree is left. Opposition to rplidar_A1.png
  #rospy.loginfo("deg : %0.3f" %msg.ranges[0])
    global deg0, deg40, deg45, deg78, deg90, deg137, deg223, deg270, deg282, deg315, deg320, send_value

    if msg.ranges[0] <= 8.000:
        deg0=msg.ranges[0]
        #print("^_________________________________^")
    elif msg.ranges[0] >= 8.000 and msg.ranges[1] <= 8.000:
        deg0=msg.ranges[1]
        #print("^_________________________________^")
    elif msg.ranges[0] >= 8.000 and msg.ranges[1] >= 8.000 and msg.ranges[359] <= 8.000:
        deg0=msg.ranges[359]
        #print("^_________________________________^")
    else:
        print("deg 0 lost")

    if msg.ranges[40] <= 8.000:
        deg40=msg.ranges[40]
        #print("^_________________________________^")
    elif msg.ranges[40] >= 8.000 and msg.ranges[39] <= 8.000:
        deg40=msg.ranges[39]
        #print("^_________________________________^")
    elif msg.ranges[40] >= 8.000 and msg.ranges[39] >= 8.000 and msg.ranges[41] <= 8.000:
        deg40=msg.ranges[41]
        #print("^_________________________________^")
    else:
        print("deg 40 lost")

    if msg.ranges[45] <= 8.000:
        deg45=msg.ranges[45]
        #print("^_________________________________^")
    elif msg.ranges[45] >= 8.000 and msg.ranges[46] <= 8.000:
        deg45=msg.ranges[46]
        #print("^_________________________________^")
    elif msg.ranges[45] >= 8.000 and msg.ranges[46] >= 8.000 and msg.ranges[44] <= 8.000:
        deg45=msg.ranges[44]
        #print("^_________________________________^")
    else:
        print("deg 45 lost")

    if msg.ranges[78] <= 8.000:
        deg78=msg.ranges[78]
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] <= 8.000:
        deg78=msg.ranges[77]
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] >= 8.000 and msg.ranges[79] <= 8.000:
        deg78=msg.ranges[79]
        #print("^_________________________________^")
    else:
        print("deg 78 lost")

    if msg.ranges[90] <= 8.000:
        deg90=msg.ranges[90]
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] <= 8.000:
        deg90=msg.ranges[89]
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] >= 8.000 and msg.ranges[91] <= 8.000:
        deg90=msg.ranges[91]
        #print("^_________________________________^")
    else:
        print("deg 90 lost")

    if msg.ranges[137] <= 8.000:
        deg137=msg.ranges[137]
        #print("^_________________________________^")
    elif msg.ranges[137] >= 8.000 and msg.ranges[136] <= 8.000:
        deg137=msg.ranges[136]
        #print("^_________________________________^")
    elif msg.ranges[137] >= 8.000 and msg.ranges[136] >= 8.000 and msg.ranges[138] <= 8.000:
        deg137=msg.ranges[138]
        #print("^_________________________________^")
    else:
        print("deg 137 lost")

    if msg.ranges[223] <= 8.000:
        deg223=msg.ranges[223]
        #print("^_________________________________^")
    elif msg.ranges[223] >= 8.000 and msg.ranges[224] <= 8.000:
        deg223=msg.ranges[224]
        #print("^_________________________________^")
    elif msg.ranges[223] >= 8.000 and msg.ranges[224] >= 8.000 and msg.ranges[222] <= 8.000:
        deg223=msg.ranges[222]
        #print("^_________________________________^")
    else:
        print("deg 223 lost")

    if msg.ranges[270] <= 8.000:
        deg270=msg.ranges[270]
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] <= 8.000:
        deg270=msg.ranges[271]
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] >= 8.000 and msg.ranges[269] <= 8.000:
        deg270=msg.ranges[269]
        #print("^_________________________________^")
    else:
        print("deg 270 lost")

    if msg.ranges[282] <= 8.000:
        deg282=msg.ranges[282]
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] <= 8.000:
        deg282=msg.ranges[283]
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] >= 8.000 and msg.ranges[281] <= 8.000:
        deg282=msg.ranges[281]
        #print("^_________________________________^")
    else:
        print("deg 282 lost")
        #print("^_________________________________^")

    if msg.ranges[315] <= 8.000:
        deg315=msg.ranges[315]
        #print("^_________________________________^")
    elif msg.ranges[315] >= 8.000 and msg.ranges[316] <= 8.000:
        deg315=msg.ranges[316]
        #print("^_________________________________^")
    elif msg.ranges[315] >= 8.000 and msg.ranges[316] >= 8.000 and msg.ranges[314] <= 8.000:
        deg315=msg.ranges[314]
        #print("^_________________________________^")
    else:
        print("deg 315 lost")
        #print("^_________________________________^")

    if msg.ranges[320] <= 8.000:
        deg320=msg.ranges[320]
        print("^_________________________________^")
    elif msg.ranges[320] >= 8.000 and msg.ranges[321] <= 8.000:
        deg320=msg.ranges[321]
        print("^_________________________________^")
    elif msg.ranges[320] >= 8.000 and msg.ranges[321] >= 8.000 and msg.ranges[319] <= 8.000:
        deg320=msg.ranges[319]
        print("^_________________________________^")
    else:
        print("deg 320 lost")
        print("^_________________________________^")

    if (deg0 > 0.350):
        send_value = "left"

def send_topic():
    global send_value
    rospy.init_node('pub_value', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    #rospy.Subscriber('package', String, operating)
    pub = rospy.Publisher('driving', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(send_value)
        rate.sleep()

if __name__ == '__main__':
    deg0=0
    deg40=0
    deg45=0
    deg78=0
    deg90=0
    deg137=0
    deg223=0
    deg270=0
    deg282=0
    deg315=0
    deg320=0
    send_value = "initial value"
    try:
        send_topic()
    except rospy.ROSInterruptException:
        pass
