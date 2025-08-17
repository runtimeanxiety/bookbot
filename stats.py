def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    return len(text.split())


def count_characters(text):
    char_count = {}
    words = text.split()
    for word in words:
        for char in word.lower():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sort_on(items):
    return items["num"]


def get_sorted_dict(char_dict):
    dict_list = []
    for char in char_dict:
        new_dict = {}
        num = char_dict[char]
        new_dict["char"] = char
        new_dict["num"] = num
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
