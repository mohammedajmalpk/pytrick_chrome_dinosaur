import cv2
import numpy as np
import pyautogui

cap = cv2.VideoCapture(0)

hand_cascade = cv2.CascadeClassifier('hand.xml')
fist_cascade = cv2.CascadeClassifier('fist.xml')

while True:
    ret,frame  = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #hands = hand_cascade.detectMultiScale(gray, 1.1, 5)
    fist = fist_cascade.detectMultiScale(gray, 1.1, 5)
    for (x,y,w,h) in fist:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        pyautogui.press('space')


    cv2.imshow('frame',frame)

    if cv2.waitKey(10) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()


