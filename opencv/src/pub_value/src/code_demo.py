#code modified and variation save


#4Mx4M space
    if (((deg0 >= 0.150) and (deg0 <= 8.000)) and ((deg90 >= 0.240) and (deg90 <= 8.000)) and ((deg270 >= 0.240) and (deg270 <= 8.000))):
        if (deg0 <= 0.250):
            if ((deg90+deg270)>=2.500):
                if (deg90 <= 0.350) and (deg270 >= 0.350) and (deg90 < deg270):
                    send_value = "right"
                elif (deg45 <= 0.350) and (deg78 <= 1.200) and (deg90 >= 0.350) and (deg270 >= 0.350) and (deg282 <= 1.200) and (deg315 <= 0.350):
                    send_value = "turn_around"
            elif ((deg90+deg270)<=2.500):
                if ()
                elif (deg90 <= 0.350) and (deg270 <= 0.350):
                    send_value = "back"
                elif (deg


        elif (deg0 <= 0.250) and (deg90 <= 0.350) and (deg270 >= 0.350):
            send_value = "right"
        elif (deg0 <= 0.250) and (deg90 >= 0.350) and (deg270 >= 0.350) and (deg90 < deg270):
            send_value = "right"
        elif (deg0 <= 0.250) and (deg90 >= 0.350) and (deg270 <= 0.350):
            send_value = "left"
        elif (deg0 <= 0.250) and (deg90 >= 0.350) and (deg270 >= 0.350) and (deg90 > deg270):
            send_value = "left"

---------------------------------------------------------------------------------------------

#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from std_msgs.msg import UInt16
from sensor_msgs.msg import LaserScan

deg0=0
deg45=0
deg78=0
deg90=0
deg137=0
deg223=0
deg270=0
deg282=0
deg315=0
send_value = "initial value"

#rospy.init_node('pub_value', anonymous=True)
#sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('driving', String, queue_size=10)

def callback(msg):
  #(+)degree is left. Opposition to rplidar_A1.png
  #rospy.loginfo("deg : %0.3f" %msg.ranges[0])
    global deg0, deg45, deg78, deg90, deg137, deg223, deg270, deg282, deg315, send_value

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

    if msg.ranges[45] <= 8.000:
        deg45=("%0.3f" %msg.ranges[45])
        #print("^_________________________________^")
    elif msg.ranges[45] >= 8.000 and msg.ranges[46] <= 8.000:
        deg45=("%0.3f" %msg.ranges[46])
        #print("^_________________________________^")
    elif msg.ranges[45] >= 8.000 and msg.ranges[46] >= 8.000 and msg.ranges[44] <= 8.000:
        deg45=("%0.3f" %msg.ranges[44])
        #print("^_________________________________^")
    else:
        print("deg 45 lost")

    if msg.ranges[78] <= 8.000:
        deg78=("%0.3f" %msg.ranges[78])
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] <= 8.000:
        deg78=("%0.3f" %msg.ranges[77])
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] >= 8.000 and msg.ranges[79] <= 8.000:
        deg78=("%0.3f" %msg.ranges[79])
        #print("^_________________________________^")
    else:
        print("deg 78 lost")

    if msg.ranges[90] <= 8.000:
        deg90=("%0.3f" %msg.ranges[90])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] <= 8.000:
        deg90=("%0.3f" %msg.ranges[89])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] >= 8.000 and msg.ranges[91] <= 8.000:
        deg90=("%0.3f" %msg.ranges[91])
        #print("^_________________________________^")
    else:
        print("deg 90 lost")

    if msg.ranges[137] <= 8.000:
        deg137=("%0.3f" %msg.ranges[137])
        #print("^_________________________________^")
    elif msg.ranges[137] >= 8.000 and msg.ranges[136] <= 8.000:
        deg137=("%0.3f" %msg.ranges[136])
        #print("^_________________________________^")
    elif msg.ranges[137] >= 8.000 and msg.ranges[136] >= 8.000 and msg.ranges[138] <= 8.000:
        deg137=("%0.3f" %msg.ranges[138])
        #print("^_________________________________^")
    else:
        print("deg 137 lost")

    if msg.ranges[223] <= 8.000:
        deg223=("%0.3f" %msg.ranges[223])
        #print("^_________________________________^")
    elif msg.ranges[223] >= 8.000 and msg.ranges[224] <= 8.000:
        deg223=("%0.3f" %msg.ranges[224])
        #print("^_________________________________^")
    elif msg.ranges[223] >= 8.000 and msg.ranges[224] >= 8.000 and msg.ranges[222] <= 8.000:
        deg223=("%0.3f" %msg.ranges[222])
        #print("^_________________________________^")
    else:
        print("deg 223 lost")

    if msg.ranges[270] <= 8.000:
        deg270=("%0.3f" %msg.ranges[270])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] <= 8.000:
        deg270=("%0.3f" %msg.ranges[271])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] >= 8.000 and msg.ranges[269] <= 8.000:
        deg270=("%0.3f" %msg.ranges[269])
        #print("^_________________________________^")
    else:
        print("deg 270 lost")

    if msg.ranges[282] <= 8.000:
        deg282=("%0.3f" %msg.ranges[282])
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] <= 8.000:
        deg282=("%0.3f" %msg.ranges[283])
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] >= 8.000 and msg.ranges[281] <= 8.000:
        deg282=("%0.3f" %msg.ranges[281])
        #print("^_________________________________^")
    else:
        print("deg 282 lost")
        #print("^_________________________________^")

    if msg.ranges[315] <= 8.000:
        deg315=("%0.3f" %msg.ranges[315])
        #print("^_________________________________^")
    elif msg.ranges[315] >= 8.000 and msg.ranges[316] <= 8.000:
        deg315=("%0.3f" %msg.ranges[316])
        #print("^_________________________________^")
    elif msg.ranges[315] >= 8.000 and msg.ranges[316] >= 8.000 and msg.ranges[314] <= 8.000:
        deg315=("%0.3f" %msg.ranges[314])
        #print("^_________________________________^")
    else:
        print("deg 315 lost")
        #print("^_________________________________^")


    #if (((deg0 >= 0.150) and (deg0 <= 8.000)) and ((deg90 >= 0.240) and (deg90 <= 8.000)) and ((deg270 >= 0.240) and (deg270 <= 8.000))):
    #    if (deg0 <= 0.200) and (deg90 <= 0.350) and (deg270 <= 0.350):
    #        send_value = "error" # or back
    #    elif (def0 <= 0.250) and (deg90 <= 0.350) and (deg270 >= 0.350):
    #        send_value = "right"
    #    elif (deg0 <= 0.250) and (deg90 >= 0.350) and (deg270 >= 0.350) and (deg90 < deg270):
    #        send_value = "right"
    #    elif (def0 <= 0.250) and (deg90 >= 0.350) and (deg270 <= 0.350):
    #        send_value = "left"
    #    elif (deg0 <= 0.250) and (deg90 >= 0.350) and (deg270 >= 0.350) and (deg90 > deg270):
    #        send_value = "left"

    print(deg0)
    print(type(deg0))
    if deg0 > 0.250:
        send_value = "front"
    else:
        send_value = "error"
    print(deg0)
    print("range : %0.3f" %msg.ranges[0])
    print(send_value)
    pub.publish(send_value)

def send_topic():
#    pub = rospy.Publisher('send_topic', UInt16, queue_size=1000)
#    rospy.init_node('pub_value')
    global send_value
    rospy.init_node('pub_value', anonymous=True)
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    #pub = rospy.Publisher('driving', String, queue_size=10)
    rate = rospy.Rate(10)
    #pub.publish(send_value)
    rospy.spin()
        #str = "operating end %s"%rospy.get_time()
        #rospy.loginfo(str)

if __name__ == "__main__":
    try:
        send_topic()
    except rospy.ROSInterruptException:
        pass
