"""
Author:      Jérémy Chaverot
Date:        January 01, 2024
Description: Invert the masks in a given folder.
"""

import cv2
import os
import sys

def inverse_masks_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") and not filename.startswith('._'):
            mask_path = os.path.join(folder_path, filename)
            try:
                # Read the mask image
                mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
                if mask is None:
                    print(f"Failed to read image: {mask_path}")
                    continue

                # Invert the mask
                inverted_mask = cv2.bitwise_not(mask)

                # Save the inverted mask with a temporary name
                temp_path = os.path.join(folder_path, "temp_" + filename)
                cv2.imwrite(temp_path, inverted_mask)

                # Delete the original mask
                os.remove(mask_path)

                # Rename the inverted mask to the original filename
                os.rename(temp_path, mask_path)
                print(f"Inverted and replaced mask for: {mask_path}")
            except Exception as e:
                print(f"Error processing {mask_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    inverse_masks_in_folder(folder_path)
