import sys
from stats import word_count, char_count, sort_dictionary

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_content = get_book_text(sys.argv[1])
    num_words = word_count(file_content)
    char_dict = char_count(file_content)
    sorted_list = sort_dictionary(char_dict)
    print(f"Found {num_words} total words")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")


main()
