from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('login/', views.login_user, name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.register_user, name='register'),
    # path('detail/<int:pk>', views.customer_detail, name='detail'),
    # path('delete_record/<int:pk>', views.delete_record, name='delete_contact'),
    # path('add_contact/', views.add_contact, name='add_contact'),
    # path('update_contact/<int:pk>', views.update_contact, name='update_contact'),

]
