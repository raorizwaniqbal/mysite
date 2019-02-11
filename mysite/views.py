from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def count(request):
    data = request.GET['fulltextarea']
    word_text = data.split()
    word_length = len(word_text)
    print(word_length)
    return render(request, 'count.html', {'fulltextarea':data, 'words' : word_length})



