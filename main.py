import sys

from stats import get_book_text
from stats import get_num_words
from stats import count_characters
from stats import get_sorted_dict


def main():
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        char_dict = count_characters(text)
        sorted_list = get_sorted_dict(char_dict)
        print(f"============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print(f"----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print(f"--------- Character Count -------")
        for char_dict in sorted_list:
            if char_dict["char"].isalpha():
                print(f"{char_dict["char"]}: {char_dict["num"]}")
        print(f"============= END ===============")
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)


main()
