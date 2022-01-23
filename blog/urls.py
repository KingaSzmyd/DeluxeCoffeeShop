from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_posts, name='blog_posts'),
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<slug:slug>/', views.edit_post, name='edit_post'),
    path('delete_post/<slug:slug>/', views.delete_post,
         name='delete_post'),
    path('<slug:slug>/', views.blog_detail, name='blog_detail'),
]
