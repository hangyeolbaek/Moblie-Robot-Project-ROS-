#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyzbar.pyzbar as pyzbar
import cv2
import numpy
import rospy
from std_msgs.msg import String

def pub_package():
    global goal_package
    global recog_package
    goal_package = raw_input('what is the goal package?(packageA or packageB) : ')
    rospy.init_node('pub_package', anonymous=True)
    pub = rospy.Publisher('package', String, queue_size=10)
    rate = rospy.Rate(10)
    cap = cv2.VideoCapture(0)
    i = 0
    while True:
        ret, img = cap.read()

        #print(img.shape)
        #img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
        #img = img[0: 480, 320: 960]
        #print(img.shape)

        if not ret:
            print("damm")
            continue

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        decoded = pyzbar.decode(gray)

        for d in decoded: 
            x, y, w, h = d.rect

            barcode_data = d.data.decode("utf-8")
            barcode_type = d.type

            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            #recog_package = "not_recognized"

            if goal_package == "packageA":
                if barcode_data == "packageA":
                    if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
                        print("packageA: move left")
                        recog_package = "match_left"
                    elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
                        print("packageA: move left")
                        recog_package = "match_left"
                    elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
                        print("packageA: This is center")
                        recog_package = "match"
                        while True:
                            pub.publish(recog_package)
                    elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
                        print("packageA: This is center")
                        recog_package = "match"
                        while True:
                            pub.publish(recog_package)
                    elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
                        print("packageA: move right")
                        recog_package = "match_right"
                    elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
                        print("packageA: move right")
                        recog_package = "match_right"
                elif barcode_data == "packageB":
                    if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
                        print("packageB: move left")
                        recog_package = "miss_matchB_left"
                    elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
                        print("packageB: move left")
                        recog_package = "miss_matchB_left"
                    elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
                        print("packageB: This is center")
                        recog_package = "miss_matchB"
                    elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
                        print("packageB: This is center")
                        recog_package = "miss_matchB"
                    elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
                        print("packageB: move right")
                        recog_package = "miss_matchB_right"
                    elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
                        print("packageB: move right")
                        recog_package = "miss_matchB_right"

            elif goal_package == "packageB":
                if barcode_data == "packageA":
                    if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
                        #print("packageA: move left")
                        recog_package = "miss_matchA_left"
                    elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
                        #print("packageA: move left")
                        recog_package = "miss_matchA_left"
                    elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
                        #print("packageA: This is center")
                        recog_package = "miss_matchA"
                    elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
                        #print("packageA: This is center")
                        recog_package = "miss_matchA"
                    elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
                        #print("packageA: move right")
                        recog_package = "miss_matchA_right"
                    elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
                        #print("packageA: move right")
                        recog_package = "miss_matchA_right"
                elif barcode_data == "packageB":
                    if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
                        #print("packageB: move left")
                        recog_package = "match_left"
                    elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
                        #print("packageB: move left")
                        recog_package = "match_left"
                    elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
                        #print("packageB: This is center")
                        recog_package = "match"
                        while True:
                            pub.publish(recog_package)
                    elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
                        #print("packageB: This is center")
                        recog_package = "match"
                        while True:
                            pub.publish(recog_package)
                    elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
                        #print("packageB: move right")
                        recog_package = "match_right"
                    elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
                        #print("packageB: move right")
                        recog_package = "match_right"
            else:
                print("wrong input try again")
                #text = '%s (%s)' % (barcode_data, barcode_type)
                #cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('img', img)

        pub.publish(recog_package)
        rate.sleep()

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    goal_package = "empty"
    recog_package = "not_recognized"
    try:
        pub_package()
    except rospy.ROSInterruptException:
        pass
