import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktarma
img = cv2.imread("image.jpeg")
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("original img")

#erozyon
kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations = 2)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("erozyon")

#genişleme dilation
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişleme")

#white noise 
whiteNoise = np.random.randint(0,2, size = img.shape[:3])
whiteNoise = whiteNoise*255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("white noise")

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Img w white noise")

#açılma
opening = cv2.morphologyEx(noise_img.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("acilma")

#black noise 
blackNoise = np.random.randint(0, 2, size = img.shape[:3])
blackNoise = blackNoise*255
plt.figure(), plt.imshow(blackNoise, cmap = "gray"), plt.axis("off"), plt.title("black noise")

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0
plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("blak noise img")

#kapatma
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("kapanma")

#gradient
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADI5ENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("gradyan")


















