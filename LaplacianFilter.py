import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
import random
# -1, cv2.IMREAD_COLOR : Loads a color image. Any transparency of image
# 0, cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
# 1, cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
ddepth = cv2.CV_16S
kernel_size = 3

# Choose file to apply the filter
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Image File", '.jpg .jpeg')])
print(file_path)

img = cv2.imread(file_path, -1)

if img is None:
    print ('Error opening image')

blurredImage = img.copy()

# Reduce noise
blurredImage = cv2.GaussianBlur(img, (3, 3), 0)  

filteredImageGray = cv2.cvtColor(blurredImage, cv2.COLOR_BGR2GRAY)

# Apply Laplacian filter to detect edges
laplacian = cv2.Laplacian(filteredImageGray, ddepth, ksize=kernel_size)
abs_laplacian = cv2.convertScaleAbs(laplacian)


# Loop through the image
# for i in range(height):
#     for j in range(width):
#         if(filteredImage[i][j] < 200):
#             if (filteredImage[i][j] > 32):
#                 filteredImage[i][j] -= random.randint(16, 32)
#             else:
#                 filteredImage[i][j] += random.randint(16, 32)
        # else:
        #     filteredImage[i][j] = random.randint(240, 255)

# head = img[300:600, 300:600]
# img[0:300, 0:300] = head

# img [5:305, 5:405] = head
# img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE

# print(img)    
# cv2.imwrite('./assets/new_cat.jpg', img)

abs_laplacian_color = cv2.merge([abs_laplacian] * 3)


horizontal_imgs = np.concatenate((img, blurredImage, abs_laplacian_color), axis=1)
resized_imgs = cv2.resize(horizontal_imgs, (0, 0), fx=0.7, fy= 0.7)
cv2.imshow("Filter tests", resized_imgs)
# cv2.imshow("Laplace Filtered Image", abs_dst)
# cv2.imshow('Cat image filtered', filteredImage)
# cv2.imshow('Cat image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
