import os
from typing import List


def get_data_folders(folder_path) -> List[str]:
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        folder_names = [
            f
            for f in os.listdir(folder_path)
            if os.path.isdir(os.path.join(folder_path, f))
        ]

        return folder_names

    except Exception as e:
        print(f"Error: {e}")
        raise


def get_file_names_in_folder(folder_path) -> List[str]:
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

    file_names = [
        f
        for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    return file_names
