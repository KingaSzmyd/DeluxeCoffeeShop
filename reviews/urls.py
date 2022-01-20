from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('<int:post_id>/', views.review_detail, name='review_detail')
]