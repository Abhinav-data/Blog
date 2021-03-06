from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class BlogPost(models.Model):
	user	= models.ForeignKey(User,default=1,null=True, on_delete=models.SET_NULL)
	image	=models.ImageField(upload_to='image/',blank=True,null=True)
	title	=models.CharField(max_length=120)
	slug    =models.SlugField(unique=True)
	content	=models.TextField(null=True,blank=True)
	publish_date=models.DateTimeField(auto_now=False, auto_now_add=False,null=True,blank=True)
	timestamp=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-publish_date', '-updated','-timestamp']

	def get_absolute_url(self):
		return f"/blog/{self.slug}"

	def get_edit_url(self):
		return f"/blog/{self.slug}/update"

	def get_delete_url(self):
		return f"/blog/{self.slug}/delete"
