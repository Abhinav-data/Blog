from django import forms
from .models import BlogPost

class BlogPostForm(forms.Form):
	title=forms.CharField()
	slug=forms.SlugField()
	content=forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model=BlogPost
		fields=['title','image','slug','content','publish_date']

	# def clean_title(self,*args,**kargs):
	# 	instance=self.instance
	# 	title=self.cleaned_data.get('title')
	# 	qs=BlogPost.objects.filter(title__iexact=title)
	# 	if(instance is not None):
	# 		qs=qs.exclude(pk=instance.pk)
	# 	if(len(qs)!=0):
	# 		raise forms.ValidationError("This title is already take")
	# 	return title