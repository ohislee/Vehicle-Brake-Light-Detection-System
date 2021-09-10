import cv2
import numpy as np

def nothing(x):
    pass

# Load image
image = cv2.imread('Photos/break_light4.jpg')

# Create a window
cv2.namedWindow('control')

# Create trackbars for color change
# Hue is from 0-179 for Opencv
cv2.createTrackbar('HMin', 'control', 0, 179, nothing)
cv2.createTrackbar('SMin', 'control', 0, 255, nothing)
cv2.createTrackbar('VMin', 'control', 0, 255, nothing)
cv2.createTrackbar('HMax', 'control', 0, 179, nothing)
cv2.createTrackbar('SMax', 'control', 0, 255, nothing)
cv2.createTrackbar('VMax', 'control', 0, 255, nothing)


# Set default value for Max HSV trackbars
cv2.setTrackbarPos('HMax', 'control', 179)
cv2.setTrackbarPos('SMax', 'control', 255)
cv2.setTrackbarPos('VMax', 'control', 255)

# Initialize HSV min/max values
hMin = sMin = vMin = hMax = sMax = vMax = 0
phMin = psMin = pvMin = phMax = psMax = pvMax = 0

while(1):
    # Get current positions of all trackbars
    hMin = cv2.getTrackbarPos('HMin', 'control')
    sMin = cv2.getTrackbarPos('SMin', 'control')
    vMin = cv2.getTrackbarPos('VMin', 'control')
    hMax = cv2.getTrackbarPos('HMax', 'control')
    sMax = cv2.getTrackbarPos('SMax', 'control')
    vMax = cv2.getTrackbarPos('VMax', 'control')

    # Set minimum and maximum HSV values to display
    lower = np.array([hMin, sMin, vMin])
    upper = np.array([hMax, sMax, vMax])


    # Convert to HSV format and color threshold
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    cv2.imshow('HSV', hsv)
    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Print if there is a change in HSV value
    if((phMin != hMin) | (psMin != sMin) | (pvMin != vMin) | (phMax != hMax) | (psMax != sMax) | (pvMax != vMax) ):
        print("(hMin = %d , sMin = %d, vMin = %d), (hMax = %d , sMax = %d, vMax = %d)" % (hMin , sMin , vMin, hMax, sMax , vMax))
        phMin = hMin
        psMin = sMin
        pvMin = vMin
        phMax = hMax
        psMax = sMax
        pvMax = vMax

    # Display result image
    cv2.imshow('image', result)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()