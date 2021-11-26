#<!---------------------------------------------------------------------------->
#<!--                  IFSP - Instituto Federal de São Paulo                 -->
#<!--                       Tópicos Avançados (TPA A6)                       -->
#<!-- File       : Ex202_image_transformation.py                             -->
#<!-- Description: Script to apply geometric transformations (rotation,      -->
#<!--            : scale and translation) in image sequences                 -->
#<!-- Author     : Fabricio Batista Narcizo (narcizo[at]itu[dot]dk)          -->
#<!-- Information: No additional information                                 -->
#<!-- Date       : 27/10/2021                                                -->
#<!-- Change     : 27/10/2021 - Creation of this script                      -->
#<!-- Review     : 27/10/2021 - Finalized                                    -->
#<!---------------------------------------------------------------------------->

__version__ = "$Revision: 2021102701 $"

################################################################################
import cv2 as cv
import math
import argparse
import numpy as np

def nothing(x):
    pass

########################################################################
def affineTransformation(image, theta=0, t=(0, 0), s=1.):
    pass

# TODO: Your code here

# FAZENDO LEITURA DO VIDEO
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", default="./inputs/PPAP.mp4", type=str,
                required=False, help="Video capture device ID or file path.")
args = vars(ap.parse_args())
video = cv.VideoCapture(args["video"])


image = np.zeros((1280, 720, 3), np.uint8)

# DEFININDO NOME DA JANELA
cv.namedWindow('transformations')

# CRIANDO AS TRACKBARS
cv.createTrackbar('r' , 'transformations', 0, 360, nothing)
cv.createTrackbar('s' , 'transformations', 1, 10, nothing)
cv.createTrackbar('tx', 'transformations', 0, 480, nothing)
cv.createTrackbar('ty', 'transformations', 0, 400, nothing)

while(1):
    ret, frame = video.read()

    if (not ret):
        break

    altura, largura = frame.shape[:2]

    centroy = altura//2
    centrox = largura//2

    # TRANSLATION
    M = np.float32([[1,0,cv.getTrackbarPos('tx', 'transformations')],[0,1,cv.getTrackbarPos('ty', 'transformations')]])
    frame_t = cv.warpAffine(frame,M,(largura,altura))

    # ROTAÇÃO
    angulo_rotacao = cv.getTrackbarPos('r', 'transformations')
    M = cv.getRotationMatrix2D((centrox, centroy), angulo_rotacao, cv.getTrackbarPos('s', 'transformations'))
    imagem_rotacionada = cv.warpAffine(frame_t, M, (largura, altura))
      
    # EXIBINDO VIDEO
    resized = cv.resize(frame, (0,0), fx=0.5, fy=0.5)
    resized_editada = cv.resize(imagem_rotacionada, (0,0), fx=0.5, fy=0.5)

    final = cv.hconcat([resized, resized_editada])

    cv.imshow('transformations', final)

    key = cv.waitKey(1) & 0xff
    if(key == 27):
        break 



