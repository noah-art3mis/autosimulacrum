import re

BOOK_NAME = ""
input_file = f"data/text/{BOOK_NAME}/{BOOK_NAME}1.md"
output_file = f"data/text/{BOOK_NAME}/{BOOK_NAME}2.md"

def extract_quotes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # removes h1 and h2
    content = re.sub(r'^\s*#{1,2}.*$', '', content, flags=re.MULTILINE) 
    #finds page numbers and quotes
    #added [a-z]. test
    pattern = re.compile(r'>\s+(.*?)\s+at\s+page\s+(\d+[a-z]*)\s+on\s+\[\[.*?\]\]', re.DOTALL)
    matches = pattern.findall(content)

    quotes = []
    for quote, page_number in matches:
        quotes.append({
            'quote': quote.strip().replace('\n', ' '),
            'page_number': page_number
        })

    return quotes


def save_quotes_to_file(quotes, output_file):
    #sort pages
    sorted_quotes = sorted(quotes, key=lambda x: x['page_number'])
        
    with open(output_file, 'w', encoding='utf-8') as file:
        for quote_data in sorted_quotes:
            #remove extraction error
            cleaned_quote = quote_data["quote"].rstrip('* *highlighted by').strip()
            file.write(f'{quote_data["page_number"]}\n')
            file.write(f'{cleaned_quote}\n\n')

if __name__ == "__main__":
    print(f'Batch converting')
    
    quotes = extract_quotes(input_file)
    save_quotes_to_file(quotes, output_file)

    print(f'Quotes extracted and saved to {output_file}')
