import cv2
import numpy as np

#Question 1
img1 = cv2.imread("/Users/mariavieira/Desktop/ece140a/Lab3/Tutorials/Tutorial_Pyramid_Basics/public/geisel.jpg", 1)  # Default condition or 1
img1[:, :, 0] = 255 - img1[:, :, 0] # taking the complement of the blue color space

cv2.imshow('Window Name', img1) # Show image
cv2.destroyAllWindows() # Destroy all opened windows


# Question 2
# The Original Dimensions are 476x640 and the new dimensions are 238x640
img2 = cv2.imread("/Users/mariavieira/Desktop/ece140a/Lab3/Tutorials/Tutorial_Pyramid_Basics/public/geisel.jpg", 1)
print('Original Dimensions : ',img2.shape)
width = int(img2.shape[1]) # same original width
height = int(img2.shape[0] * 50 / 100) # half of its original height
dim = (width, height)

# resize image
resized = cv2.resize(img2, dim, interpolation=cv2.INTER_AREA)
print('Resized Dimensions : ', resized.shape)

cv2.imshow("Resized image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()