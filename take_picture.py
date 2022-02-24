import cv2
import os


def divide_frame(frame):
    height, width, channels = frame.shape
    upper_right = frame[0:height // 2 + 200, 0:width // 2]
    cv2.imshow('upper_right', upper_right)
    return upper_right

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(640,480))
        frame = divide_frame(frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cap_path = r'D:/Research/Frame/testImage/'
            os.makedirs(cap_path,exist_ok=True)
            cv2.imwrite(cap_path+'g5_test.png', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()