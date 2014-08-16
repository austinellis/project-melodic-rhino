#!/usr/bin/python -tt
# Copyright Austin Ellis

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

#wordtype = "animal"


def get_word(wordtype, num=1):
    if wordtype == 'adjective':
        pass
    if wordtype == 'animal':
        pass
    if wordtype == 'greekgod':
        pass
    if wordtype == 'customfile':
        pass


def get_random(wordlist_dict):
    word = random.choice(wordlist_dict.values())
    return word.rstrip('\n')


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


def display_project(random_word, random_adj=False):
    new_string = []
    if random_adj != False:
        new_string.append(random_adj)
        for item in random_word:
            new_string.append(item)
    else:
        for item in random_word:
            new_string.append(item)

    join_str = ' '.join(new_string)
    project_name = 'Project' + ' ' + join_str
    with open('results.txt', 'a') as results_file:
        results_file.write(project_name + "\n")
    return project_name



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
    random_word = []
    random_adj = False
    if args.file:
        wordlist_dict = file_to_dict(args.file)
        random_word.append(get_random(wordlist_dict))

    if args.animals:
        random_word.append(get_animal())

    if args.greekgods:
        random_word.append(get_greakgod())

    if args.adjectives:
        random_adj = get_adjective()

    #project_name_output = 'Project ' + ' ' + random_word
    # print project_name_output
    project_name = display_project(random_word, random_adj)
    print project_name


if __name__ == '__main__':
    main()
