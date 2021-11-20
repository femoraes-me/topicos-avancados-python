# IMPORTAÇÃO DAS BIBLIOTECAS
import cv2 as cv
import numpy as np

# CRIANDO UMA IMAGEM COM FUNDO PRETO
image = np.zeros((512, 512, 3), np.uint8)

### ELIPSE & CIRCULO ###
#for i in range(0, 361, 30):
    #cv.ellipse(image, (256, 256), (128, 64), i, 0, 360, (255, 255, 255))
    #cv.circle(image, (256, 256), 16, (0, 0, 255), -1)

### RETANGULO ###
#cv.rectangle(image, (128, 128), (384, 384), (0, 255, 255))
#cv.rectangle(image, (128, 192), (384, 320), (0, 255, 255), -1)

### LINHAS ###
# for i in range(32, 512, 32):
#     cv.line(image, (0, i), (512, i), (0, 0, 255))
#     cv.line(image, (i, 0), (i, 512), (0, 0, 255))

### TEXTOS ###
# text = "Felipe Soares Pinto de Moraes"
# cv.putText(image, text, (10, 100), cv.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 255))

### SUB-IMAGEM
# filename = "./inputs/lena.jpg"
# image = cv.imread(filename)
# image = image[:200, :300]
# image = image[200:, 300:]
# image = image[128:384, 128:-128]

### REDIMENSIONAMENTO DE IMAGEM
filename = "./inputs/lena.jpg"
image = cv.imread(filename)
#image = cv.resize(image, (32, 32))
#image = cv.resize(image, (0, 0), fx=3, fy=3)


# EXIBINDO A IMAGEM
cv.imshow("image", image)

# DEFININDO TOQUE DE TECLA PARA FECHAR
cv.waitKey(0)