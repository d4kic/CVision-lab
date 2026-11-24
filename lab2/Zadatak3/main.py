import cv2
import numpy as np
import matplotlib.pyplot as plt

def morfoloska_rekonstrukcija(marker, maska):
    kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    pret_marker = np.zeros_like(marker)
    tren_marker = marker.copy()
    while not np.array_equal(tren_marker, pret_marker):
        pret_marker = tren_marker.copy()
        tren_marker = cv2.dilate(tren_marker, kernel3)
        tren_marker = cv2.min(tren_marker, maska)
    return tren_marker


slika = cv2.imread("nebo.png")

# segmentacija svih zvezda pomocu top-hat operacije
slika_gray = cv2.cvtColor(slika, cv2.COLOR_BGR2GRAY)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
tophat = cv2.morphologyEx(slika_gray, cv2.MORPH_TOPHAT, kernel)
_, sve_zvezde = cv2.threshold(tophat, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

hsv_slika = cv2.cvtColor(slika, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv_slika)

# zasiceni pikseli unutar zvezda predstavljaju zute zvezde
_, zasiceno = cv2.threshold(s, 80, 255, cv2.THRESH_BINARY)
zuti_marker = cv2.bitwise_and(zasiceno, sve_zvezde)

# morfoloska rekonstrukcija: marker raste unutar maske svih zvezda
zute_zvezde = morfoloska_rekonstrukcija(zuti_marker, sve_zvezde)

# oduzimanje zutih zvezda
bele_zvezde = cv2.subtract(sve_zvezde, zute_zvezde)
cv2.imwrite("maska_belih_zvezda.png", bele_zvezde)

plt.figure(figsize=(10, 10))
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.imshow(bele_zvezde, cmap="gray")
plt.axis("off")
plt.show()