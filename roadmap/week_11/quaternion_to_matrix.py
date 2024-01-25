"""
Author:      Jérémy Chaverot
Date:        November 20, 2023
Description: Transform a txt file with quaternions and the translation vector into multiple npy files containing the
             rotation matrix concatenated with the translation vector.
"""

import numpy as np
import sys
import os


def quaternion_to_matrix(Q, translation):
    """
        Covert a quaternion and translation into a full three-dimensional augmented rotation matrix.

        Input
        :param Q: A 4 element array representing the quaternion (q0, q1, q2, q3).
        :param translation: A 3 element array representing the translation (x, y, z).

        Output
        :return: A 3x4 element matrix representing the 3D rotation matrix concatenated with the translation vector.
    """

    # Extract the values from arguments
    q0 = Q[0]
    q1 = Q[1]
    q2 = Q[2]
    q3 = Q[3]

    x = translation[0]
    y = translation[1]
    z = translation[2]

    # Compute the rotation matrix
    r00 = 2 * (q0 * q0 + q1 * q1) - 1
    r01 = 2 * (q1 * q2 - q0 * q3)
    r02 = 2 * (q1 * q3 + q0 * q2)

    r10 = 2 * (q1 * q2 + q0 * q3)
    r11 = 2 * (q0 * q0 + q2 * q2) - 1
    r12 = 2 * (q2 * q3 - q0 * q1)

    r20 = 2 * (q1 * q3 - q0 * q2)
    r21 = 2 * (q2 * q3 + q0 * q1)
    r22 = 2 * (q0 * q0 + q3 * q3) - 1

    # 3x3 rotation matrix concatenated with the 3x1 translation vector
    matrix = np.array([[r00, r01, r02, x],
                       [r10, r11, r12, y],
                       [r20, r21, r22, z]])

    return matrix


if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python quaternion_to_matrix.py </path/to/your/text/file> </path/to/the/pose/folder>")
        sys.exit(1)

    file_path = sys.argv[1]
    pose_folder_path = sys.argv[2]
    file_content = None

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
    except FileNotFoundError:
        print(f"The file {file_path} was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    poses = file_content.split('\n')[:-1]

    # Iterate through each pose, apply the transformation and save it
    for pose in poses:
        image_id, obj_id, q0, q1, q2, q3, x, y, z = pose.split(',')
        Q = np.array([q0, q1, q2, q3], dtype=np.float32)
        translation = np.array([x, y, z], dtype=np.float32)
        matrix = quaternion_to_matrix(Q, translation)
        np.save(pose_folder_path + '/pose' + str(int(image_id)), matrix)

    print(f"Number of transformation processed: {len(poses)}.")
