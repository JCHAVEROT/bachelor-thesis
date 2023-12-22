import cv2
import numpy as np

def inverse_mask(mask_path):
    # Read the mask image
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    # Invert the mask
    inverted_mask = cv2.bitwise_not(mask)

    # Save the inverted mask
    cv2.imwrite(mask_path, inverted_mask)

# Example usage
for i in range(400):
    mask_path = f'{int(i):04}.png'
    inverse_mask(mask_path)
