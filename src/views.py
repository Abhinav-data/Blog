from django.shortcuts import render

from .models import BlogPost


def blog_post_detail_page(request,id):
	obj=BlogPost.objects.get(id=id)
	context={"object":obj}
	return render(request,"blog_post_detail.html",context)