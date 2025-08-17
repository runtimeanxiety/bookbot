from stats import get_num_words
from stats import count_characters
from stats import get_sorted_dict


def main():
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words()} total words")
    print(f"--------- Character Count -------")
    for char_dict in get_sorted_dict():
        if char_dict["char"].isalpha() == True:
            print(f"{char_dict["char"]}: {char_dict["num"]}")
    print(f"============= END ===============")


main()
