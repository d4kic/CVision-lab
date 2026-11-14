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

img_fft = frekventni_dom(img)

img_fft_mag = np.abs(img_fft) + 1e-12      # 1e-12 da nema deljenja nulom
img_mag_1 = img_fft / img_fft_mag          # faza
img_fft_log = np.log(img_fft_mag)          # log-amplituda

# faza ide na mesto log-amplitude, log-amplituda u ugao
faza = np.angle(img_mag_1)
rezultat = prostorni_iz_fft(faza, np.exp(1j * img_fft_log))

plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

plt.imshow(np.log(rezultat + 1e-12), cmap="gray")
plt.axis("off")
plt.savefig("rezultat.png", dpi=70)
plt.show()