from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render,get_object_or_404
from .models import BlogPost
from .forms import BlogPostModelForm

def blog_post_list_view(request):
	qs=BlogPost.objects.all()
	context={'object_list':qs}
	return render(request,"blog/list.html",context)

@staff_member_required
#@login_required
def blog_post_create_view(request):
	form=BlogPostModelForm(request.POST or None)
	if(form.is_valid()):
		obj=form.save(commit=False)
		obj.user=request.user
		obj.save()
		form=BlogPostModelForm()
	context={'form':form}
	return render(request,"form.html",context)

def blog_post_detail_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	context={"object":obj}
	return render(request,"blog/detail.html",context)

def blog_post_update_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	form=BlogPostModelForm(request.POST or None,instance=obj)
	print(form.is_valid())
	if form.is_valid():
		form.save()
	context={'form':form,'title':f"Update {obj.title}"}
	return render(request,"form.html",context)

def blog_post_delete_view(request,slug):
	obj=get_object_or_404(BlogPost,slug=slug)
	context={"object":obj, 'form':None}
	return render(request,"blog/delete.html",context)
