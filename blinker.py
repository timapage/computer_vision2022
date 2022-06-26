import re
from unittest import result
from winreg import REG_RESOURCE_LIST
import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot
from time import sleep

import serial
ser = serial.Serial('COM3',9600)
ser.write(b'a')


# cap = cv2.VideoCapture('Video.mp4')
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640, 360, [20, 50], invert=True)
# [160, 33, 161, 163, 133, 7, 173, 144, 145, 246, 153, 154, 155, 157, 158, 159]
idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
# idList_left = [263, 249, 390, 373, 374, 380, 381, 382, 362, 467, 260, 259, 257, 258, 286, 414]
idList_left = [384, 385, 386, 387, 388, 390, 263, 362, 398, 466, 373, 374, 249, 380, 381, 382]
idLips = [0, 267, 269, 270, 13, 14, 17, 402, 146, 405, 409, 415, 291, 37, 39, 40, 178, 308, 181, 310, 311, 312, 185, 314, 317, 
318, 61, 191, 321, 324, 78, 80, 81, 82, 84, 87, 88, 91, 95, 375]
ratioList = []
ratioListLips = []
ratio_list_right = []
blinkCounter = 0
blinkCounter_right = 0
blinkCounter_lips = 0
counter = 0
counter_right = 0
counter_lips = 0
color = (255, 0, 0)
color_left = (0, 0, 255)
color_lips = (255,255,51)
last_action = ''
while True:

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5,color, cv2.FILLED)
        

        if faces:
            face = faces[0]
            for id in idLips:
                # cv2.circle(img, face[id], 5,color, cv2.FILLED)
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,500)
                fontScale              = 0.5
                fontColor              = (255,255,255)
                thickness              = 1
                lineType               = 2

                cv2.putText(img,f'{id}', 
                    face[id],
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
                          # cv2.circle(img, face[id], 5,color_left, cv2.FILLED)
            # font = cv2.FONT_HERSHEY_SIMPLEX
            # bottomLeftCornerOfText = (10,500)
            # fontScale              = 0.5
            # fontColor              = (255,255,255)
            # thickness              = 1
            # lineType               = 2

            # cv2.putText(img,f'{id}', 
            #     face[id], 
            #     font, 
            #     fontScale,
            #     fontColor,
            #     thickness,
            #     lineType)
        
        for id in idList_left:
            # if id==380 or id==257 or id==414 or id==467:
            #     cv2.circle(img, face[id], 5, (0,0,0), cv2.FILLED)
            # el
            if id==385:
                cv2.circle(img, face[id], 5, (255,255,51), cv2.FILLED)

                # font                   = cv2.FONT_HERSHEY_SIMPLEX
                # bottomLeftCornerOfText = (10,500)
                # fontScale              = 0.5
                # fontColor              = (255,255,255)
                # thickness              = 1
                # lineType               = 2

                # cv2.putText(img,f'{id}', 
                #     face[id], 
                #     font, 
                #     fontScale,
                #     fontColor,
                #     thickness,
                #     lineType)
                #sariq
            elif id==263:
                cv2.circle(img, face[id], 5, (0,255,51), cv2.FILLED)
                #pushti
            # elif id==259:
            #     cv2.circle(img, face[id], 5, (222,222,222), cv2.FILLED)
            #     #gray
            elif id==374:
                cv2.circle(img, face[id], 5, (255,102,255), cv2.FILLED)
                #pushti
            elif id==467:
                cv2.circle(img, face[id], 5, (26,203,230), cv2.FILLED)
                #och ko'k
            else:
                cv2.circle(img, face[id], 5,color_left, cv2.FILLED)
                # font = cv2.FONT_HERSHEY_SIMPLEX
                # bottomLeftCornerOfText = (10,500)
                # fontScale              = 0.5
                # fontColor              = (255,255,255)
                # thickness              = 1
                # lineType               = 2
                # cv2.putText(img,f'{id}', 
                #     face[id], 
                #     font, 
                #     fontScale,
                #     fontColor,
                #     thickness,
                #     lineType)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]

        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)
        # 380 or id==257 or id==414 or id==467

        #  = [384, 385, 386, 387, 388, 390, 263, 362, 398, 466, 373, 374, 249, 380, 381, 382]

        rightUp = face[386]
        rightDown = face[374]
        rightLeft = face[263]
        rightRight = face[398] #467 
        lenghtVer_right, _ = detector.findDistance(rightUp, rightDown)
        lenghtHor_right, _ = detector.findDistance(rightLeft, rightRight)
        # print(lenghtVer_right)
        # print(lenghtHor_right)

        lipUp = face[82]
        lipDown = face[87]
        lipLeft = face[61]
        lipRight = face[324]

        lenghtVerLips, _ = detector.findDistance(lipUp, lipDown)
        lenghtHorLips, _ = detector.findDistance(lipLeft, lipRight)



        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        cv2.line(img, rightUp, rightDown, (0, 200, 0), 3)
        cv2.line(img, rightLeft, rightRight, (0, 200, 0), 3)

        cv2.line(img, lipUp, lipDown, (0, 200, 0), 3)
        cv2.line(img, lipLeft, lipRight, (0, 200, 0), 3)

        ratio = int((lenghtVer / lenghtHor) * 100)
        ratio_right = int((lenghtVer_right / lenghtHor_right) * 100)
        ratioList.append(ratio)
        ratio_list_right.append(ratio_right)
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)



        ratio = int((lenghtVerLips / lenghtHorLips) * 100)
        ratioListLips.append(ratio)
        if len(ratioListLips) > 3:
            ratioListLips.pop(0)
        ratioAvgLips = sum(ratioListLips) / len(ratioListLips)




        if len(ratio_list_right) > 3:
            ratio_list_right.pop(0)
        ratioAvg_right = sum(ratio_list_right) / len(ratio_list_right)
        # print('ratioAvg',ratioAvg_right)
        if ratioAvgLips > 31:
                blinkCounter_lips += 1
                color = (0,200,0)
                counter = 1
                result = "ogiz"
                if result == "ogiz":
                    if result != last_action:
                        print(result)
                        last_action = result
                        ser.write(b'1')
                        sleep(5)

                    
                blinkCounter_lips+=1
                # if result == "oldinga":
                #     ser.write(b'2')
                # if result == "onga":
                #     ser.write(b'1')
                # if result == "chapga":
                #     ser.write(b'4')
            # if counter != 0:
            #     counter += 1
            #     if counter > 10:
            #         counter = 0
            #         color = (255,0, 255)
        elif ratioAvg < 31 and ratioAvg_right < 31 and blinkCounter > 2:
            blinkCounter += 1
            color = (0,200,0)
            counter = 1
            result = "ikki"
            if result == "ikki":
                if result != last_action:
                    print(result) 
                    ser.write(b'2')
                    last_action = result
                    sleep(5)
        else:
            if ratioAvg < 31 and counter == 0:
                blinkCounter += 1
                color = (0,200,0)
                counter = 1
                result = "chap"
                if result == "chap":
                    if result != last_action:
                        print(result)
                        ser.write(b'4')
                        last_action = result
                        sleep(5)
                # if result == "oldinga":
                #     ser.write(b'2')
                # if result == "onga":
                #     ser.write(b'1')
                # if result == "chapga":
                #     ser.write(b'4')
            if counter != 0:
                counter += 1
                if counter > 10:
                    counter = 0
                    color = (255,0, 255)


            if ratioAvg_right < 31 and counter_right == 0:
                blinkCounter_right += 1
                color = (0,200,0)
                counter_right = 1
                result = "ong"
                if result == "ong":
                    if result != last_action:
                        print(result)
                        last_action = result
                        ser.write(b'3')
                        sleep(5)
            if counter_right != 0:
                counter_right += 1
                if counter_right > 10:
                    counter_right = 0
                    color = (255,0, 255)

        # cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100),
        #                    colorR=color)
        

        # cvzone.putTextRect(img, f'Blink Count ong: {blinkCounter_right}', (100, 50),
        #             colorR=color)
        

        # if result == "ogiz":
        #     if result != last_action:
        #         print(result)
        #         last_action = result
        #         ser.write(b'1')
        # elif result == "ikki":
        #     if result != last_action:
        #         print(result)
        #         last_action = result
        #         ser.write(b'2')
        # elif result == "chap":
        #     if result != last_action:
        #         print(result)
        #         last_action = result
        #         ser.write(b'4')
                
        # elif result == "ong":
        #     if result != last_action:
        #         print(result)
        #         last_action = result
        #         ser.write(b'3')

        imgPlot = plotY.update(ratioAvgLips, color)
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
    else:
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, img], 2, 1)

    cv2.imshow("Image", imgStack)
    cv2.waitKey(25)

# if result == "orqaga":
#         ser.write(b'3')
# if result == "oldinga":
#     ser.write(b'2')
# if result == "onga":
#     ser.write(b'1')
# if result == "chapga":
#     ser.write(b'4')