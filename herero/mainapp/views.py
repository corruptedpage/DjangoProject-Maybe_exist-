from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainapp/main.html')


def katalog(request):
    return render(request, 'mainapp/katalog.html')


def main(request):
    return render(request, 'mainapp/main.html')