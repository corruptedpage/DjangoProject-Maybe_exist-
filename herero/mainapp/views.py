from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/main.html')


def products(request):
    return render(request, 'mainapp/katalog.html')


def main(request):
    return render(request, 'mainapp/main.html')


def here(request):
    return render(request, 'mainapp/!!.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')