from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def counter(request):
    texts = request.POST['texts']
    text = len(texts.split())
    return render(request, 'counter.html', {'text': text})
