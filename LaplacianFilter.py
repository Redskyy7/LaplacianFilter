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

# Read image

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

abs_laplacian_color = cv2.merge([abs_laplacian] * 3)

# Show the images
horizontal_imgs = np.concatenate((img, blurredImage, abs_laplacian_color), axis=1)
resized_imgs = cv2.resize(horizontal_imgs, (0, 0), fx=0.7, fy= 0.7)
cv2.imshow("Filter tests", resized_imgs)

cv2.waitKey(0)
cv2.destroyAllWindows()
