from stats import get_length, letter_count, chars_dict_to_sorted_list
import sys

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(file_path, word_count, char_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def main(file_path: str) -> None:
    word_count = get_length(file_path)
    words = get_book_text(file_path)
    no_of_letters = letter_count(words)
    sorted_letter_count = chars_dict_to_sorted_list(no_of_letters)
    print_report(file_path, word_count, sorted_letter_count)

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main(sys.argv[1])
