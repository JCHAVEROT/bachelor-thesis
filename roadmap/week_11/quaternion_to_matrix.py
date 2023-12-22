"""
Author:      Jérémy Chaverot
Date:        November 20, 2023
Description: Transform a .txt file with quaternions and the translation vector into multiple .npy files containing the
             rotation matrix augmented with the translation vector.
"""

import numpy as np
import sys
import os


def quaternion_to_matrix(Q, translation):
    """
        Covert a quaternion and translation into a full three-dimensional augmented rotation matrix.

        Input
        :param Q: A 4 element array representing the quaternion (qw, qx, qy, qz).
        :param translation: A 3 element array representing the translation (x, y, z).

        Output
        :return: A 3x4 element matrix representing the full 3D rotation matrix with
                 translation. This rotation matrix converts a point in the local
                 reference frame to a point in the global reference frame.
    """

    # Extract the values from Q
    qw = Q[0]
    qx = Q[1]
    qy = Q[2]
    qz = Q[3]

    # Extract the values from the translation vector
    x = translation[0]
    y = translation[1]
    z = translation[2]

    # First row of the rotation matrix
    r00 = 2 * (qw * qw + qx * qx) - 1
    r01 = 2 * (qx * qy - qw * qz)
    r02 = 2 * (qx * qz + qw * qy)

    # Second row of the rotation matrix
    r10 = 2 * (qx * qy + qw * qz)
    r11 = 2 * (qw * qw + qy * qy) - 1
    r12 = 2 * (qy * qz - qw * qx)

    # Third row of the rotation matrix
    r20 = 2 * (qx * qz - qw * qy)
    r21 = 2 * (qy * qz + qw * qx)
    r22 = 2 * (qw * qw + qz * qz) - 1

    # 3x3 rotation matrix
    rot_matrix_augm = np.array([[r00, r01, r02, x],
                                [r10, r11, r12, y],
                                [r20, r21, r22, z]])

    return rot_matrix_augm


if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python quaternion_to_matrix.py </path/to/your/text/file> </path/to/the/pose/folder>")
        sys.exit(1)

    # Get arguments from the command line
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
    
    # Iterate through each pose and apply the transformation
    for pose in poses:
        image_id, obj_id, qw, qx, qy, qz, x, y, z = pose.split(',')
        Q = np.array([qw, qx, qy, qz], dtype=np.float32)
        translation = np.array([x, y, z], dtype=np.float32)
        matrix = quaternion_to_matrix(Q, translation)
        np.save(pose_folder_path + '/pose' + str(int(image_id)), matrix)


    print(f"Number of transformation processed: {len(poses)}")