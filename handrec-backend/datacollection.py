import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
from matplotlib.pyplot import imshow
import time
import math

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)

# For adding the margins
offset = 20
# Pixel size
imgSize = 300

folder = "Data/C"
counter = 0

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        # The dimensions of the box
        x, y, w, h = hand['bbox']

        # Creating a box shape so that the size of image box would be one
        # uint8 - 0-255 color range
        imgWhite = np.ones((imgSize,imgSize,3),np.uint8)*255

        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        # This shape is the matrix of 3 things h,w and channels but we don't need channels
        imgCropShape = imgCrop.shape

        # Filling/removing the white space of the box
        aspectRatio = h/w
        if aspectRatio > 1:
            k = imgSize/h
            # ceil to roundoff to high
            wCal = math.ceil(k*w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))

            # This shape is the matrix of 3 things h,w and channels but we don't need channels
            imgResizeShape = imgResize.shape

            # To center the image in white box
            wGap =math.ceil((imgSize-wCal)/2)

            # height is same hence removed
            imgWhite[:, wGap:wCal+wGap] = imgResize

        else:
                k = imgSize / w
                # ceil to roundoff to high
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))

                # This shape is the matrix of 3 things h,w and channels but we don't need channels
                imgResizeShape = imgResize.shape

                # To center the image in white box
                hGap = math.ceil((imgSize - hCal) / 2)

                # height is same hence removed
                imgWhite[hGap:hCal + hGap, :] = imgResize

        cv2.imshow("ImageCrop", imgCrop)
        cv2.imshow("ImageWhite", imgWhite)

    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imgWhite)
        print(counter)