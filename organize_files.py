import os 
import re
import shutil
from utils import get_file_names_in_folder

# PARAMETERS
BOOK_FOLDER_NAME = 'pmn'

# CONSTANTS
DATA_INPUT = f'./data/raw/{BOOK_FOLDER_NAME}'
DATA_OUTPUT = f'./data/ordered/{BOOK_FOLDER_NAME}'

def main(input_path, output_path):
    file_names = get_file_names_in_folder(input_path)

    for file_name in file_names:
        match = re.search(r'(\d+)', file_name)

        if not match:
            print(f"\tSkipping iteration: File name does not match regex: {file_name}. Skipping iteration")
            continue
            
        page_number = match.group(1)
        
        new_folder_path = os.path.join(output_path, page_number)
        new_file_name = modify_filename(file_name, page_number)
        
        os.makedirs(new_folder_path, exist_ok=True)
        
        source_path = os.path.join(input_path, file_name)
        destination_path = os.path.join(new_folder_path, new_file_name)
        
        if os.path.exists(destination_path):
            print(f"\tSkipping iteration: File already exists at destination: {destination_path}. ")
            continue
        
            
        shutil.copy(source_path, destination_path)

        
def modify_filename(file_name, page_number):
    try:
        modified_file_name = file_name if re.search(fr'{page_number}\s*\((\d+)\)', file_name) else re.sub(r'^(\d+)', fr'\1 (1)', file_name)
        return modified_file_name
    except Exception as e:
        print(f"\tSkipping iteration: error modifying file name: {file_name}/ {e}")
        return file_name
            
if __name__ == "__main__":
    print("== Start simulacrum data organization == ")
    main(DATA_INPUT, DATA_OUTPUT)
    print("== Simulacrum data organization successful ==")

