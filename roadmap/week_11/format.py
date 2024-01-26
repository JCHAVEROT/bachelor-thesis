"""
Author:      Jeremy Chaverot
Date:        November 29, 2023
Description: Create the files val.txt, train.txt and test.txt according to a test percentage.
"""

import os
import sys
import random


if __name__ == "__main__":

	# Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python format.py <object_name> <test_percentage>")
        sys.exit(1)

    object = sys.argv[1]
    test_percentage = float(sys.argv[2])

    if (test_percentage < 0 or 1 < test_percentage):
        print("Wrong value for the variable <test_percentage>. Should be between 0 and 1 included.")
        sys.exit(1)

    # List of files in the given folder
    all_files = os.listdir(f'data/SpaceCraft/{object}/images')

    # Filter the list to select only images and exclude MacOS temporary files
    image_files = [file for file in all_files if file.lower().endswith(('.jpg')) and not file.startswith('._')]

    num_images = len(image_files)

    # Transform each image
    with open(f'data/SpaceCraft/{object}/train.txt', 'w') as train, open(f'data/SpaceCraft/{object}/test.txt', 'w') as test:
        for image_file in image_files:
            rand = random.random()
            image_path = 'SpaceCraft/hubble/images/' + image_file
            if (rand < test_percentage):
                test.write(image_path + '\n')
            else: train.write(image_path + '\n')

    print(f"Done splitting {num_images} images in train.txt and test.txt")