from stats import get_book_text, count_words, count_letters, pretty_report
def main():
    print("============ BOOKBOT ============")
    book_string = get_book_text("./books/frankenstein.txt")
    print("Analyzing book found at books/frankenstein.txt...")
    num_of_words = count_words(book_string)
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    dict_book = count_letters(book_string)
    print("--------- Character Count -------")
    pretty_report(dict_book)
main();

