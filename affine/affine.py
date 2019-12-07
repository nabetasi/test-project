#!/usr/bin/env python

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.png')
rows,cols,ch = img.shape

print("input",rows,cols,ch)

pts1 = np.float32([[0,0],[140,0],[0,70]])
pts2 = np.float32([[70,140],[70,0],[0,140]])

M = cv2.getAffineTransform(pts1,pts2)

dst = cv2.warpAffine(img,M,(rows,cols),flags=cv2.INTER_NEAREST)

for x_pixel in range(cols):
    for y_pixel in range(rows):
        in_pixel_value = img[y_pixel, x_pixel]
        out_pixel_value = dst[cols-x_pixel-1, rows-y_pixel-1]
        if ( in_pixel_value.all() != out_pixel_value.all() ):
            print 'x, y @ in = ' + str(x_pixel) + ', ' + str(y_pixel)
            print 'in_pixel=' + str(in_pixel_value)
            print 'out_pixel=' + str(out_pixel_value)

cv2.imwrite('affine_out.png', dst)


plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
