#<!---------------------------------------------------------------------------->
#<!--                  IFSP - Instituto Federal de São Paulo                 -->
#<!--                       Tópicos Avançados (TPA A6)                       -->
#<!-- File       : Ex301_histogram.py                                        -->
#<!-- Description: Script to represent the pixel distribution function based -->
#<!--            : on each grayscale level of an input image                 -->
#<!-- Author     : Fabricio Batista Narcizo (narcizo[at]itu[dot]dk)          -->
#<!-- Information: No additional information                                 -->
#<!-- Date       : 16/11/2021                                                -->
#<!-- Change     : 16/11/2021 - Creation of this script                      -->
#<!-- Review     : 16/11/2021 - Finalized                                    -->
#<!---------------------------------------------------------------------------->

__version__ = "$Revision: 2021111601 $"

################################################################################
import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np

################################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=False, help="Path to the image")
args = vars(ap.parse_args())

# Get the input filename
filename = "./inputs/lena.jpg" if args["image"] is None else args["image"]

# Loads a grayscale image from a file passed as argument.
image = cv2.imread(filename, cv2.IMREAD_COLOR)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
image_shuffle = image_gray.copy()
np.random.shuffle(image_shuffle);

# Create the Matplotlib figures.
fig_imgs = plt.figure("Images")
fig_hist = plt.figure("Histograms")

# This function creates a Matplotlib window and shows four images.
def showImage(image, pos, title="Image", isGray=False):
    sub = fig_imgs.add_subplot(2, 2, pos)
    sub.set_title(title)
    if isGray:
        sub.imshow(image, cmap="gray")
    else:
        sub.imshow(image)
    sub.axis("off")

# This function creates a Matplotlib window and shows four histograms.
def showHistogram(histogram, pos, title="Histogram", color="blue"):
  sub = fig_hist.add_subplot(2, 2, pos)
  sub.set_title(title)
  plt.xlabel("Bins")
  plt.ylabel("Number of Pixels")
  plt.xlim([0, 256])
  plt.plot(histogram, color=color)

# TODO: You code here
# GRAYSCALE
showImage(image_gray, 1, title="GrayScale", isGray=True)
hist = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
showHistogram(hist, 1, "GrayScale", color="blue")

# SHUFFLE
showImage(image_shuffle, 2, title="Shuffled", isGray=True)
hist = cv2.calcHist([image_shuffle], [0], None, [256], [0, 256])
showHistogram(hist, 2, "Shuffled", color="green")

# RGB 
showImage(image_rgb, 3, "RGB")
colors = ('r', 'g', 'b')
hist = {}
for i, col in enumerate(colors):
  hist[i] = cv2.calcHist([image_rgb], [i], None, [256], [1, 256])
ahist = np.array((*hist[0], *hist[1], *hist[2]), dtype=np.uint8)
showHistogram(ahist, 3, "RGB", color="red")

# HSV 
showImage(image_hsv, 4, "HSV")
colors = ('r', 'g', 'b')
hist = {}
for i, col in enumerate(colors):
  hist[i] = cv2.calcHist([image_hsv], [i], None, [256], [1, 256])
ahist = np.array((*hist[0], *hist[1], *hist[2]), dtype=np.uint8)
showHistogram(ahist, 4, "HSV", color="yellow")

# Show the Matplotlib windows.
plt.show()

