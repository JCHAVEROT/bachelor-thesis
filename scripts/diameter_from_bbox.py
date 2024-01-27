"""
Author:      Jérémy Chaverot
Date:        November 29, 2023
Description: Compute the diameter of a space object from its bounding box.
"""

import numpy as np
import sys
from utils.dataset_constants import object_bounding_boxes


def get_diameter(id):
    bbox = object_bounding_boxes[id]
    diameter = np.linalg.norm(bbox[0] - bbox[1])
    return diameter


if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python diameter_from_bbox.py <object_id>")
        sys.exit(1)

    # Get arguments from the command line
    arg1 = sys.argv[1]

    # Call the function with the provided arguments
    print(get_diameter(arg1))