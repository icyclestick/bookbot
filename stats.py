def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
        return book_contents

def count_words(string):
    split_string = string.split()
    amount = len(split_string)
    return amount

def count_letters(string):
    book_dict = {}
    lower_cased = string.lower()
    for char in lower_cased:
        if char in book_dict:
            book_dict[char] += 1
        elif char not in book_dict:
            book_dict[char] = 1
    return book_dict

def sort_on(items):
        return items["count"]

def pretty_report(dictionary_book):
    list_of_characters = []
    for key in dictionary_book:
        list_of_characters.append({"char": key, "count":dictionary_book[key]})
    list_of_characters.sort(reverse=True, key=sort_on)

    for item in list_of_characters:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["count"]}\n")
