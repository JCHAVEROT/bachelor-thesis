# 27.11.2023 to 04.12.2023

## What was done

- Figured out how the model was loding data when not using COLMAP with the file eval.py (MOSTLY SAME AS LAST WEEKS).
- Modified files eval.py, database.py, spacecraft\_object\_data\_prepare.py, to\_jpg.py, diameter\_from\_bbox.py, quaternion\_to\_matrix.py
- Create the hubble data file.
- Script to convert the quaternions and the coordinates x, y, z into a rotation matrix augmented by the translation vector, format.py.

## What is to be done

- Better understand each dependencies, files format, what happens on load.
- Mimic the LINEMOD data file organization, and adapt the code in consequence.


## Questions to ask

- Is the mask behing inversed for the spacecraft dataset a problem ?

