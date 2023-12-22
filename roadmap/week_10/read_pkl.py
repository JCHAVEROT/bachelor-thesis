"""
Author:      Jérémy Chaverot
Date:        November 20, 2023
Description: Read the info from a .pkl file.
"""

import pickle
import sys

def read_pkl(file_name):
    with open(file_name, 'rb') as f:
        data = pickle.load(f)
        print(data)

if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python read_pkl.py <file_name>")
        sys.exit(1)

    # Get arguments from the command line
    arg1 = sys.argv[1]

    # Call the function with the provided arguments
    read_pkl(arg1)