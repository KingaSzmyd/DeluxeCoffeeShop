from django.urls import path
from . import views

urlpatterns = [
    path('', views.reviews, name='reviews'),
    path('<int:product_id>/', views.review_detail, name='review_detail')
]