from stats import get_book_text, word_count, count_characters, sort_on


def main():
    # relative path to frankenstein.txt
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    count = word_count(book_text)
    char_count = count_characters(book_text)

    char_list = []

    for char, num in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": num})

    # use sorted() instead of .sort() to avoid None result
    sorted_list = sorted(char_list, reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")

    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")


# run the program
if __name__ == "__main__":
    main()
