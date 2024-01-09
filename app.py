import cv2 
import numpy as np

cap = cv2.VideoCapture(0)

overlay = cv2.imread('jewellery.png')
size = 400
overlay = cv2.resize(overlay, (size,size))

img2gray = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 1, 255, cv2.THRESH_BINARY)

while True:
    ret, frame = cap.read()
    center_row = frame.shape[0] // 2
    center_col = frame.shape[1] // 2
    start_row = center_row - size // 2
    end_row = start_row + size
    start_col = center_col - size // 2
    end_col = start_col + size
    # Region of Image (ROI), set to the middle of the screen
    roi = frame[start_row:end_row, start_col:end_col]
    roi[np.where(mask)] = 0
    roi += overlay

    cv2.imshow("webcam", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()