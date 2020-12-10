from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
import os
import sys

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        parse_file(uploaded_file.name)
    return render(request, 'upload.html', context)


def count_words(filepath):
    words = {}
    with open(filepath) as fp:
        for line in fp:
            for word in line.split():
                if word not in words:
                    words[word] = 1
                else:
                    words[word] += 1
    print(words)


def parse_file(f_name):
    filepath = 'media/'+f_name
    if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
    count_words(filepath)

    


