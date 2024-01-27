# 20.11.2023 to 27.11.2023

## What was done

- Figure out how the model was loding data when not using COLMAP with the file eval.py (MOSTLY SAME AS LAST WEEKS).
- Script to read .npy files, and .pkl files.

## What is to be done

- Better understand each dependencies, files format, what happens on load.
- Mimic the LINEMOD data file organization, and adapt the code in consequence.


## Questions to ask

- What is the K-matrix ? Answer : the intrinsic matrix. Can be obtained by asking the students working on the dataset.
- What is the format of the pose ? Answer : Our format is the quaternions and the 3 coordinates. Theirs the rotation matrix concatenated with the translation vector.


Response:
K matrix: intrinsic matrix
Pose matrix: Rotational matrix and translation vector combined