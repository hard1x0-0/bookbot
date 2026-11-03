# returning text of book as a string
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


# word count
def word_count(texts):
    words = texts.split()
    return (len(words))


# character count
def get_chars_dict(texts):
    my_dict = {}
    lower_text = texts.lower()

    for char in lower_text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1

    return my_dict


def sort_on(my_dict: tuple[str, int]) -> int:
    return my_dict[1]


def charc_dict_to_sorted_list(my_dict: dict[str, int]):
    my_list = []

    for char in my_dict:
        count = my_dict[char]
        x = (char, count)
        my_list.append(x)

    sorted_my_list = sorted(
        my_list,
        reverse=True,
        key=sort_on
    )

    return sorted_my_list


# print a report
# str.isalpha() returns true when a string is non-empty
# and all of its characters are alphabetic
def print_report(book_path, wordcount, sortedlist):
    # print(f"========== BOOKBOT ==========\nAnalyzing book found at {path}...\n")
    # print("============ BOOKBOT ============")

    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for char,count in sortedlist:
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")