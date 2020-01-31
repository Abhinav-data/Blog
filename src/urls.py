from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static
from . import views

urlpatterns = [
	path('', views.blog_post_list_view),
	
    path('<str:slug>/', views.blog_post_detail_view),
    path('<str:slug>/delete', views.blog_post_delete_view),
    path('<str:slug>/update', views.blog_post_update_view),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)