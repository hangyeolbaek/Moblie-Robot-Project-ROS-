import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
  #(+)degree is left. Opposition to rplidar_A1.png
  #rospy.loginfo("deg : %0.3f" %msg.ranges[0])
#    global d
#    print("deg 0 : %0.3f" %msg.ranges[0]) #front
#    print("deg +78 : %0.3f" %msg.ranges[78])
#    print("deg +90 : %0.3f" %msg.ranges[90])# left
#    print("deg +137 : %0.3f" %msg.ranges[137])
#    print("deg +223(-137) : %0.3f" %msg.ranges[223])
#    print("deg +270(-90) : %0.3f" %msg.ranges[270]) # right
#    print("deg +282(-78) : %0.3f" %msg.ranges[282])

#    print("deg 89 : %0.3f" %msg.ranges[89])
#    print("deg 90 : %0.3f" %msg.ranges[90])
#    print("deg 91 : %0.3f" %msg.ranges[91])
#    print("^_________________________________^")

    global deg0, deg40, deg78, deg90, deg137, deg223, deg270, deg282, deg320
    deg0=("%0.3f" %msg.ranges[0]) #front
    deg40=("%0.3f" %msg.ranges[40])
    deg78=("%0.3f" %msg.ranges[78])
    deg90=("%0.3f" %msg.ranges[90])# left
    deg137=("%0.3f" %msg.ranges[137])
    deg223=("%0.3f" %msg.ranges[223])
    deg270=("%0.3f" %msg.ranges[270]) # right
    deg282=("%0.3f" %msg.ranges[282])
    deg320=("%0.3f" %msg.ranges[320])

#    print(deg0)
#    print(deg78)
#    print(deg90)
#    print(deg137)
#    print(deg223)
#    print(deg270)
#    print(deg282)
#    print("^_________________________________^")

#    if msg.ranges[0] <= 8.000:
#        deg0=("%0.3f" %msg.ranges[0])
#    elif msg.ranges[0] >= 8.000 and msg.ranges[1] <= 8.000:
#        deg0=("%0.3f" %msg.ranges[1])
#    elif msg.ranges[0] >= 8.000 and msg.ranges[1] >= 8.000 and msg.ranges[359] <= 8.000:
#        deg0=("%0.3f" %msg.ranges359])lidar
#    else:
#        print("deg 0 lost")

    if msg.ranges[0] <= 8.000:
        print("deg 0 : %0.3f" %msg.ranges[0])
        #print("^_________________________________^")
    elif msg.ranges[0] >= 8.000 and msg.ranges[1] <= 8.000:
        print("deg 1 : %0.3f" %msg.ranges[1])
        #print("^_________________________________^")
    elif msg.ranges[0] >= 8.000 and msg.ranges[1] >= 8.000 and msg.ranges[359] <= 8.000:
        print("deg 359 : %0.3f" %msg.ranges[359])
        #print("^_________________________________^")
    else:
        print("deg 0 is lost value")

    if msg.ranges[40] <= 8.000:
        print("deg 40 : %0.3f" %msg.ranges[40])
        #print("^_________________________________^")
    elif msg.ranges[40] >= 8.000 and msg.ranges[39] <= 8.000:
        print("deg 39 : %0.3f" %msg.ranges[39])
        #print("^_________________________________^")
    elif msg.ranges[40] >= 8.000 and msg.ranges[39] >= 8.000 and msg.ranges[41] <= 8.000:
        print("deg 41 : %0.3f" %msg.ranges[41])
        #print("^_________________________________^")
    else:
        print("deg 40 is lost value")

    if msg.ranges[78] <= 8.000:
        print("deg 78 : %0.3f" %msg.ranges[78])
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] <= 8.000:
        print("deg 77 : %0.3f" %msg.ranges[77])
        #print("^_________________________________^")
    elif msg.ranges[78] >= 8.000 and msg.ranges[77] >= 8.000 and msg.ranges[79] <= 8.000:
        print("deg 79 : %0.3f" %msg.ranges[79])
        #print("^_________________________________^")
    else:
        print("deg 78 is lost value")

    if msg.ranges[90] <= 8.000:
       print("deg 90 : %0.3f" %msg.ranges[90])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] <= 8.000:
        print("deg 89 : %0.3f" %msg.ranges[89])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] >= 8.000 and msg.ranges[91] <= 8.000:
        print("deg 91 : %0.3f" %msg.ranges[91])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] >= 8.000 and msg.ranges[91] >= 8.000 and msg.ranges[88] <= 8.000:
        print("deg 88 : %0.3f" %msg.ranges[88])
        #print("^_________________________________^")
    elif msg.ranges[90] >= 8.000 and msg.ranges[89] >= 8.000 and msg.ranges[91] <= 8.000 and msg.ranges[88] >= 8.000 and msg.ranges[92] <= 8.000:
        print("deg 92 : %0.3f" %msg.ranges[92])
        #print("^_________________________________^")
    else:
        print("deg 90 is lost value")

    if msg.ranges[137] <= 8.000:
        print("deg 137 : %0.3f" %msg.ranges[137])
        #print("^_________________________________^")
    elif msg.ranges[137] >= 8.000 and msg.ranges[136] <= 8.000:
        print("deg 136 : %0.3f" %msg.ranges[136])
        #print("^_________________________________^")
    elif msg.ranges[137] >= 8.000 and msg.ranges[136] >= 8.000 and msg.ranges[138] <= 8.000:
        print("deg 138 : %0.3f" %msg.ranges[138])
        #print("^_________________________________^")
    else:
        print("deg 137 is lost value")

    if msg.ranges[223] <= 8.000:
        print("deg 223 : %0.3f" %msg.ranges[223])
        #print("^_________________________________^")
    elif msg.ranges[223] >= 8.000 and msg.ranges[224] <= 8.000:
        print("deg 224 : %0.3f" %msg.ranges[224])
        #print("^_________________________________^")
    elif msg.ranges[223] >= 8.000 and msg.ranges[224] >= 8.000 and msg.ranges[222] <= 8.000:
        print("deg 222 : %0.3f" %msg.ranges[222])
        #print("^_________________________________^")
    else:
        print("deg 223 is lost value")

    if msg.ranges[270] <= 8.000:
        print("deg 270 : %0.3f" %msg.ranges[270])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] <= 8.000:
        print("deg 271 : %0.3f" %msg.ranges[271])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] >= 8.000 and msg.ranges[269] <= 8.000:
        print("deg 269 : %0.3f" %msg.ranges[269])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] >= 8.000 and msg.ranges[269] >= 8.000 and msg.ranges[272] <= 8.000:
        print("deg 272 : %0.3f" %msg.ranges[272])
        #print("^_________________________________^")
    elif msg.ranges[270] >= 8.000 and msg.ranges[271] >= 8.000 and msg.ranges[269] >= 8.000 and msg.ranges[272] >= 8.000 and msg.ranges[268] <= 8.000:
        print("deg 268 : %0.3f" %msg.ranges[268])
        #print("^_________________________________^")
    else:
        print("deg 270 is lost value")

    if msg.ranges[282] <= 8.000:
        print("deg 282 : %0.3f" %msg.ranges[282])
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] <= 8.000:
        print("deg 283 : %0.3f" %msg.ranges[283])
        #print("^_________________________________^")
    elif msg.ranges[282] >= 8.000 and msg.ranges[283] >= 8.000 and msg.ranges[281] <= 8.000:
        print("deg 281 : %0.3f" %msg.ranges[281])
        #print("^_________________________________^")
    else:
        print("deg 282 is lost value")
        #print("^_________________________________^")

    if msg.ranges[320] <= 8.000:
        print("deg 320 : %0.3f" %msg.ranges[320])
        print("^_________________________________^")
    elif msg.ranges[320] >= 8.000 and msg.ranges[321] <= 8.000:
        print("deg 321 : %0.3f" %msg.ranges[321])
        print("^_________________________________^")
    elif msg.ranges[320] >= 8.000 and msg.ranges[321] >= 8.000 and msg.ranges[319] <= 8.000:
        print("deg 319 : %0.3f" %msg.ranges[319])
        print("^_________________________________^")
    else:
        print("deg 320 is lost value")
        print("^_________________________________^")

    #if (((msg.ranges[0] >= 0.15) and (msg.ranges[0] <= 8.00)) and ((msg.ranges[78] >= 0.24) and (msg.ranges[78] <= 8.00)) and ((msg.ranges[90] >= 0.24) and (msg.ranges[90] <= 8.00)) and ((msg.ranges[137] >= 0.40) and (msg.ranges[137] <= 8.00)) and ((msg.ranges[223] >= 0.40) and (msg.ranges[223] <= 8.00)) and ((msg.ranges[270] >= 0.24) and (msg.ranges[270] <= 8.00)) and ((msg.ranges[282] >= 0.24) and (msg.ranges[282] <= 8.00))):

    #if (((deg0 >= 0.15) and (deg0 <= 8.00)) and ((deg78 >= 0.24) and (deg78 <= 8.00)) and ((deg90 >= 0.24) and (deg90 <= 8.00)) and ((deg137 >= 0.40) and (deg137 <= 8.00)) and ((deg223 >= 0.40) and (deg223 <= 8.00)) and ((deg270 >= 0.24) and (deg270 <= 8.00)) and ((deg282 >= 0.24) and (deg282 <= 8.00))):

    #print(deg0)
    #print(deg78)
    #print(deg90)
    #print(deg137)
    #print(deg223)
    #print(deg270)
    #print(deg282)

    if (((msg.ranges[0] >= 0.150) and (msg.ranges[0] <= 8.000)) and ((msg.ranges[78] >= 0.240) and (msg.ranges[78] <= 8.000)) and ((msg.ranges[90] >= 0.240) and (msg.ranges[90] <= 8.000)) and ((msg.ranges[137] >= 0.400) and (msg.ranges[137] <= 8.000)) and ((msg.ranges[223] >= 0.400) and (msg.ranges[223] <= 8.000)) and ((msg.ranges[270] >= 0.240) and (msg.ranges[270] <= 8.000)) and ((msg.ranges[282] >= 0.240) and (msg.ranges[282] <= 8.000))):
        print("value = 1")
    else:
        print("value = 0")

deg0=0
deg40=0
deg78=0
deg90=0
deg137=0
deg223=0
deg270=0
deg282=0
deg320=0
rospy.init_node('value_test')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()
