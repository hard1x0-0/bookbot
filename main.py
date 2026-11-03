import sys
from stats import (
    charc_dict_to_sorted_list,
    print_report,
    word_count,
    get_book_text,
    get_chars_dict,
    
)

# return x


def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])

    count = word_count(text)
    print(f"Found {count} total words")

    count_lower = get_chars_dict(text)
    # print(count_lower)

    srt_list = charc_dict_to_sorted_list(count_lower)
    # print(srt_list)

    print_report(sys.argv[1]
        ,
        count,
        srt_list
    )
    

    # print(printreport)

    # print(text)


main()