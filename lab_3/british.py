import re
import argparse
import random
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Shuffles letters in text words.")
    parser.add_argument("-r", "--random")
