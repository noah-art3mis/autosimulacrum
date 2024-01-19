import time
import os


def count_time(start_time: float, task_name : str) -> None: 
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{task_name}: {elapsed_time:.2f} seconds")

def get_data_folders(folder_path) -> []:
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        folder_names = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f))]

        return folder_names

    except Exception as e:
        print(f"Error: {e}")
        
         
def get_file_names_in_folder(folder_path) -> []:
    try:
        if not os.path.exists(folder_path):
            raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")

        file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

        return file_names

    except Exception as e:
        print(f"Error: {e}")