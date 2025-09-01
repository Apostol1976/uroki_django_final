from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home - Главная"}
    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "Home - Главная"}
    return render(request, "main/about.html", context)


def kontakti(request):
    context = {"title": "Home - Главная"}
    return render(request, "main/kontakti.html", context)
