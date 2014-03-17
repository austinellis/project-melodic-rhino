#!/usr/bin/python -tt
# Copyright Austin Ellis
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Uses word lists to generate random project "code names" like
# "Project Flying Squirrel"

import sys
import argparse


def open_wordlist(wordtype):
    f = open(wordtype, 'rU')
    wordlist = {}
    i = 0
    for line in f:
        word = line.title()
        if word not in wordlist.values():
            wordlist[i] = word
            i += 1
    return wordlist


def print_wordlist(wordlist):
    wordlist_tuples = wordlist.items()
    for wordlist_tuples in wordlist_tuples[:]:
        print wordlist_tuples[0], ':', wordlist_tuples[1],
    pass


def generate(wordlist1, ):
    animal_file = 'wordlists/animals.txt'
    animals = open_wordlist(animal_file)


def main():
    # parameters = sys.argv[]
    # for p in parameters:

    generate()


if __name__ == '__main__':
    main()
