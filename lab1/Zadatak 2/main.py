import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("primer.png", cv2.IMREAD_GRAYSCALE)

# Gausov kernel iste velicine kao slika
h, w = img.shape
kernel = cv2.getGaussianKernel(h, 10) @ cv2.getGaussianKernel(w, 10).T

img_fft = np.fft.fft2(img)
kernel_fft = np.fft.fft2(np.fft.ifftshift(kernel))

# mnozenje u frekvenciji = konvolucija
rezultat = np.abs(np.fft.ifft2(img_fft * kernel_fft))

plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

plt.imshow(rezultat, cmap="gray")
plt.axis("off")
plt.savefig("rezultat.png", dpi=70)
plt.show()