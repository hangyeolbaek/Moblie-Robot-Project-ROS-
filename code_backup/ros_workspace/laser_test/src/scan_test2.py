#! /usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import * # python2는 Tkinter이고 python3는 tkinter이다
import time
import math
import rospy
from sensor_msgs.msg import LaserScan

window = Tk()
window.geometry("1000x1000")
window.resizable(True,True)
wt = 950 #x
hi = 950 #y
l = 50
l2 = 80

p = 20

def point(x,y,p):
    w.create_oval(x-p,y-p,x+p,y+p,tags=('a')) #x1,y1,x2,y2
    
def Time(lis):
    global c
    global wt
    global hi
    if c == 0:
        c = 1
        for T in range(0,1440,1) :
            x = wt/2 + lis[T]*math.cos(T*360/1440)
            y = hi/2 - lis[T]*math.sin(T*360/1440)
            point(x,y,20)
            window.after(10, Time) #Time 함수 반복 (간격으로 ms)
    else :
        c = 0
        w.delete('a')
        window.after(0, Time) #Time 함수 반복 (간격으로 ms)

def callback(msg):
    global c
    global wt
    global hi
    global l
    global window
    w = Canvas(window,width=wt,height=hi,bg="white")
    w.pack(expand=True)
    w.create_line(wt/2,hi/2,wt/2+l,hi/2,fill="red")
    w.create_line(wt/2,hi/2,wt/2,hi/2-l,fill="green")
    w.create_oval(wt/2-l2,hi/2-l2,wt/2+l2,hi/2+l2) #x1,y1,x2,y2 Center
    T = 0
    x = 0
    y = 0
    global f
    print len(msg.ranges) #721
    #rospy.loginfo("deg : %f" %msg.ranges[720]) #721/2 senter 0 ~ 60  #1440 /4 360
    Time(msg.ranges)




c = 0
f = 2.5


rospy.init_node('scan_test2')
sub = rospy.Subscriber('/scan', LaserScan, callback)
#sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
window.mainloop()
