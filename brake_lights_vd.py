import cv2 as cv
import numpy as np

capture = cv.VideoCapture('Videos/car_driving.mp4')

fps = capture.get(cv.CAP_PROP_FPS)
width  = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
size = (width, height)

video_output = cv.VideoWriter('Videos/brakeLight_detection.mp4', cv.VideoWriter_fourcc(*'mp4v'), fps, size)


i = 0 # nFrames: (0 -> nframes-1)
while 1:
    ret, frame = capture.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    HSV_min = np.array([0,100,100])
    HSV_max = np.array([179,255,255])

    mask = cv.inRange(hsv, HSV_min, HSV_max)
    result = cv.bitwise_and(frame, frame, mask= mask)

    gray_result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

    contours, hierarchy = cv.findContours(gray_result, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)


    brake_light = []
    for cnt in contours:
        area = cv.contourArea(cnt)
        if 100 < area < 200:
            brake_light = cnt
            x,y,w,h = cv.boundingRect(brake_light)
            cv.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)


    #--------------saving output
    if ret:
        video_output.write(frame)
    else:
        break
    i += 1
    
    

    cv.imshow('Img', frame)

    if cv.waitKey(2) & 0xff == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
