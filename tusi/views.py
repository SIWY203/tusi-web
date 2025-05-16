from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Aktualnosci, O_nas, Oferta, Galeria, Kontakt, Cennik, Home
from oferta_podstrony.models import Oferta_pozycja


def home(request):
    oferta = Oferta.objects.last()
    last_about = O_nas.objects.first()
    last_post = Aktualnosci.objects.last()
    home = Home.objects.all()
    context = {
        'oferta': oferta,
        'posts': last_post,
        'about': last_about,
        'home': home,
    }
    return render(request, 'tusi/home.html', context)


def o_nas(request):
    posts = O_nas.objects.order_by('kolejnosc')

    return render(request, 'tusi/o_nas.html', {
        'title': 'O nas',
        'posts': posts
    })


def aktualnosci(request):
    posts = Aktualnosci.objects.order_by('-kolejnosc')

    return render(request, 'tusi/aktualnosci.html', {
        'title': 'Aktualności',
        'posts': posts
    })


def oferta(request):
    posts = Oferta.objects.order_by('kolejnosc')
    cennik = Cennik.objects.all()
    pozycje = Oferta_pozycja.objects.all()
    podstrony_posty = []
    for pozycja in pozycje:
        pierwszy_post = pozycja.posts.order_by('kolejnosc').first()
        if pierwszy_post:
            podstrony_posty.append(pierwszy_post)

    return render(request, 'tusi/oferta.html', {
        'title': 'Oferta',
        'posts': posts,
        'cennik': cennik,
        'pozycje': podstrony_posty, # nazwa podstron
    })


def oferta_podstrona(request, slug):
    pozycja = get_object_or_404(Oferta_pozycja, slug=slug)
    posts = pozycja.posts.order_by('kolejnosc')  # Pobieranie powiązanych postów
    return render(request, 'tusi/oferta_podstrona.html', {
        'pozycja': pozycja,
        'posts': posts,
    })


def galeria(request):
    posts = Galeria.objects.order_by('-kolejnosc')

    return render(request, 'tusi/galeria.html', {
        'title': 'Galeria',
        'posts': posts
    })


def kontakt(request):
    posts = Kontakt.objects.order_by('kolejnosc')

    return render(request, 'tusi/kontakt.html', {
        'title': 'Kontakt',
        'posts': posts
    })


def cennik(request):
    posts = Cennik.objects.order_by('kolejnosc')

    return render(request, 'tusi/cennik.html', {
        'title': 'Cennik',
        'posts': posts
    })
