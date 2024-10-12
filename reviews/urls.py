from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('reviews/', views.review_list, name='review_list'),
    path('reviews/add/', views.add_review, name='add_review'),
]
