#!/usr/bin/python -tt
# Copyright Austin Ellis
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Uses word lists to generate random project "code names" like
# "Project Flying Squirrel"

import sys
import os
import argparse
import random


def file_to_dict(filename):
    """
    Takes in a filename including path, opens the file,
    and returns a dict
    """
    f = open(filename, 'rU')
    wordlist_dict = {}
    i = 0
    for line in f:
        word = line.title()
        if word not in wordlist_dict.values():
            wordlist_dict[i] = word
            i += 1
    # for key, word in wordlist.iteritems():
    #    print key, word
    return wordlist_dict


def get_random(wordlist_dict):
    word = random.choice(wordlist_dict.values())
    return word


def get_animal():
    filename = 'wordlists/animals.txt'
    wordlist_dict = file_to_dict(filename)
    animal = get_random(wordlist_dict)
    return animal.rstrip('\n')


def get_greakgod():
    filename = 'wordlists/greekgods.txt'
    wordlist_dict = file_to_dict(filename)
    greekgod = get_random(wordlist_dict)
    return greekgod.rstrip('\n')



def get_adjective():
    filename = 'wordlists/adjectives.txt'
    wordlist_dict = file_to_dict(filename)
    adjective = get_random(wordlist_dict)
    return adjective.rstrip('\n')


def print_wordlist(wordlist):
    for key, word in wordlist.iteritems():
        print key, word


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', help='needs a filename')
    parser.add_argument('-a', '--animals',
                        help='Use animals wordlist', action='store_true')
    parser.add_argument('-gg', '--greekgods',
                        help='Use Greek gods wordlist', action='store_true')
    parser.add_argument('-adj', '--adjectives',
                        help='include adjectives', action='store_true')
    args = parser.parse_args()


    if args.file:
        wordlist_dict = file_to_dict(args.file)
        print get_random(wordlist_dict)

    if args.animals:
        animal = get_animal()

    if args.greekgods:
        greekgod = get_greakgod()

    if args.adjectives:
        adjective = get_adjective()

    project_name_output = 'Project ' + adjective + ' ' +  animal
    print project_name_output


if __name__ == '__main__':
    main()
