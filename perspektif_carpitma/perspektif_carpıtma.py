import cv2
import numpy as np

#içe aktarma
img = cv2.imread("kart.png")
cv2.imshow("orijinal", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

width = 400
height = 500

pts1 = np.float32([[434,26],[117,276],[597,199],[278,467]]) #orjinal resimde resmin köşeleri
pts2 = np.float32([[0,0],[0, height], [width, 0],[width,height]]) #yeni oluşacak düz resmin doğru köşeleri

#perspektif transform matrisi
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#çevirme işlemi
imgOutput = cv2.warpPerspective(img, matrix, (width,height))
cv2.imshow("donusturulmus", imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()
