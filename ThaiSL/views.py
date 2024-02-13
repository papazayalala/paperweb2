from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.staticfiles import finders
from pythainlp import word_tokenize

def home_view(request):
    return render(request, 'home.html')

def animation_view(request):
    if request.method == 'POST':
        text = request.POST.get('sen')
        words = word_tokenize(text, engine="newmm", keep_whitespace=False)

        filtered_text = []
        for w in words:
            path = w + ".mp4"
            f = finders.find(path)
            if not f:
                filtered_text.extend(list(w))
            else:
                filtered_text.append(w)
        words = filtered_text

        context = {
            'words': words,
            'text': text,
        }
        return render(request, 'animation.html', context)
    
    else:
        context = {}
        return render(request, 'animation.html', context)

def animationeng_view(request):
    if request.method == 'POST':
        text = request.POST.get('sen')
        words = word_tokenize(text, engine="newmm", keep_whitespace=False)

        filtered_text = []
        for w in words:
            path = w + ".mp4"
            f = finders.find(path)
            if not f:
                filtered_text.extend(list(w))
            else:
                filtered_text.append(w)
        words = filtered_text

        context = {
            'words': words,
            'text': text,
        }
        return render(request, 'animationeng.html', context)
    
    else:
        context = {}
        return render(request, 'animationeng.html', context)


def image_view(request):
    return render(request, 'image.html')
    
def pronoun_view(request):
    return render(request, 'pronoun.html')

def emotional_view(request):
    return render(request, 'emotional.html')

def verb_view(request):
    return render(request, 'verb.html')

def most_view(request):
    return render(request, 'most.html')

def place_view(request):
    return render(request, 'place.html')

def cons_view(request):
    return render(request, 'cons.html')

def vowel_view(request):
    return render(request, 'vowel.html')

def tone_view(request):
    return render(request, 'tone.html')

def family_view(request):
    return render(request, 'family.html')

def stoA_view(request):
    return render(request, 'stoA.html')