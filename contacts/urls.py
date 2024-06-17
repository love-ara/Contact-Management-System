from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('contact/<int:pk>', views.customer_contact, name='contact'),
    path('create_contact/', views.create_contact, name='create_contact'),
]
