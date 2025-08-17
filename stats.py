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
