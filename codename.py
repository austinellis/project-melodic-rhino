#!/usr/bin/python -tt
# Copyright Austin Ellis
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Uses word lists to generate random project "code names" like
# "Project Flying Squirrel"

import sys
import argparse
import os


def open_wordlist(filename):
    """
    Takes in a filename including path, opens the file,
    and returns a dict
    """
    f = open(filename, 'rU')
    wordlist_dict = {}
    i = 0
    for line in f:
        word = line.title()
        if word not in wordlist.values():
            wordlist[i] = word
            i += 1
    #for key, word in wordlist.iteritems():
    #    print key, word
    return wordlist_dict

def generate_wordlist(wordlist1):
    file_name = wordlist1
    words = open_wordlist(file_name)



def print_wordlist(wordlist):
    wordlist_tuples = wordlist.items()
    for wordlist_tuples in wordlist_tuples[:]:
        print wordlist_tuples[0], ':', wordlist_tuples[1],
    pass





def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('customfile', help='needs a filename', action='store_true')
    parser.add_argument('-a', '--animals', help='Use animals wordlist', action='store_true')
    parser.add_argument('-gg', '--greekgods', help='Use Greek gods wordlist', action='store_true')
    args = parser.parse_args()

    #if args.filename:
    #    generate_wordlist(args.customfile)
    if args.animals:
        filename = 'wordlists/animals.txt'
        #filepath = os.path.abspath(filename)
        generate_wordlist(filename)
    if args.greekgods:
        filename = 'wordlists/greekgods.txt'
        generate_wordlist(filename)


if __name__ == '__main__':
    main()
