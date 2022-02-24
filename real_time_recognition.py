import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

from tensorflow.keras.models import load_model

#手を映す位置をあらかじめ決めておいてその部分を切り抜いて分類することで手を探す処理を省くことができる？
model = load_model(r"D:/Research/Model/kaggle_model/")

cap = cv2.VideoCapture(0)
image_size = (32,32)

def divide_frame(frame):
    height,width,channels = frame.shape
    upper_right = frame[0:height // 2 + 200,0:width // 2]
    cv2.imshow('upper_right',upper_right)

def number_of_elements(img):
    H = []
    S = []
    V = []
    for i in range(0,32):
        for j in range(0,32):
            H.append(img[i][j][0])
            S.append(img[i][j][1])
            V.append(img[i][j][2])
    return H, S, V

def binarization_image(img):
    lower = np.array([0, 0, 0], dtype='uint8')
    upper = np.array([90, 10, 255], dtype='uint8')
    skinRegionHSV = cv2.inRange(img, lower, upper)
    bin = cv2.blur(skinRegionHSV, (2, 2))
    _, thresh = cv2.threshold(bin, 0, 255, cv2.THRESH_BINARY)
    return img

while True:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(640,480))
        img = divide_frame(frame)
        img = cv2.resize(img,image_size)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        img = binarization_image(img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()