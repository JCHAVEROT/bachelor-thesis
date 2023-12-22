# 04.11.2023 to 11.12.2023

## What was done

- Modified file database.py again.

## What is to be done

- Fix the bugs in the code to make the pose estimation more accurate.


## Questions to ask

- If we want to retrain the model, we need to fix the inverted masks first.

Fig. 1. Given (a) reference images of an object with known poses and (b) query images containing the same object with unknown poses, our pose estimator is able to accurately estimate (c) their object poses in the query images, where green color means ground- truth and blue color means estimation. Note that all objects are unseen in the training set and the same estimator is applied for all objects.

- In Gen6D the camera should be moving, not the object, is that a problem ?

- A metric to compare the estimated pose to the ground truth one with a percentage of error ?

- As the object can be seen from really any viewpoint since moving in space, and because of the special light conditions, does it imply we need a lot more references images ?

- Images where the object is centered and not too far ?