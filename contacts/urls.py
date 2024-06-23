from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('contact/<int:pk>', views.contact_list, name='contact'),
    path('create_contact/', views.create_contact, name='create_contact'),
    path('delete_contact/<int:pk>', views.delete_contact, name='delete_contact'),
<<<<<<< HEAD
    path('search_contact', views.search_contact, name='search_contact'),
=======
    path('contact/update/<int:pk>/', views.update_contact, name='update_contact'),
>>>>>>> origin/update

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)