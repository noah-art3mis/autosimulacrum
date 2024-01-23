import time
import os
import logging
from typing import List


def make_logger(file_name):
    # file_name should be __file__ in implementation

    name = os.path.splitext(os.path.basename(file_name))[0]
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler = logging.FileHandler(f"{name}.log")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.DEBUG)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger


def count_time(start_time: float, task_name: str) -> None:
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"{task_name}: {elapsed_time:.2f} seconds")


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
