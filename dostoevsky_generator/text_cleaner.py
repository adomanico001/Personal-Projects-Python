# Cleans texts for Dostoevsky generator
# @author Addie Domanico
# @version 2025/03/08

import re


def load_books(book_files):
    """Reads and cleans the Dostoevsky novels by removing headers, footers, and unnecessary text

    :param book_files: A dict with keys as file paths and values as book titles
    :return: A dict of cleaned book texts
    """

    cleaned_books = {}

    for book_file, book_title in book_files.items():
        try:
            with open(book_file, 'r', encoding='utf-8') as file:
                raw_text = file.read()

            # Regex pattern to remove header
            header_pattern = r'\*\*\* START OF THE PROJECT GUTENBERG EBOOK .*? \*\*\*'
            clean_text = re.sub(header_pattern, ' ', raw_text, flags=re.DOTALL)

            # Find start of actual book using title
            start_match = re.search(rf'\n\s*{re.escape(book_title)}', clean_text, flags=re.IGNORECASE)
            if start_match:
                clean_text = clean_text[start_match.end():]
                clean_text = f"{book_title}\n\n" + clean_text

            footer_pattern = r'\*\* END OF THE PROJECT GUTENBERG EBOOK .*?\*\*\*'
            clean_text = re.sub(footer_pattern, ' ', clean_text, flags=re.DOTALL)

            cleaned_books[book_file] = clean_text.strip()

        except FileNotFoundError:
            print(f"Error: file '{book_file}' not found.")
            cleaned_books[book_file] = ""
        except Exception as e:
            print(f"Error loading '{book_file}': {e}")
            cleaned_books[book_file] = ""

    return cleaned_books

books = {
    "crime_and_punishment.txt": "CRIME AND PUNISHMENT",
    "the_brothers_karamazov.txt": "THE BROTHERS KARAMAZOV",
    "notes_from_the_underground.txt": "NOTES FROM THE UNDERGROUND"
}

cleaned_texts = load_books(books)

for file_path, text in cleaned_texts.items():
    print(f"\n--- {file_path} ---\n{text[:500]}\n")
