#<!---------------------------------------------------------------------------->
#<!--                  IFSP - Instituto Federal de São Paulo                 -->
#<!--                       Tópicos Avançados (TPA A6)                       -->
#<!-- File       : Ex101_color_spaces.py                                     -->
#<!-- Description: Script to convert the input images in two different       -->
#<!--            : color spaces (RGB and HSV)                                -->
#<!-- Author     : Fabricio Batista Narcizo (narcizo[at]itu[dot]dk)          -->
#<!-- Information: No additional information                                 -->
#<!-- Date       : 10/10/2021                                                -->
#<!-- Change     : 10/10/2021 - Creation of this script                      -->
#<!-- Review     : 10/10/2021 - Finalized                                    -->
#<!---------------------------------------------------------------------------->

__version__ = "$Revision: 2021101001 $"

################################################################################
import numpy as np
import argparse
import cv2

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

################################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="./inputs/lena.jpg", type=str,
                required=False, help="Path to the image.")
args = vars(ap.parse_args())

# Create the Matplotlib window.
fig = plt.figure()

# Hint: You can find more information about opening, converting and showing
#       images using OpenCV on official OpenCV docs (http://docs.opencv.org)

# TODO: Implement your solution here.
img = cv2.imread(args['image'])

img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

img_0 = np.zeros((img.shape[0], img.shape[1]), np.uint8)

[blue, green, red] = cv2.split(img)

img_blue = cv2.merge([blue, img_0, img_0])
img_green = cv2.merge([img_0, green, img_0])
img_red = cv2.merge([img_0, img_0, red])

# Show the final image.
# plt.show(img) final sugerido pelo professor
cv2.imshow("Original Image", img) 
cv2.waitKey(0)

cv2.imshow("HSV Image", img_hsv) 
cv2.waitKey(0)

cv2.imshow("Red Image", img_red) 
cv2.waitKey(0)

cv2.imshow("Green Image", img_green) 
cv2.waitKey(0)

cv2.imshow("Blue Image", img_blue) 
cv2.waitKey(0)