"""
Author:      Jérémy Chaverot
Date:        November 20, 2023
Description: Read the info from a .npy file.
"""

import numpy as np
import sys

def read_npy(file_name):
    data = np.load(file_name)
    print(data)

if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python read_npy.py <file_name>")
        sys.exit(1)

    # Get arguments from the command line
    arg1 = sys.argv[1]

    # Call the function with the provided arguments
    read_npy(arg1)