import os

def rename_and_delete_images(folder_path):
    # List all files in the folder
    files = sorted([f for f in os.listdir(folder_path) if f.endswith('.npy') and not f.startswith('._')])

    # Pad the index with zeros up to 4 digits, rename files, and then delete the old ones
    for index, file in enumerate(files):
        new_filename = f"pose{str(index)}.npy"
        old_file_path = os.path.join(folder_path, file)
        new_file_path = os.path.join(folder_path, new_filename)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        #print(f"Renamed {file} to {new_filename}")


# Update this path to the folder containing your .jpg images
folder_path = r"F:\bachelor-thesis\Gen6D\data\SpaceCraft\jwst-ref\pose"
rename_and_delete_images(folder_path)

