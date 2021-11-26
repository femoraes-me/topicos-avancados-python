#<!---------------------------------------------------------------------------->
#<!--                  IFSP - Instituto Federal de São Paulo                 -->
#<!--                       Tópicos Avançados (TPA A6)                       -->
#<!-- File       : Ex102_video_stream.py                                     -->
#<!-- Description: Script to convert the video stream in two different       -->
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

################################################################################
# Construct the argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", default="./inputs/PPAP.mp4", type=str,
                required=False, help="Video capture device ID or file path.")
args = vars(ap.parse_args())

# Hint: You can find more information about opening, converting and showing
#       images using OpenCV on official OpenCV docs (http://docs.opencv.org)

# TODO: Implement your solution here.
video = cv2.VideoCapture(args["video"])

while True:

    ret, frame = video.read()

    if not ret:
        break

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    bit_0 = np.zeros((frame.shape[0], frame.shape[1]), np.uint8)

    [blue, green, red] = cv2.split(frame)

    frame_blue = cv2.merge([blue, bit_0, bit_0])
    frame_green = cv2.merge([bit_0, green, bit_0])
    frame_red = cv2.merge([bit_0, bit_0, red])

    #cv2.imshow("Video", frame) 
    #cv2.imshow("Video", frame_hsv) 
    #cv2.imshow("Video", frame_blue) 
    #cv2.imshow("Video", frame_green) 
    cv2.imshow("Video", frame_red) 
    
    stop = cv2.waitKey(1)

    if stop == ord("p"): #aperte a tecla p para parar o video
        break

