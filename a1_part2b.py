#We, Anthony Su and Yingyong L. (mention assigned group number and your names), declare that the attached assignment is our own work in accordance with the Seneca Academic Policy.  We have not copied any part of this assignment, manually or electronically, from any other source including web sites, unless specified as references. We have not distributed our work to other students.
import cv2 as cv
import numpy as np

# i. Open and read two images
img1 = cv.imread('lambo.jpg')
img2 = cv.imread('beach.jpg')

# Check if images are loaded successfully
if img1 is None:
    print("Error: Could not load 'lambo.jpg'")
    exit()
if img2 is None:
    print("Error: Could not load 'niceview.jpg'")
    exit()

# Get dimensions of first image
height, width = img1.shape[:2]

# Resize second image to match first image dimensions
img2 = cv.resize(img2, (width, height))

# ii. Ask user for alpha value between 0 and 1
alpha = float(input("Enter a blending value between 0 and 1: "))

# Ensure alpha is between 0 and 1
alpha = max(0, min(1, alpha))

# iii. Implement linear blend
# blend = (1 - alpha) * img1 + alpha * img2
blended = cv.addWeighted(img1, 1 - alpha, img2, alpha, 0)

# Display original and blended images
cv.imshow('Image 1', img1)
cv.imshow('Image 2', img2)
cv.imshow('Blended Image', blended)

cv.waitKey(0)
cv.destroyAllWindows()
