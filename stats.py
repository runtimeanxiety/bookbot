def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words():
    num_words = 0
    file_contents = get_book_text("books/frankenstein.txt")
    words = file_contents.split()
    for word in words:
        num_words += 1
    return num_words


def count_characters():
    char_count = {}
    file_contents = get_book_text("books/frankenstein.txt")
    words = file_contents.split()
    for word in words:
        for char in word:
            if char.lower() not in char_count:
                char_count[char.lower()] = 0
                char_count[char.lower()] += 1
            else:
                char_count[char.lower()] += 1
    return char_count


def sort_on(items):
    return items["num"]


def get_sorted_dict():
    dict_list = []
    dict = count_characters()
    for char in dict:
        new_dict = {}
        num = dict[char]
        new_dict["char"] = char
        new_dict["num"] = num
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
