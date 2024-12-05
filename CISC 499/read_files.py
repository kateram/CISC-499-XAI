import os

def read_python_files(folder_name):
    """
    Reads all Python (.py) files and converts their content to strings.

    :param folder_name: Name of the folder containing Python files.
    :return: A dictionary where keys are file names and values are the file contents as strings.
    """
    # Get the folder path relative to the script's location
    script_dir = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(script_dir, folder_name)
    
    file_contents = {}

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            # Open and read the file
            with open(file_path, "r") as file:
                file_contents[filename] = file.read()
        except Exception as e:
            print(f"Error reading {filename}: {e}")

    return file_contents

