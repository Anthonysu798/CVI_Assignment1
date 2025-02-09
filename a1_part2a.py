import cv2
import numpy as np

# i. Open a color image and display
image = cv2.imread('lambo.jpg')
cv2.imshow('Original Image', image)

# ii. Increase brightness by adding a constant
brightness = 150
bright_image = np.clip(image + brightness, 0, 255).astype(np.uint8)
cv2.imshow('Increased Brightness', bright_image)

# iii. Change the contrast by multiplying the image by a constant 
contrast = 0.5
contrast_image = np.clip(image * contrast, 0, 255).astype(np.uint8)
cv2.imshow('Changed Contrast', contrast_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
