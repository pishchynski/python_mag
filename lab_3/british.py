import codecs
import re
import argparse
import os
import random
import sys


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
        with codecs.open(filename, mode="r", encoding="utf-8") as text_file:
            text = text_file.read()
    else:
        print "Enter text to shuffle:"
        sys.stdout.flush()
        text = raw_input()
    return text


def shuffle_word(word, is_random):
    res = ""
    if is_random:
        letters = list(word[1:-1])
        random.shuffle(letters)
        res = word[0] + "".join(letters) + word[-1]
    else:
        res = "".join(sorted(word))
    return res


def shuffle(text, is_random):
    pattern = r'[\w\d-]+'

    res = list(text)
    for word in re.finditer(pattern, text, re.U):
        if word.end() - word.start() + 1 <= 3:
            res[word.start():word.end()] = word
            continue

        res[word.start():word.end()] = shuffle_word(text[word.start():word.end()], is_random)
    return "".join(res).encode("utf-8")


def main():
    args = parse_args()
    text = get_text(args.filename, args.console_text)
    print(shuffle(text, args.random))
    return 0


if __name__ == '__main__':
    main()
