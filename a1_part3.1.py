#We, Anthony Su and Yingyong L. (mention assigned group number and your names), declare that the attached assignment is our own work in accordance with the Seneca Academic Policy.  We have not copied any part of this assignment, manually or electronically, from any other source including web sites, unless specified as references. We have not distributed our work to other students.

import cv2 as cv

# Read the image
img = cv.imread('lambo.jpg')

# Draw a green rectangle
# Parameters: image, start_point, end_point, color (BGR format), thickness
cv.rectangle(img, (100, 100), (500, 400), (0, 255, 0), thickness=4)

# Display the image
cv.imshow("Sports Car", img)

cv.waitKey(0)

