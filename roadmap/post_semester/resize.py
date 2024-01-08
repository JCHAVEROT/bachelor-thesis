"""
Author:      Jérémy Chaverot
Date:        January 01, 2024
Description: Resize the images from a given folder.
"""

import os
import sys
from PIL import Image

def resize_images(folder_path, resize_factor):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") and not filename.startswith('._'):
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:
                # Calculate new size
                new_size = tuple([int(dim / resize_factor) for dim in img.size])
                # Resize the image
                resized_img = img.resize(new_size, Image.ANTIALIAS)
                # Save the resized image with a different name temporarily
                temp_path = os.path.join(folder_path, "temp_" + filename)
                resized_img.save(temp_path)

            # Delete the original image
            os.remove(img_path)

            # Rename the resized image to the original filename
            os.rename(temp_path, img_path)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: resize.py <folder_path> <resize_factor>")
        sys.exit(1)

    folder_path = sys.argv[1]
    factor = int(sys.argv[2])

    resize_images(folder_path, factor)

