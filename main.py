from stats import count_words
from stats import count_characters

def get_book_text(book_path):
    with open(book_path) as file:
        book_text = file.read()
    return book_text

def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    book_characters = count_characters(book_text)
    print(f'{count_words(book_text)} words found in the document.')
    print(book_characters)

main()