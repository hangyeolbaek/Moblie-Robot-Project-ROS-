#!/usr/bin/env python
import rospy
import time
import math
import numpy as np
from std_msgs.msg import String, UInt16
from sensor_msgs.msg import LaserScan
from rospy.numpy_msg import numpy_msg
#from pub_value.msg import StringArray

def callback(msg):
  #(+)degree is left. Opposition to rplidar_A1.png
  #rospy.loginfo("deg : %0.3f" %msg.ranges[0])
    global deg0, deg30_float, deg30_str, deg40, deg45, deg78, deg90_float, deg90_str, deg270_float, deg270_str, deg282, deg315, deg320, deg330_float, deg330_str, send_value

    if msg.ranges[0] <= 8.000:
        deg0=msg.ranges[0]
        #print("^_________________________________^")
    elif msg.ranges[0] >= 8.000 and msg.ranges[1] <= 8.000:
        deg0=msg.ranges[1]
        #print("^_________________________________^")
    elif msg.ranges[0] >= 8.000 and msg.ranges[1] >= 8.000 and msg.ranges[359] <= 8.000:
        deg0=msg.ranges[359]
        #print("^_________________________________^")
    #else:
        #print("deg 0 lost")
        #print("dump")

    if msg.ranges[30] <= 8.000:
        deg30_float=msg.ranges[30]
        deg30_str=("%0.2f" %msg.ranges[30])
        #print("^_________________________________^")
    elif msg.ranges[30] >= 8.000 and msg.ranges[29] <= 8.000:
        deg30_float=msg.ranges[29]
        deg30_str=("%0.2f" %msg.ranges[29])
        #print("^_________________________________^")
    elif msg.ranges[30] >= 8.000 and msg.ranges[29] >= 8.000 and msg.ranges[31] <= 8.000:
        deg30_float=msg.ranges[31]
        deg30_str=("%0.2f" %msg.ranges[31])
        #print("^_________________________________^")
    #else:
        #print("deg 90 lost")
        #print("dump")


    if msg.ranges[40] <= 8.000:
        deg40=msg.ranges[40]
        #print("^_________________________________^")
    elif msg.ranges[40] >= 8.000 and msg.ranges[39] <= 8.000:
        deg40=msg.ranges[39]
        #print("^_________________________________^")
    elif msg.ranges[40] >= 8.000 and msg.ranges[39] >= 8.000 and msg.ranges[41] <= 8.000:
        deg40=msg.ranges[41]
        #print("^_________________________________^")
    #else:
        #print("deg 40 lost")
        #print("dump")

    if msg.ranges[45] <= 8.000:
        deg45=msg.ranges[45]
        #print("^_________________________________^")
    elif msg.ranges[45] >= 8.000 and msg.ranges[46] <= 8.000:
        deg45=msg.ranges[46]
        #print("^_________________________________^")
    elif msg.ranges[45] >= 8.000 and msg.ranges[46] >= 8.000 and msg.ranges[44] <= 8.000:
        deg45=msg.ranges[44]
        #print("^_________________________________^")
    #else:
        #print("deg 45 lost")
        #print("dump")

    if msg.ranges[78] <= 8.000:
        deg78=msg.ranges[78]
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] <= 8.000:
        deg78=msg.ranges[77]
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] >= 8.000 and msg.ranges[79] <= 8.000:
        deg78=msg.ranges[79]
        #print("^_________________________________^")
    #else:
        #print("deg 78 lost")
        #print("dump")

    if msg.ranges[90] <= 8.000:
        deg90_float=msg.ranges[90]
        deg90_str=("%0.2f" %msg.ranges[90])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] <= 8.000:
        deg90_float=msg.ranges[89]
        deg90_str=("%0.2f" %msg.ranges[89])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] >= 8.000 and msg.ranges[91] <= 8.000:
        deg90_float=msg.ranges[91]
        deg90_str=("%0.2f" %msg.ranges[91])
        #print("^_________________________________^")
    #else:
        #print("deg 90 lost")
        #print("dump")

#    if msg.ranges[137] <= 8.000:
#        deg137=msg.ranges[137]
#        #print("^_________________________________^")
#    elif msg.ranges[137] >= 8.000 and msg.ranges[136] <= 8.000:
#        deg137=msg.ranges[136]
#        #print("^_________________________________^")
#    elif msg.ranges[137] >= 8.000 and msg.ranges[136] >= 8.000 and msg.ranges[138] <= 8.000:
#        deg137=msg.ranges[138]
#        #print("^_________________________________^")
#    #else:
#        #print("deg 137 lost")
#        #print("dump")

#    if msg.ranges[223] <= 8.000:
#        deg223=msg.ranges[223]
#        #print("^_________________________________^")
#    elif msg.ranges[223] >= 8.000 and msg.ranges[224] <= 8.000:
#        deg223=msg.ranges[224]
#        #print("^_________________________________^")
#    elif msg.ranges[223] >= 8.000 and msg.ranges[224] >= 8.000 and msg.ranges[222] <= 8.000:
#        deg223=msg.ranges[222]
#        #print("^_________________________________^")
#    #else:
#        #print("deg 223 lost")
#        #print("dump")

    if msg.ranges[270] <= 8.000:
        deg270_float=msg.ranges[270]
        deg270_str=("%0.2f" %msg.ranges[270])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] <= 8.000:
        deg270_float=msg.ranges[271]
        deg270_str=("%0.2f" %msg.ranges[271])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] >= 8.000 and msg.ranges[269] <= 8.000:
        deg270_float=msg.ranges[269]
        deg270_str=("%0.2f" %msg.ranges[269])
        #print("^_________________________________^")
    #else:
        #print("deg 270 lost")
        #print("dump")

    if msg.ranges[282] <= 8.000:
        deg282=msg.ranges[282]
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] <= 8.000:
        deg282=msg.ranges[283]
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] >= 8.000 and msg.ranges[281] <= 8.000:
        deg282=msg.ranges[281]
        #print("^_________________________________^")
    #else:
        #print("deg 282 lost")
        #print("dump")
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
    #else:
        #print("deg 315 lost")
        #print("dump")
        #print("^_________________________________^")

    if msg.ranges[320] <= 8.000:
        deg320=msg.ranges[320]
        #print("^_________________________________^")
    elif msg.ranges[320] >= 8.000 and msg.ranges[321] <= 8.000:
        deg320=msg.ranges[321]
        #print("^_________________________________^")
    elif msg.ranges[320] >= 8.000 and msg.ranges[321] >= 8.000 and msg.ranges[319] <= 8.000:
        deg320=msg.ranges[319]
        #print("^_________________________________^")
    #else:
        #print("deg 320 lost")
        #print("dump")
        #print("^_________________________________^")

    if msg.ranges[330] <= 8.000:
        deg330_float=msg.ranges[330]
        deg330_str=("%0.2f" %msg.ranges[330])
        #print("^_________________________________^")
    elif msg.ranges[330] >= 8.000 and msg.ranges[331] <= 8.000:
        deg330_float=msg.ranges[331]
        deg330_str=("%0.2f" %msg.ranges[331])
        #print("^_________________________________^")
    elif msg.ranges[330] >= 8.000 and msg.ranges[331] >= 8.000 and msg.ranges[329] <= 8.000:
        deg330_float=msg.ranges[329]
        deg330_str=("%0.2f" %msg.ranges[329])
        #print("^_________________________________^")
    #else:
        #print("deg 270 lost")
        #print("dump")

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

    #if (deg0 >= 0.250):
    #    send_value = "front"
    #elif (deg0 <= 0.250):
    #    send_value = "error"

    #if ((deg0 >= 0.150) and (deg0 <= 8.000)):
    #    if (deg0 <= 0.350):
    #        send_value = "turn_left"
    #        print("left",deg0)
        #flag = 1

    #    elif (deg0 > 0.350):
            #send_value = "motor_stop"
	    #time.sleep(0.2)
    #        send_value = "front"
	    #time.sleep(0.2)
	    #flag = 0
	#    print("front",deg0)		

#first test code(deg45, deg315)
#    if ((deg0 >= 0.150) and (deg0 <= 8.000)):
#        if (deg0 > 0.250):
#            if (deg45 > 0.350):
#                if (deg315 > 0.350):
#                    send_value = "front"
#                elif (deg315 <= 0.350):
#                    if (deg90 > 0.300) and (deg270 > 0.300) and (deg90 > deg270):
#                        send_value = "left"
#                    elif (deg90 <= 0.300):
#                        send_value = "turn_left"
#            elif (deg45 <= 0.350):
#                if (deg315 > 0.350):
#                    send_value = "right"
#                elif (deg315 <= 0.350):
#                    send_value = "turn_left"
#        elif (deg0 <= 0.250):
#            if (deg90 > deg270):
#                send_value = "left"
#            elif (deg90 < deg270):
#                send_value = "right"
#            elif ((deg45 <= 0.350) and (deg78 <= 1.204) and (deg282 <= 1.204) and (deg315 <= 0.350)):
#                send_value = "turn_left"
        
    # driving when QRcode not recognized
#    if ((deg0 >= 0.150) and (deg0 <= 8.000)):
#        if (deg0 > 0.300):
#            if (deg40 > 0.390):
#                if (deg320 > 0.390):
#                    send_value = "front"
#                elif (deg320 <= 0.390):
#                    if (deg90 > 0.320) and (deg270 > 0.320):
#                        send_value = "left"
#                    elif (deg90 <= 0.320):
#                        send_value = "turn_left"
#            elif (deg40 <= 0.390):
#                if (deg320 > 0.390):
#                    if (deg90 > 0.320) and (deg270 > 0.320):
#                        send_value = "right"
#                    elif (deg270 <= 0.320):
#                        send_value = "turn_left"
#                elif (deg320 <= 0.390):
#                    send_value = "turn_left"
#        elif (deg0 <= 0.300):
#            if (deg40 > 0.390) and (deg320 <= 0.390):
#                send_value = "left"
#            elif (deg40 <= 0.390) and (deg320 > 0.390):
#                send_value = "right"
#            elif (deg40 <= 0.390) and (deg320 <= 0.390):
#                 send_value = "left"


def operating(data):
    global deg0, deg30_float, deg30_str, deg40, deg45, deg78, deg90_float, deg90_str, deg270_float, deg270_str, deg282, deg315, deg320, deg330_float, deg330_str, position, send_value, flag_for_package, sw
    position = data.data
    flag_for_package = True

    # driving when QRcode not recognized
    if position == "not_recognized": # QRcode recognized yet
        if (((deg0 >= 0.150) and (deg0 <= 8.000)) and ((deg90_float >= 0.240) and (deg90_float <= 8.000)) and ((deg270_float >= 0.240) and (deg270_float <= 8.000))):
            if (deg0 > 0.300):
                if (deg40 > 0.390):
                    if (deg320 > 0.390):
                        send_value = "front"
                    elif (deg320 <= 0.390):
                        if (deg90_float > 0.320) and (deg270_float > 0.320):
                            send_value = "left"
                        elif (deg90_float <= 0.320):
                            send_value = "turn_right"
                elif (deg40 <= 0.390):
                    if (deg320 > 0.390):
                        if (deg90_float > 0.320) and (deg270_float > 0.320):
                            send_value = "right"
                        elif (deg270_float <= 0.320):
                            send_value = "turn_left"
                    elif (deg320 <= 0.390):
                        send_value = "turn_left"
                        time.sleep()
            elif (deg0 <= 0.300):
                if (deg40 > 0.390) and (deg320 <= 0.390) and (deg90_float > deg270_float):
                    send_value = "left"
                elif (deg40 <= 0.390) and (deg320 > 0.390) and (deg90_float < deg270_float):
                    send_value = "right"
                elif (deg40 <= 0.390) and (deg320 <= 0.390) and (deg90_float > deg270_float):
                    send_value = "left"
                elif (deg40 <= 0.390) and (deg320 <= 0.390) and (deg90_float < deg270_float):
                    send_value = "right"
#        else:
#            send_value = "motor_stop"

    elif position == "match":
        #print("in the match")
        if (deg0 > 0.250):
            send_value = "front_slow"
        elif (deg0 > 0.150) and (deg0 <= 0.250):
            if (deg30_str == deg330_str):
                if ((deg90_float+deg270_float) < 0.800):
                    if((deg90_float > 0.325) and (deg90_float < 0.375) and (deg270_float > 0.325) and (deg270_float < 0.375)):
                        send_value = "front_slow"
                    else:
                        if (deg90_float < deg270_float):
                            send_value = "right_real_slow"
                        elif (deg90_float > deg270_float):
                            send_value = "left_real_slow"
            elif(deg30_str != deg330_str):
                if (deg30_float > deg330_float):
                    send_value = "turn_right"
                elif (deg30_float < deg330_float):
                    send_value = "turn_left"
        elif (deg0 <= 0.150):
            if ((deg90_float > 0.325) and (deg90_float < 0.375) and (deg270_float > 0.325) and (deg270_float < 0.375)):
                send_value = "riftup"
                time.sleep(50)
                sw = 1
            else:
                if (deg90_float < deg270_float):
                    send_value = "right_real_slow"
                elif (deg90_float > deg270_float):
                    send_value = "left_real_slow"

#            if (deg40 > 0.500) and (deg40 < 0.600) and (deg320 > 0.500) and (deg320 < 0.600):
#                send_value = "front_slow"
#            elif (deg40 < 0.500) and (deg320 > 0.600) and ((deg90_float+deg270_float) < 0.800):
#                send_value = "turn_left"
#            elif (deg40 > 0.600) and (deg320 < 0.500) and ((deg90_float+deg270_float) < 0.800):
#                send_value = "turn_right"
        #elif (deg0 > 0.150) and (deg0 <= 0.300):
#        elif (deg0 <= 0.150):
#            send_value = "riftup"
#            time.sleep(10)
#            sw += 1
            
    elif position == "match_left":
        send_value = "left_real_slow"
        #send_value = "front"
    elif position == "match_right":
        send_value = "right_real_slow"
        #send_value = "front"
    elif position == "miss_matchA_left": # input : packageB, recognize : packageA
        if position != "match":
            send_value = "right_slow"
    elif position == "miss_matchA": # input : packageB, recognize : packageA
        if position != "match":
            send_value = "right_slow"
    elif position == "miss_matchA_right": # input : packageB, recognize : packageA
        if position != "match":
            send_value = "right_slow"
    elif position == "miss_matchB_left": # input : packageA, recognize : packageB
        if position != "match":
            send_value = "left_slow"
    elif position == "miss_matchB": # input : packageA, recognize : packageB
        if position != "match":
            send_value = "left_slow"
    elif position == "miss_matchB_right": # input : packageA, recognize : packageB
        if position != "match":
            send_value = "left_slow"
            #print("===========================data.data = " + data.data + " =================================")
            #position = data.data
            #print("================================in the loop====================================")

#        send_value = "left_slow"

def send_topic():
    global send_value, sw, i, j, pub_log, flag_for_package, deg90_float, deg270_float, deg0
######################################first########################################
    rospy.init_node('pub_value', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.Subscriber('package', String, operating)
    pub = rospy.Publisher('driving', String, queue_size=10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if sw == 0:
            pub.publish(send_value)
            if send_value == "front":
                pub_log.append("back") 
                i += 1
            elif send_value == "front_slow":
                pub_log.append("back_slow") 
                i += 1
            elif send_value == "right":
                pub_log.append("left") 
                i += 1
            elif send_value == "right_slow":
                pub_log.append("left_slow") 
                i += 1
            elif send_value == "left":
                pub_log.append("right") 
                i += 1
            elif send_value == "left_slow":
                pub_log.append("right_slow") 
                i += 1
            print(pub_log)
            print("i + ", i)
        elif (sw == 1) and (flag_for_package == True):
            pub_log.reverse()
            print("before list trans = ", type(pub_log[j]))
            print(pub_log)
            sw = 2
            flag_for_package = False
        elif (sw == 2):
            if (pub_log[j] == "right_slow") and (deg270_float <= 1.000):
                pub.publish("back")
            elif ((pub_log[j] == "back") or (pub_log[j] == "left_slow") or (pub_log[j] == "right_slow")) and (deg270_float >= 1.000):
                pub.publish("right_slow")
            elif (pub_log[j] == "back_slow") and (deg270_float <= 0.500):
                pub.publish(pub_log[j])
            elif (pub_log[j] == "back_slow") and (deg270_float > 0.500) and (deg270_float <= 1.000):
                pub.publish("left_slow")
            else:
                pub.publish(pub_log[j])
            j += 1
            print("i = ", i)
            print("j = ", j)
            print("sw = ", sw)
            #if (j > 95) and (pub_log[j] == "back"):
            #    pub.publish("back")
            if ((i == j) or ((deg0 > 2.200) and (deg0 <= 8.000))):
                sw = 3
        elif (sw == 3):
            print("deg90_float = ", deg90_float)
            print("deg270_float = ", deg270_float)
            if (((deg90_float)+(deg270_float)) <= 0.800):
                #print("aaaaaaaaa")
                if ((deg90_float > 0.325) and (deg90_float < 0.375) and (deg270_float > 0.325) and (deg270_float < 0.375)):
                    pub.publish("riftdown")
                    time.sleep(42)
                    sw = 4
                #if (deg90_str != deg270_str):
                #    if (deg90_float > deg270_float):
                #        send_value = "left_real_slow"
                #    elif (deg90_float < deg270_float):
                #        send_value = "right_real_slow"
                else:
                    if (deg90_float < deg270_float):
                        pub.publish("right_real_slow")
                    elif (deg90_float > deg270_float):
                        pub.publish("left_real_slow")
            else:
                pub.publish("back_slow")
            print("sw = 3")
        elif (sw == 4):
            pub.publish("motor_stop")
            print("sw = 4")
        rate.sleep()

##########################################error_code#################################################
#    rospy.init_node('pub_value', anonymous=True)
#    rospy.Subscriber('/scan', LaserScan, callback)
#    rospy.Subscriber('package', String, operating)
#    if sw == 0:
#        pub = rospy.Publisher('driving', String, queue_size=10)
#        rate = rospy.Rate(10)
#        while not rospy.is_shutdown():
#            pub.publish(send_value)
#            if send_value == "front":
#                pub_log.append("back")
#            elif send_value == "front_slow":
#                pub_log.append("back_slow")
#            elif send_value == "right":
#                pub_log.append("left")
#            elif send_value == "right_slow":
#                pub_log.append("left_slow")
#            elif send_value == "left":
#                pub_log.append("right")
#            elif send_value == "left_slow":
#                pub_log.append("right_slow")
#            i += 1
#            print(pub_log)
#            rate.sleep()
#    elif sw == 1:
#        pub = rospy.Publisher('driving', String, queue_size=10)
#        rate = rospy.Rate(10)
#        pub_log.reverse()
#        while not rospy.is_shutdown():
#            print("before list trans = ", type(pub_log[j]))
#            pub.publish(pub_log[j])
#            j += 1
#            if i == j:
#                send_value = "riftdown"
#                time.sleep(50)
#                sw += 1
#            print(pub_log)
#            rate.sleep()
#    elif sw == 2:
#        pub = rospy.Publisher('driving', String, queue_size=10)
#        rate = rospy.Rate(10)
#        while not rospy.is_shutdown():
#            pub.publish("motor_stop")
#            print(pub_log)
#            rate.sleep()

if __name__ == '__main__':
    deg0=0
    deg30_float=0
    deg30_str=0
    deg40=0
    deg45=0
    deg78=0
    deg90_float=0
    deg90_str=0
    deg270_float=0
    deg270_str=0
    deg282=0
    deg315=0
    deg320=0
    deg330_float=0
    deg330_str=0
    position = "initial value"
    send_value = "initial value"
    flag_for_package = True
    i=0
    j=10
    sw = 0
    pub_log = list()
    try:
        send_topic()
    except rospy.ROSInterruptException:
        pass
