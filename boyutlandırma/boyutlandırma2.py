import cv2
#fotoyu içe aktarma
img = cv2.imread("foto.jpg", 0) #0 siyah beyaz yapıyor
print("Resim Boyutu: ", img.shape)
cv2.imshow("orijinal", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

#resized
imgResized = cv2.resize(img, (800,800))
print("Resized Img Shape: ", imgResized.shape)
cv2.imshow("Img Resized", imgResized)

#kırpma
imgCropped = img[:200,300] #width height -> height width
cv2.imshow("Kirpik Resim", imgCropped)



