import time
from playwright.sync_api import Page, expect, sync_playwright

from utils.logger import make_logger
from utils.file_handling import get_data_folders, get_file_names_in_folder
from utils.time_counter import count_time

    
# PARAMETERS
BOOK_FOLDER_NAME = input("Enter folder name:")

# CONSTANTS
DATA_PATH = f'./data/ordered/{BOOK_FOLDER_NAME}'
PAGE = "https://playwright.dev/"
logger = make_logger(__file__)

https://playwright.dev/python/docs/input
https://playwright.dev/python/docs/api/class-page#page-event-file-chooser
https://playwright.dev/python/docs/locators

def main():
    with sync_playwright() as p:
        start_time = time.perf_counter()

        # browser = p.firefox.launch(headless=False, slow_mo=50)
        browser = p.firefox.launch()
        page = browser.new_page()
        page.goto(PAGE)
        
        for folder in get_data_folders(DATA_PATH):
            page.locator(':text("Create Post")').click()
            
            try:
                files = get_file_names_in_folder(folder)
            except Exception as e:
                logger.exception('error')
                raise
            
            page.get_by_label("Upload files").set_input_files(files)

            page.locator(':text("Save as Draft")').click()
            count_time(start_time, "made another post")
                   
        browser.close()



if __name__ == "__main__":
    
    start_time = time.perf_counter()
    main()
    count_time(start_time, "final time")
    

