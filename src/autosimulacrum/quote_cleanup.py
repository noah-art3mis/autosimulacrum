import re
import sys
from utils.logger import make_logger


def extract_quotes(book_name, file_name):
    input_file = f"./data/{book_name}/text/{file_name}"

    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()
    except FileNotFoundError as e:
        logger.exception(f"The file {input_file} was not found. Exiting.")
        sys.exit(1)

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


def save_quotes_to_file(quotes, output_file):
    output_file = f"./data/{book_name}/text/{book_name}_cleanup.md"

    # sort pages
    sorted_quotes = sorted(quotes, key=lambda x: x["page_number"])
    logger.info("sorted pages")

    with open(output_file, "w", encoding="utf-8") as file:
        for quote_data in sorted_quotes:
            # remove extraction error
            page_number = quote_data["page_number"]
            file.write(f"{page_number}\n")

            cleaned_quote = quote_data["quote"].rstrip("* *highlighted by").strip()
            file.write(f"{cleaned_quote}\n\n")
            logger.info(f"write page {page_number}")
    logger.info(f"End quote cleanup. Saved to {output_file}")


if __name__ == "__main__":
    logger = make_logger(__file__)
    logger.info(f"Start quote cleanup process")
    book_name = input("Enter folder name:")
    file_name = input("Enter file name (with extension):")

    quotes = extract_quotes(book_name, file_name)
    save_quotes_to_file(quotes, book_name)
