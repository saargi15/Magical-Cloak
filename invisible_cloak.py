import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        break

background = cv2.imread("./image.jpg")
background = cv2.resize(background, (frame.shape[1], frame.shape[0]))

while cap.isOpened():
    ret, current_frame = cap.read()
    if ret:
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        lower_green1 = np.array([35, 60, 60]) 
        upper_green1 = np.array([70, 255, 255])

        lower_green2 = np.array([70, 60, 60])
        upper_green2 = np.array([90, 255, 255])

        mask1 = cv2.inRange(hsv_frame, lower_green1, upper_green1)
        mask2 = cv2.inRange(hsv_frame, lower_green2, upper_green2)

        green_mask = mask1 + mask2

       
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=2)
        green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)

        part1 = cv2.bitwise_and(background, background, mask=green_mask)

        inverse_mask = cv2.bitwise_not(green_mask)
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=inverse_mask)

        final = part1 + part2

        cv2.imshow("Invisible Green Cloak", final)

        if cv2.waitKey(5) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()

