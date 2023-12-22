"""
Author:      Jérémy Chaverot
Date:        November 20, 2023
Description: Prepare the data folder of a SpaceCraft dataset object to fit Gen6D requirements.
"""


def main(args):
    



if __name__ == "__main__":

    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python spacecraft_object_data_prepare.py <object_name>")
        sys.exit(1)

    # Get arguments from the command line
    args = sys.argv[1]

    # Call the function with the provided arguments
    read_npy(args)