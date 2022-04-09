from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "Ural/index.html")

def second_page(request):
    return render(request, "Ural/second_page.html")

def third_page(request):
    return render(request, "Ural/third_page.html")

def fourth_page(request):
    return render(request, "Ural/fourth_page.html")

def fifth_page(request):
    return render(request, "Ural/fifth_page.html")