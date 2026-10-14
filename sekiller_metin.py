import cv2
import numpy as np

#resim oluştur
img = np.zeros((512,512,3), np.uint8) #siyah bir resim
print(img.shape)

cv2.imshow("Siyah", img)
#PENCERENİN AÇILMASI İÇİN KRİTİK
cv2.waitKey(0)
cv2.destroyAllWindows()

#çizgi
cv2.line(img, (0,0), (512,512), (0,255,0)) #resim, başlangıç noktası, bitiş nokatsı, renk 
#RGB(red green blue) = (255,0,0)-> red (0,255,0)->gren OPENCV DIRALAMAYI BGR OLARAK KABUL EDİYOR!
cv2.imshow("cizgi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#dikdörtgen
#(resim, başlangıç,bitiş,renk )

cv2.rectangle(img, (0,0), (256,256), (255,0,0)) # parantezi kapatmadan önce cv2.FILLED yazars adikdörtgenin içi doldurulmuş olur
cv2.imshow("Dikdortgen" , img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#çember
#(resim,merkez,yarı çap, renk)
cv2.circle(img, (300,300), 45, (0,0,255), cv2.FILLED)
cv2.imshow("cember", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#metin
#(resim, başlangıç noktası, font, kalınlığı, renk )
cv2.putText(img, "Resim", (350,350), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255))
cv2.imshow("Metin", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

 



