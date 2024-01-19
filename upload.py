import re
from playwright.sync_api import Page, expect, sync_playwright
import time
from utils import count_time, get_data_folders, get_file_names_in_folder
    
# PARAMETERS
BOOK_FOLDER_NAME = 'test'

# CONSTANTS
DATA_PATH = f'./data-src/ordered/{BOOK_FOLDER_NAME}'
PAGE = "https://playwright.dev/"

def main():
    with sync_playwright() as p:
        start_time = time.perf_counter()

        # browser = p.firefox.launch(headless=False, slow_mo=50)
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(PAGE)
        
        for folder in get_data_folders(DATA_PATH):
            page.locator(':text("Create Post")').click()
            
            files = get_file_names_in_folder()(folder)
            page.get_by_label("Upload files").set_input_files(files)

            page.locator(':text("Save as Draft")').click()
            count_time(start_time, "made another post")
                   
        browser.close()



if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    count_time(start_time, "final time")
    

