def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    characters_dict = {}
    for words in book_text:
        for character in words:
            if character.isalpha():
                character = character.lower()
                if character in characters_dict:
                    characters_dict[character] += 1
                else:
                    characters_dict[character] = 1
    return characters_dict

def get_order(characters_dict):
    return characters_dict["num"]

def sort_characters(characters_dict):
    characters_list_dictionary = []
    for character in characters_dict:
        characters_list_dictionary.append({"char": character, "num": characters_dict[character]})
    characters_list_dictionary.sort(reverse=True, key=get_order)
    return characters_list_dictionary


def sort_characters2(characters_dict):
    characters_list_dictionary = []
    for character, value in characters_dict.items():
        character_dictionary= {"char": character, "num": value}
        characters_list_dictionary.append(character_dictionary)
    characters_list_dictionary.sort(reverse=True, key=get_order)
    return characters_list_dictionary