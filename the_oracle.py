# -*- coding: utf-8 -*-
"""the_oracle.ipynb

Original file is located at
    https://colab.research.google.com/drive/1bvBVxXwZLdhluU1kP6vVMmCWf7CEQbMO
"""

import requests


def get_kjv() -> str:
    response = requests.get('https://openbible.com/textfiles/kjv.txt')
    return response.text

import string

def remove_punctuation(s) -> str:
    ret = []
    for c in s:
        if c not in string.punctuation:
            ret.append(c)
    return ''.join(ret)


def process_kjv(kjv) -> tuple[list[str], list[int]]:
    words = []
    line_lengths = []
    lines = kjv.split('\n')
    for line in lines:
        line = remove_punctuation(line)
        line_words = line.split()[2:]
        words.extend(line_words)
        line_lengths.append(len(line_words))
    return words, line_lengths

import random


def gen_word(words: list[str]) -> str:
    return random.choice(words)


def gen_length(line_lengths: list[int]) -> int:
    return random.choice(line_lengths)


def gen_verse(words: list[str], line_lengths: list[int]) -> str:
    length = gen_length(line_lengths)
    verse = []
    for _ in range(length):
        verse.append(gen_word(words))
    verse = ' '.join(verse) + '.'
    verse = verse[0].upper() + verse[1:]
    return verse

def main():
    print("--- The Oracle ---")
    print("Getting KJV Bible ready...")
    try:
      kjv = get_kjv()
    except:
      print("Failed to fetch the KJV file, there is likely some issue with Colab if you ever have this error reported, wait for a while and try again.")
      return
    words, line_lengths = process_kjv(kjv)
    print("Press ENTER to get a new verse, press Ctrl-C or enter 'quit' to exit.")
    while True:
        try:
            cmd = input().lower()
        except KeyboardInterrupt:
            break
        if cmd == 'quit':
            break
        verse = gen_verse(words, line_lengths)
        print(verse)
    print('Exit.')


if __name__ == '__main__':
    main()
