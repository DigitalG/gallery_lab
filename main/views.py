from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):

    last_arts = Artwork.objects.all().order_by('-post_date')[:4]

    ctx = {'last_arts': last_arts,}

    return render(request, 'index.html', ctx)


def art(request):
    categories = Category.objects.all()

    ctx = {'categories': categories}

    return render(request, 'art.html', ctx)


def artwork(request, id):
    artwork = Artwork.objects.get(pk=id)
    tags = artwork.Tags.replace(', ', ',').split(',')

    ctx = {'artwork': artwork,
           'tags': tags}

    return render(request, 'artwork.html', ctx)


def category(request, id):
    category = Category.objects.get(pk=id)
    gallery = Artwork.objects.filter(category=category)

    ctx = {'gallery': gallery,
           'category': category}

    return render(request, 'category.html', ctx)


def tag(request, tag):

    result = Artwork.objects.filter(Tags__contains=tag)

    ctx = {'result': result}

    return render(request, 'tag_search.html', ctx)
