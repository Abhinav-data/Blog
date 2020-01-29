from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context={"title":"Hello Boy", "my_list":[1,2,3,4,5,6]}
    return render(request, "index.html", context)


def about_page(request):
    return HttpResponse("<h1>About</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact</h1>")
