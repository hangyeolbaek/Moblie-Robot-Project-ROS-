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
l2 = 100*2


def point(x,y,p):
    w.create_oval(x-p,y-p,x+p,y+p,tags=('a')) #x1,y1,x2,y2
    
def Time(lis):
    global c
    global wt
    global hi
    global window
    #T = 1000
    #print lis[T]
    w.delete('a')
    for T in range(0,1440,2) :
        x = wt/2 + 70*lis[T]*math.cos(T*360/1440*math.pi/180)
        y = hi/2 - 70*lis[T]*math.sin(T*360/1440*math.pi/180)
        point(x,y,1)
        x = wt/2 + 70*lis[1440-(T/2+1)]*math.cos((1440-(T/2+1))*360/1440*math.pi/180)
        y = hi/2 - 70*lis[1440-(T/2+1)]*math.sin((1440-(T/2+1))*360/1440*math.pi/180)
        point(x,y,1)


def callback(msg):
    rospy.loginfo("deg : %f" %msg.ranges[720]) #721/2 senter 0 ~ 60  #1440 /4 360
    Time(msg.ranges)
    time.sleep(0.0001)




c = 0
w = Canvas(window,width=wt,height=hi,bg="white")
w.pack(expand=True)
w.create_line(wt/2,hi/2,wt/2+l,hi/2,fill="red")
w.create_line(wt/2,hi/2,wt/2,hi/2-l,fill="green")
w.create_oval(wt/2-l2,hi/2-l2,wt/2+l2,hi/2+l2) #x1,y1,x2,y2 Center

rospy.init_node('scan_test2')
sub = rospy.Subscriber('/scan', LaserScan, callback)
window.mainloop()





