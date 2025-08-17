def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def count_words():
    num_words = 0
    file_contents = get_book_text("books/frankenstein.txt")
    words = file_contents.split()
    for word in words:
        num_words += 1
    return num_words

def main():
    print(f"{count_words()} words found in the document")

main()