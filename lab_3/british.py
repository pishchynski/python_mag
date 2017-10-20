import re
import argparse
import os
import random


def is_file_valid(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def parse_args():
    parser = argparse.ArgumentParser(description="Shuffles letters in text words.")
    parser.add_argument("-r", "--random", action="store_true",
                        help="If checked, letters in words will be shuffled randomly. Else, alphabetically.")
    parser.add_argument("-f", "--file", dest="filename",
                        help="Input file with text.", metavar="FILE",
                        type=lambda x: is_file_valid(parser, x))
    parser.add_argument("-t", "--text", dest="console_text",
                        help="Input text.", metavar="console_text",
                        type=str)

    return parser.parse_args()


def get_text(filename, console_text):
    if console_text:
        return console_text

    text = ""

    if filename:
        with open(filename, "r") as text_file:
            text = text_file.read()
    else:
        text = raw_input("Enter text to shuffle:")
    return text


def shuffle_word(word, is_random):
    res = ""
    if is_random:
        letters = list(word)
        random.shuffle(letters)
        res = "".join(letters)
    else:
        res = "".join(sorted(word))
    return res


def shuffle(text, is_random):
    split_regex = "([\s\.\,]+)"
    splitted_text = re.split(split_regex, text)
    res = []
    for word in splitted_text:
        if word and not re.match(split_regex, word):
            if len(word) <= 2:
                res.append(word)
                continue
            word = word.decode("utf-8")
            word = word[0] + shuffle_word(word[1:-1], is_random) + word[-1]
            word = word.encode("utf-8")
        res.append(word)
    return "".join(res)


def main():
    args = parse_args()
    text = get_text(args.filename, args.console_text)
    print(shuffle(text, args.random))
    return 0


if __name__ == '__main__':
    main()
