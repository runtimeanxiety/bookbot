import sys
from stats import get_book_text, get_num_words, count_characters, get_sorted_dict


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    try:
        text = get_book_text(filepath)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    num_words = get_num_words(text)
    char_dict = count_characters(text)
    sorted_list = get_sorted_dict(char_dict)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print(f"============= END ===============")


main()
