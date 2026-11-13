import cv2
import numpy as np
import matplotlib.pyplot as plt

def frekventni_dom(img):
    img_fft = np.fft.fft2(img)
    img_fft = np.fft.fftshift(img_fft)
    return img_fft

def prostorni_iz_fft(magnitude_log, complex_moduo_1):
    img_fft = complex_moduo_1 * np.exp(magnitude_log)
    return np.abs(np.fft.ifft2(img_fft))

img = cv2.imread("primer.png", cv2.IMREAD_GRAYSCALE)
fft = frekventni_dom(img)

amplituda_log = np.log1p(np.abs(fft))
faza = np.angle(fft)

# zamena
rezultat = prostorni_iz_fft(faza, np.exp(1j * amplituda_log))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Originalna slika")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(np.log(rezultat + 1e-12), cmap="gray")   # log jer je opseg velik
plt.title("Zamenjena amplituda i faza")
plt.axis("off")
plt.savefig("rez.png", dpi=70)
plt.show()