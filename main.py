from stats import (count_words, count_characters, sort_characters)
import sys

def get_book_text(book_path):
    with open(book_path) as file:
        book_text = file.read()
    return book_text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_characters = count_characters(book_text)
    sorted_characters = sort_characters(book_characters)
    printing(sorted_characters, book_path, book_text)

def printing(sorted_characters, book_path, book_text):
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {book_path}...')
    print("----------- Word Count ----------")
    print(f'Found {count_words(book_text)} total words')
    print("---------- Character Count -------")
    for character in sorted_characters:
        print(f"{character["char"]}: {character["num"]}")

main()