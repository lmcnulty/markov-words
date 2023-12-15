#!/usr/bin/env python3
import random, argparse, re, sys
from collections import defaultdict
clamp = lambda x, y, z: max(x, min(y, z))

def main():
    args = get_arguments()

    words = []
    with open(args.dictionary_file, encoding=args.encoding) as f:
        for line in f.read().split('\n'):
            if len(line) == 0: continue
            if args.no_apostrophes and "'" in line: continue
            if args.no_capitals and re.match('[A-Z]', line[0]): continue
            words.append(line)

    successors = get_successors(words, args.n)

    for i in range(args.count):
        word = random_word(
            successors, args.n, 
            max_length=args.max_length, 
            end_bias=args.end_bias
        )
        print(word)

def get_successors(words, n):
    successors = defaultdict(lambda: defaultdict(lambda: 0))
    for word in words:
        for ci, char in enumerate(list(word) + ['$']):
            head = ''
            if ci == 0:
                head = '^'
            elif ci < n:
                head = '^' + word[0:clamp(1, ci, len(word))]
            elif ci >= n:
                head = word[ci - n:ci]

            successors[head][char] += 1
    return successors

def random_successor(successors, substring, end_bias = 1):
    choices = []
    for key, value in successors[substring].items():
        if value == '$':
            choices += [key] * (end_bias * value)
        else:
            choices += [key] * value
    return random.choice(choices)

def random_word(successors, n, max_length = sys.maxsize, end_bias = 1):
    word = ""
    while len(word) < max_length - 1:
        head = word[max(0, len(word) - n):len(word)]
        if len(head) < n:
            head = '^' + head
        successor = random_successor(successors, head, end_bias) 
        if successor == '$':
            break
        word += successor
    return word

def get_arguments():
    parser = argparse.ArgumentParser(prog='markdov-words')
    parser.add_argument(
        '-d', '--dictionary-file', default="/usr/share/dict/words",
        help=(
            "Path to dictionary file -- "
            "A dictionary file is just one containing "
            "a list of words separated by line-breaks. "
            "On Unix systems these can usually be found in "
            "/usr/share/dict/."
        )
    )
    parser.add_argument(
        '--no-apostrophes', action='store_true',
        help="Exclude words with apostrophes from the dictionary"
    )
    parser.add_argument(
        '--no-capitals', action='store_true',
        help="Exclude words starting with A-Z capital letters"
    )
    parser.add_argument(
        '--encoding', default="utf-8",
        help="Number of words to print"
    )
    parser.add_argument(
        '-c', '--count', type=int, default=1,
        help="Number of words to print"
    )
    parser.add_argument(
        '-e', '--end-bias', type=int, default=100,
        help=(
            "Multiplier for the probability "
            "that a word will end at a given point -- "
            "Note that sometime the probability is zero, "
            "so setting this very high does not guarantee "
            "that words will not be abnormally long. "
        )
    )
    parser.add_argument(
        '-n', '--n', type=int, default=3,
        help=(
            "The number of previous letters to take into account"
            "in selecting the next one -- "
            "For high values of n, "
            "the results are likely "
            "to exactly reproduce words in the dictionary, "
            "whereas for lower values, "
            "they are likely to sound implausible."
        )
    )
    parser.add_argument(
        '-l', '--max-length', type=int, default=16,
        help=(
            "Maximum length of a word, "
            "which if reached will simply terminate the word, "
            "even if the ending is not a probable one."
        )
    )
    return parser.parse_args()

if __name__ == '__main__':
    main()
