"""
Author:      Jeremy Chaverot
Date:        December 10, 2023
Description: Invert the masks from a given folder.
"""

import cv2
import os
import sys


def inverse_masks_in_folder(folder_path):
	# Iterate through the list of files at the specified path
    for filename in os.listdir(folder_path):
    	# Filter to include only png image files and exclude MacOS temporary files
        if filename.endswith(".png") and not filename.startswith('._'):
            mask_path = os.path.join(folder_path, filename)
            try:

                mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)
                if mask is None:
                    print(f"Failed to read image: {mask_path}")
                    continue
                inverted_mask = cv2.bitwise_not(mask)
                temp_path = os.path.join(folder_path, "temp_" + filename)
                cv2.imwrite(temp_path, inverted_mask)

                # Delete the original wrong mask
                os.remove(mask_path)

                # Rename the inverted mask
                os.rename(temp_path, mask_path)
                print(f"Inverted and replaced mask for: {mask_path}")
            except Exception as e:
                print(f"Error processing {mask_path}: {e}")


if __name__ == "__main__":

	# Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python invert_mask.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    inverse_masks_in_folder(folder_path)