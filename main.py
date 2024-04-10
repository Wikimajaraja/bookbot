def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters_dictionary = get_num_characters(text)
    print(f"{num_words} words were found in the document.")
    
    sorted_dict = sort_me(characters_dictionary)

    for element in sorted_dict:
        if sorted_dict[element] == 1:
            time_times = "time"
        else:
            time_times = "times"
        print(f"The {element} character was found {sorted_dict[element]} {time_times}.")


# Function to get the amount of words in the text.
def get_num_words(text):
    words = text.split()
    return len(words)


# Function to get the characters and the amount of times they appear on the text.
def get_num_characters(text):
    lowered_text = text.lower()
    characters_counter = {}
    
    for character in lowered_text:
        if character.isalpha() == True:
            if character in characters_counter:
                characters_counter[character] += 1
            else:
                characters_counter[character] = 0
    return characters_counter


# Function to sort the dictionary.
# This creates a new dictionary using the keys and values from the old dictionary elements, 
# but they will be sorted using the second element (key=lambda item: item[1]) of the dictionary, and in descending order (reverse=True)
def sort_me(baby):
    sorted_baby = {key: value for key, value in sorted(baby.items(), key=lambda item: item[1], reverse=True)}
    return sorted_baby


# Function to get the file.
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()