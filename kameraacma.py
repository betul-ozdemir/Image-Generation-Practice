import cv2

#capture
cap = cv2.VideoCapture(0) #dışardan harici bir kamera takarsak buraya 0 yazmak zorundayız.

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #Kameranın genişliğini alıp yazdırma
height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #yükseklik
print(width, height)

#video kaydedici başlatma
writer = cv2.VideoWriter("video_kaydı.mp4" , cv2.VideoWriter_fourcc(*"DIVX"),20,(width, height))
#fourcc çerçeveleri sıkıştırmak için kullanılan dört karakterli codec kodu. 20 de video akışının hızı her saniyede göreceğimiz frame sayısı

#video okuyacağız görselleştirip paraelde video kaydına devam edeceğiz
while True:
    ret, frame = cap.read()
    cv2.imshow("Video", frame)
    
    #save
    writer.write(frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break 
cap.release()
writer.release()
cv2.destroyAllWindows()

