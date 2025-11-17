def get_book_text(file_path):
    """Reads the content of a book from a text file and returns it as a string."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
def dict_character(text):
    """Returns a dictionary with the frequency of each character in the text."""
    char_freq = {}
    for char in text:
        if char in char_freq:
            char_freq[char] += 1
        else:
            if 'a' <= char <= 'z':
                char_freq[char] = 1
    char_freq = dict(sorted(char_freq.items(), key=lambda item: item[1], reverse=True))
    return char_freq