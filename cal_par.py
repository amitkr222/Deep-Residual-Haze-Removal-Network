import cv2
import numpy as np
import math

img1 = cv2.imread(r"C:\Users\Amitk\Downloads\DRHnet\code\GroundTruth\53_GT.png")
#cv2.imshow('Image 1', img1)

img2 = cv2.imread(r"C:\Users\Amitk\Downloads\DRHnet\code\output\dehaze_outdoor_53_hazy.png")
#cv2.imshow('Image 2', img2)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Calculate the PSNR between the two images
def calculate_psnr(img1, img2):
    # img1 and img2 have range [0, 255]
    img1 = img1.astype(np.float64)
    img2 = img2.astype(np.float64)
    mse = np.mean((img1 - img2)**2)
    if mse == 0:
        return float('inf')
    return 20 * math.log10(255.0 / math.sqrt(mse))

psnr_val = calculate_psnr(img1, img2)
print("PSNR Value is:",psnr_val)


