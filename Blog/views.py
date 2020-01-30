from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    context={"title":"Hello Boy", "my_list":[1,2,3,4,5,6]}
    return render(request, "index.html", context)


def about_page(request):
    return HttpResponse("<h1>About</h1>")


def contact_page(request):
	form=ContactForm(request.POST or None)
	if (form.is_valid()):
		print(form.cleaned_data)
		form=ContactForm()

	context={"title":"Contact us","form":form}
	return render(request,"form.html",context)
