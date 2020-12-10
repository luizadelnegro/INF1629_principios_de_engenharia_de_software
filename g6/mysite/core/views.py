from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import operator
import os
import re
import string
import sys


def upload(request):
    context = {}
    if request.method == 'POST':
        words_file = request.FILES['words']
        stop_words_file = request.FILES['stop_words']

        fs = FileSystemStorage()
        name = fs.save(words_file.name, words_file)
        context['url'] = fs.url(name)
        f_name = words_file.name
        context['frequencies'] = sort(frequencies(remove_stop_words(
            scan(filter_chars_and_normalize(read_file(f_name))), stop_words_file)))

    return render(request, 'upload.html', context)


def read_file(path_to_file):
    with open(path_to_file) as f:
        str_data = f.read()
    return str_data


def filter_chars_and_normalize(str_data):
    pattern = re.compile('[\W_]+')
    return pattern.sub(' ', str_data).lower()


def scan(str_data):
    return str_data.split()


def remove_stop_words(word_list, stop_words_file):
    f_name = stop_words_file.name

    with open(f_name) as f:
        stop_words = f.read().split(',')
        print(stop_words)

    stop_words.extend(list(string.ascii_lowercase))
    return [word for word in word_list if not word in stop_words]


def frequencies(word_list):
    word_freqs = {}
    for word in word_list:
        if word in word_freqs:
            word_freqs[word] += 1
        else:
            word_freqs[word] = 1
    return word_freqs


def sort(word_freq):
    return sorted(word_freq.items(), key=operator.itemgetter(1), reverse=True)
