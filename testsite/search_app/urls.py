# search_app/urls.py

from django.contrib import admin
from django.urls import path  
from search_app import views  
  
urlpatterns = [
    path('', views.SearchView.as_view()), 
    path('admin/', admin.site.urls),
]