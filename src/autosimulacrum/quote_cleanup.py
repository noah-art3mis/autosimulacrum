import re
from utils.logger import make_logger

# PARAMETERS
BOOK_NAME = input("Enter folder name:")

# CONSTANTS
INPUT_FILE = f"data/text/{BOOK_NAME}/{BOOK_NAME}1.md"
OUTPUT_FILE = f"data/text/{BOOK_NAME}/{BOOK_NAME}2.md"
logger = make_logger(__file__)


def extract_quotes(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # removes h1 and h2
    content = re.sub(r"^\s*#{1,2}.*$", "", content, flags=re.MULTILINE)
    logger.info("removed h1 and h2")

    # finds page numbers and quotes
    # TODO added [a-z]. test
    pattern = re.compile(
        r">\s+(.*?)\s+at\s+page\s+(\d+[a-z]*)\s+on\s+\[\[.*?\]\]", re.DOTALL
    )
    logger.info("found page numbers")

    matches = pattern.findall(content)

    quotes = []
    for quote, page_number in matches:
        quotes.append(
            {"quote": quote.strip().replace("\n", " "), "page_number": page_number}
        )
    return quotes


def save_quotes_to_file(quotes, OUTPUT_FILE):
    # sort pages
    sorted_quotes = sorted(quotes, key=lambda x: x["page_number"])
    logger.info("sorted pages")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        for quote_data in sorted_quotes:
            # remove extraction error
            page_number = quote_data["page_number"]
            file.write(f"{page_number}\n")

            cleaned_quote = quote_data["quote"].rstrip("* *highlighted by").strip()
            file.write(f"{cleaned_quote}\n\n")
            logger.info(f"write page {page_number}")


if __name__ == "__main__":
    logger.info(f"Start quote cleanup process")

    quotes = extract_quotes(INPUT_FILE)
    save_quotes_to_file(quotes, OUTPUT_FILE)

    logger.info(f"End quote cleanup. Saved to {OUTPUT_FILE}")
