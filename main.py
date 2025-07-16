import sys

from stats import get_book_text, count_words, count_letters, pretty_report
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_string = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}") 
    num_of_words = count_words(book_string)
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    dict_book = count_letters(book_string)
    print("--------- Character Count -------")
    pretty_report(dict_book)
main();

