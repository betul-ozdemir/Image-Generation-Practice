import cv2
import matplotlib.pyplot as plt 
import numpy as np
import warnings
warnings.filterwarnings("ignore")

#bluring(detayı azaltır, gürültüyü engeller )
img = cv2.imread("resim.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #bunu yapıyoruz çünkü opencv de difflt olarak BGR var
plt.figure()
plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show() 

"""

ortalama bulanıklaştırma yöntemi

"""
dst2 = cv2.blur(img, ksize = (3,3))
plt.figure(), plt.imshow(dst2), plt.axis("off"), plt.title("ortalama blur")

"""

gaussian blur

"""
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX=7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("Gauss Blur")

"""
medyan blur

"""
mb = cv2.medianBlur(img, ksize = 3)
plt.figure(), plt.imshow(mb), plt.axis("off"), plt.title("Medyan Blur")

#gürültü oluşturma
def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy

#içe aktar ve normalize et
img = cv2.imread("resim.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("original"),plt.show()

gaussianNoisyImage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoisyImage), plt.axis("off"),plt.title("gauss noisy"),plt.show()

 # gauss blur
gb2 = cv2.GaussianBlur(gaussianNoisyImage, ksize = (3,3), sigmaX = 7)
plt.figure(), plt.imshow(gb), plt.axis("off"), plt.title("with Gauss blur")

def saltPepperNoise(image):
    
    row, col, ch = image.shape
    s_vs_p = 0.5
    
    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1
    
    #pepper siyah
    num_pepper = np.ceil(amount * image.size * 1 - s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
plt.figure(), plt.imshow(spImage), plt.axis("off"), plt.title("SP Image")

mb2 = cv2.medianBlur(spImage.astype(np.float), ksize = 3)
plt.figure(), plt.imshow(mb2), plt.axis("off"), plt.title("with median  blur")



















