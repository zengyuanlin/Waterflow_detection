# -*- coding: utf-8 -*- 
# @Time : 2021/11/9 17:07 
# @Author : lijie 
# @File : main.py
import cv2

if __name__ == '__main__':
    print("The opencv version is " + cv2.__version__)
    # 写视频是否使能
    writeVideoFlag = True
    openVideFlag = False

    # 重新定义视频窗口尺寸
    if writeVideoFlag:
        windowNewName = "frame"
        w1 = 640
        h1 = 480
        cv2.namedWindow(windowNewName, 0)
        cv2.resizeWindow(windowNewName, w1, h1)

    rtspUrl = "rtsp://42.192.163.202:5548/record/streamh264.mp4"

    cap = cv2.VideoCapture(rtspUrl)

    # 判断摄像机是否正确打开
    if cap.isOpened():
        print("The video is opening")
        openVideFlag = True
    else:
        print("The video is closed")
        openVideFlag = False
    while openVideFlag:
        success, frame = cap.read()
        if success != True:
            break
        cv2.imshow("frame", frame)

        k = cv2.waitKey(1)
        # if cv2.getWindowProperty(windowNewName, cv2.WND_PROP_AUTOSIZE) < 1:
        #     break
        # if k == 27:
        #     break
    #退出GUI窗口
    cap.release()
    cv2.destroyAllWindows()

