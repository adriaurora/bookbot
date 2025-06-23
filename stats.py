def count_words(book_text):
    words = book_text.split()
    return len(words)
def count_characters(book_text):
    characters_dict = {}
    for words in book_text:
        for character in words:
            character = character.lower()
            if character in characters_dict:
                characters_dict[character] += 1
            else:
                characters_dict[character] = 1
    return characters_dict