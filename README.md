# BookBot

BookBot is a command-line tool that analyzes a book (any plain text file). It counts the total words and shows how often each letter appears, sorted from most to least common.

This is my first [Boot.dev](https://www.boot.dev) project.

## Features

- Counts the total number of words in a book
- Counts how many times each character appears (case-insensitive)
- Sorts letters from most to least frequent
- Prints a clean, readable report

## Project Structure

```
bookbot/
├── main.py       # Entry point: reads the path, runs the analysis, prints the report
├── stats.py      # Helper functions: text loading, word count, character count, sorting, report
├── books/        # Put your .txt books here
└── README.md
```

## Requirements

- Python 3.9 or higher

No external libraries are needed.

## Usage

Clone the repo:

```bash
git clone https://github.com/<your-username>/bookbot.git
cd bookbot
```

Run it with the path to a book:

```bash
python3 main.py books/<your_book>.txt
```

If you forget the path, you will see:

```
Usage: python3 main.py <path_to_book>
```

## Example Output

```
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

## How It Works

1. `get_book_text` reads the whole file into a string.
2. `word_count` splits the text on whitespace and counts the pieces.
3. `get_chars_dict` lowercases the text and tallies each character in a dictionary.
4. `charc_dict_to_sorted_list` turns the dictionary into a list of `(char, count)` pairs and sorts it by count, highest first.
5. `print_report` prints the word count and only the alphabetic characters.

## What I Learned

- Reading files in Python
- Working with strings, dictionaries, lists, and tuples
- Sorting with a custom `key` function
- Splitting code across modules and importing between files
- Reading command-line arguments with `sys.argv`

## License

This project is for learning purposes.