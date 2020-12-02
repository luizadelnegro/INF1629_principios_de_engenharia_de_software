from django.http import HttpResponse

from django.shortcuts import render
#!/usr/bin/env python
import sys, re, operator, string

#
# The functions
#
def read_file(path_to_file):
    with open(path_to_file) as f:
        data = f.read()
    return data

def filter_chars_and_normalize(str_data):
    pattern = re.compile('[\W_]+')
    return pattern.sub(' ', str_data).lower()

def scan(str_data):
    return str_data.split()

def remove_stop_words(word_list):
    with open('../stop_words.txt') as f:
        stop_words = f.read().split(',')
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in stop_words]

def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs

def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)

def print_all(word_freqs):
    if(len(word_freqs) > 0):
        print(word_freqs[0][0], '-', word_freqs[0][1])
        print_all(word_freqs[1:])

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def UserHome(request):

# 		return redirect('/' )

#
# The main function
#
#print_all(sort(frequencies(remove_stop_words(scan(filter_chars_and_normalize(read_file(sys.argv[1]))))))[0:25])