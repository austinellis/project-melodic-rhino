#!/usr/bin/python -tt
# Copyright Austin Ellis

# Uses word lists to generate random project "code names" like
# "Project Flying Squirrel"

import sys
import os
from os import listdir
import random
from os.path import isfile, join


def load_menu():
    path_dict = {}
    path = "/www/Sites/project_melodic_rhino/wordlists"
    path_list = [f for f in listdir(path) if isfile(join(path, f))]
    i = 0
    for item in path_list:
        if not item.startswith('.'):
            path_dict[i] = item
            i += 1
    return path_dict


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
    return word.rstrip('\n')


def get_word(list):
    filename = 'wordlists/' + list
    wordlist_dict = file_to_dict(filename)
    word = get_random(wordlist_dict)
    #print filename
    return word.rstrip('\n')


def print_wordlist(wordlist):
    for key, word in wordlist.iteritems():
        print key, word


def display_project(random_word_list, adjective=''):
    new_string = []
    if adjective != '':
        new_string.append(adjective)
        for item in random_word_list:
            new_string.append(item)
    else:
        for item in random_word_list:
            new_string.append(item)

    join_str = ' '.join(new_string)
    project_name = 'Project' + ' ' + join_str
    with open('results.txt', 'a') as results_file:
        results_file.write(project_name + "\n")
    return project_name


def main():
    menu = load_menu()
    random_word_list = []
    print '\n'
    print 'Available Lists: \n'
    for i in menu:
        print i + 1, ': ', menu[i]
    print '\n'
    word_count = int(raw_input('How many words would you like in '
                               'your project name:'))
    while word_count > 0:
        choice = int(raw_input('Select a list: '))
        choice = choice - 1
        if 'adjective' in menu[choice]:
            adjective = get_word(menu[choice])
            #print adjective
            word_count -= 1
        else:
            #print menu[choice]
            random_word_list.append(get_word(menu[choice]))
            word_count -= 1

    project_name = display_project(random_word_list, adjective)
    print project_name
        #print random_word_list

#    project_name = display_project(random_word, random_adj)
#    print project_name


if __name__ == '__main__':
    main()
