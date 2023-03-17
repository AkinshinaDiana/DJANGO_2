from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name = 'main'),
    path('about/', views.about, name = 'about'),
    path('services/', views.services, name = 'services'),
    path('ourworks/', views.ourworks, name = 'ourworks'),
    path('contacts/', views.contacts, name = 'contacts'),
]
