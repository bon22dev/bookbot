# bookbot/main.py

def get_book_text(filepath):
    """Takes a file path and returns its contents as a string."""
    with open(filepath) as file:
        return file.read()


def word_count(book_text):
    """Takes the book text and returns the number of words."""
    words = book_text.split()
    return len(words)

def count_characters(text):
    """Takes the text from the book and returns a dictionary
    of character counts (case-insensitive)."""
    text = text.lower()
    char_counts = {}

    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts

def sort_on(items):
	return items["num"]

