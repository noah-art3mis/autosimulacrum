import os
import re
import shutil
from utils.file_handling import get_file_names_in_folder
from utils.logger import make_logger


def main(book_name, logger) -> None:
    input_path = f"./data/{book_name}/img/raw/"
    output_path = f"./data/{book_name}/img/ordered/"

    logger.info(f"Start simulacrum data organization on '{input_path}'")

    try:
        file_names = get_file_names_in_folder(input_path)
    except FileNotFoundError as e:
        logger.exception(str(e))
        raise

    for file_name in file_names:
        match = re.search(r"(\d+[a-z]*)", file_name)

        if not match:
            logger.warning(
                f"Skipping iteration: File name does not match regex: {file_name}"
            )
            continue

        page_number = match.group(1)

        new_folder_path = os.path.join(output_path, page_number)
        new_file_name = modify_filename(file_name, page_number)

        os.makedirs(new_folder_path, exist_ok=True)

        source_path = os.path.join(input_path, file_name)
        destination_path = os.path.join(new_folder_path, new_file_name)

        if os.path.exists(destination_path):
            logger.warning(
                f"Skipping iteration: File already exists at destination: {destination_path}. "
            )
            continue

        shutil.copy(source_path, destination_path)
        logger.info(f"copied {file_name} to {new_file_name}")
        logger.info(f"End simulacrum data organization on '{output_path}'")


def modify_filename(file_name, page_number) -> str:
    try:
        modified_file_name = (
            file_name
            if re.search(rf"{page_number}\s*\((\d+)\)", file_name)
            else re.sub(r"^(\d+)", rf"\1 (1)", file_name)
        )
        return modified_file_name
    except Exception as e:
        logger.exception(
            f"Skipping iteration: error modifying file name: {file_name}/ {e}"
        )
        return file_name


if __name__ == "__main__":
    logger = make_logger(__file__)
    book_name = input("Enter folder name:")
    main(book_name, logger)
