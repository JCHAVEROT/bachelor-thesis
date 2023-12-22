"""
Author:      Jérémy Chaverot
Date:        November 20, 2023
Description: Transform every images of a folder into .jpg format.
"""

import os
import sys
from PIL import Image

def transform_image(image_path):
    img = Image.open(image_path)
    new_image_path = image_path.split('.')[0] + '.jpg'
    img.save(new_image_path)


if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python png_to_jpg.py </path/to/your/images>")
        sys.exit(1)

    # Get arguments from the command line
    folder_path = sys.argv[1]

    # Get a list of all files in the folder
    all_files = os.listdir(folder_path)
    
    # Filter the list to include only image files (you can add more extensions if needed)
    image_files = [file for file in all_files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')) and not file.startswith('._')]
    
    # Get the number of images in the folder
    num_images = len(image_files)

    # Iterate through each image and apply the transformation
    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        transform_image(image_path)
        os.remove(image_path)

    print(f"Number of images transformed into .jpg: {num_images}")
