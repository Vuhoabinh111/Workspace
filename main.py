from stats import *
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
book_text = get_book_text(book_path)
for i in dict_character(book_text.lower()):
    print(f"{i}: {dict_character(book_text.lower())[i]}")