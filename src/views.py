from django.shortcuts import render,get_object_or_404
from .models import BlogPost


def blog_post_list_view(request):
	qs=BlogPost.objects.all()
	context={'object_list':qs}
	return render(request,"blog/list.html",context)


def blog_post_create_view(request):
	context={'form':None}
	return render(request,"blog/create.html",context)

def blog_post_detail_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	context={"object":obj}
	return render(request,"blog/detail.html",context)

def blog_post_update_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	context={"object":obj}
	return render(request,"blog/update.html",context)

def blog_post_delete_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	context={"object":obj, 'form':None}
	return render(request,"blog/delete.html",context)
