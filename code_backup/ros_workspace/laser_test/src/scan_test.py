#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan


def callback(msg):
    global c
    print len(msg.ranges) #721
    rospy.loginfo("deg : %f" %msg.ranges[720]) #721/2 senter 0 ~ 60  #1440 /4 360
    if msg.ranges[720] < 2:
        print "2m"
    
    
    
    print(c)
    if c < 255 :
        c += 1
    else :
        c = 0

c = 0
rospy.init_node('scan_test')
sub = rospy.Subscriber('/scan', LaserScan, callback)
#sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
rospy.spin()
