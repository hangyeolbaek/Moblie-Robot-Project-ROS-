import pyzbar.pyzbar as pyzbar
import cv2

# def func(codedata, xpoint, xwpoint):
#     if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
#         print("packageA: move left")
#     elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
#          print("packageA: move left")
#     elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
#         print("packageA: This is center")
#     elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
#         print("packageA: This is center")
#     elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
#         print("packageA: move right")
#     elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
#         print("packageA: move right")

cap = cv2.VideoCapture(0)

i = 0
while(cap.isOpened()):
    ret, img = cap.read()

    #img = cv2.resize(img, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    img = img[0: 480, 320: 960]

    if not ret:
        continue

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
    decoded = pyzbar.decode(gray)

    for d in decoded: 
        x, y, w, h = d.rect

        barcode_data = d.data.decode("utf-8")
        barcode_type = d.type

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        if barcode_data == "packageA":
            if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
                print("packageA: move left")
            elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
                print("packageA: move left")
            elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
                print("packageA: This is center")
            elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
                print("packageA: This is center")
            elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
                print("packageA: move right")
            elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
                print("packageA: move right")
        elif barcode_data == "packageB":
            if (((x > 0) and (x < 213)) and ((x + w) > 0) and ((x + w) < 213)): #두 점 모두 sec1에 위치(왼쪽)
                print("packageB: move left")
            elif (((x > 0) and (x < 213)) and ((x + w) > 213) and ((x + w) < 426)): #x점이 sec1, (x + w)점이 sec2일 때(왼쪽)
                print("packageB: move left")
            elif (((x > 213) and (x < 426)) and ((x + w) > 213) and ((x + w) < 426)): #두 점 모두 sec2에 위치(중앙)
                print("packageB: This is center")
            elif (((x > 0) and (x < 213)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec1, (x + w)점이 sec3일 때(가까운 중앙)
                print("packageB: This is center")
            elif (((x > 213) and (x < 426)) and ((x + w) > 426) and ((x + w) < 640)): #x점이 sec2, (x + w)점이 sec3일 때(오른쪽)
                print("packageB: move right")
            elif (((x > 426) and (x < 640)) and ((x + w) > 426) and ((x + w) < 640)): #두 점 모두 sec3에 위치(오른쪽)
                print("packageB: move right")
        #text = '%s (%s)' % (barcode_data, barcode_type)
        #cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('img', img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    cap.release()
    cv2.destroyAllWindows()