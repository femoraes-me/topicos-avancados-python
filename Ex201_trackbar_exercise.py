# IMPORTAÇÃO DAS BIBLIOTECAS
import cv2 as cv
import numpy as np

def nothing(x):
    pass

# CRIANDO UMA IMAGEM COM FUNDO PRETO
image = np.zeros((512, 512, 3), np.uint8)

# DEFININDO NOME DA JANELA
cv.namedWindow('teste')

cv.createTrackbar('x', 'teste', 0, 100, nothing)
cv.createTrackbar('y', 'teste', 0, 100, nothing)
cv.createTrackbar('r', 'teste', 0, 100, nothing)

while(1): 

    # CRIAÇÃO DO RETANGULO
    image_copy = image.copy()    
    x = cv.getTrackbarPos('x','teste')
    y = cv.getTrackbarPos('y','teste')
    cv.rectangle(image_copy, ((128 - x), (128 - y)), ((384 + x), (384 + y)), (0, 255, 0))
    cv.imshow("teste", image)

    # CALCULO DA AREA DO RETANGULO
    b = 256 + (2 * x)
    h = 256 + (2 * y)
    area = b * h
    text = str(area)
    cv.imshow("teste", image_copy)
    image_copy2 = image_copy.copy()
    cv.putText(image_copy2, text, (10, 25), cv.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 255))
    cv.imshow("teste", image_copy2)

    # CRIANDO O CIRCULO
    image_copy3 = image_copy2.copy()
    r = cv.getTrackbarPos('r','teste')    
    cv.circle(image_copy3, (256, 256), (10 + r), (0, 0, 255), -1)
    cv.imshow("teste", image_copy3)

    #CALCULO DA AREA DO CIRCULO
    image_copy4 = image_copy3.copy()
    area_circ = 3.14 * ( (r + 10) ** 2)
    text_circ = str(area_circ)
    cv.putText(image_copy4, text_circ, (10, 507), cv.FONT_HERSHEY_SIMPLEX, 0.99, (255, 255, 255))
    cv.imshow("teste", image_copy4)

    # CRIANDO AS LINHAS DIAGONAIS
    image_copy5 = image_copy4.copy()
    cv.line(image_copy5, ((128 - x),(128 - y)), ((384 + x), (384 + y)), (0, 255, 255))
    cv.line(image_copy5, ((128 - x), (384 + y)), ((384 + x), (128 - y)), (255, 255, 0))
    cv.imshow("teste", image_copy5)

    cv.waitKey(1)

cv.destroyAllWindows()

# CRIANDO AS TRACKBARS
# cv.createTrackbar('x1', 'teste', 0, 200, nothing)
# cv.createTrackbar('y1', 'teste', 0, 200, nothing)
# cv.createTrackbar('x2', 'teste', 300, 512, nothing)
# cv.createTrackbar('y2', 'teste', 300, 512, nothing)

# LAÇO PARA EXIBIÇÃO E ALTERAÇÃO DO RETANGULO
# while(1):    

#     image_copy = image.copy()
    
#     # x1 = cv.getTrackbarPos('x1','teste')
#     # y1 = cv.getTrackbarPos('y1','teste')
#     # x2 = cv.getTrackbarPos('x2','teste')
#     # y2 = cv.getTrackbarPos('y2','teste')

#     cv.rectangle(image_copy, 200, 200, (0, 255, 255))

#     cv.imshow("teste", image)
#     cv.imshow("teste", image_copy)

#     cv.waitKey(1)

# cv.destroyAllWindows()