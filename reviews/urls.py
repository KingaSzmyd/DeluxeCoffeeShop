from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_posts, name='review_posts'),
    path('review_detail<slug:slug>/', views.review_detail, name='review_detail'),
]
