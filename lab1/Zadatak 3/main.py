import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("primer.png", cv2.IMREAD_GRAYSCALE)

img_fft = np.fft.fftshift(np.fft.fft2(img))

amp = np.abs(img_fft) + 1e-12
faza = np.angle(img_fft)

novi_spektar = np.exp(faza + 1j * np.log(amp))
rezultat = np.real(np.fft.ifft2(np.fft.ifftshift(novi_spektar)))

plt.imshow(img, cmap="gray")
plt.axis("off")
plt.show()

vmin, vmax = np.percentile(rezultat, [1, 99])
plt.imshow(rezultat, cmap="gray", vmin=vmin, vmax=vmax)
plt.axis("off")
plt.imsave("rezultat.png", rezultat, cmap="gray", vmin=vmin, vmax=vmax)
plt.show()