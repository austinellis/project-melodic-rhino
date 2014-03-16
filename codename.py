#!/usr/bin/python -tt
# Copyright Austin Ellis
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Uses word lists to generate random project "code names" like
# "Project Flying Squirrel"

import sys


def open_wordlist(wordtype):
    f = open(wordtype, 'rU')
    wordlist = {}
    i = 0
    for line in f:
        row = line.title()
        for word in row:
            print word
            if word not in wordlist.keys():
                wordlist[i] = word
                i += 1
                #print wordlist


def generate():
    animal_file = 'animals.txt'
    animals = open_wordlist(animal_file)
    print animals


def main():
     #parameters = sys.argv[]
     # for p in parameters:
     generate()


if __name__ == '__main__':
    main()
