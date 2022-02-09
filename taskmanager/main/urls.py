from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('create/', create, name='create'),
    path('delete/<int:id>/', delete, name='delete'),
    path('edit/<int:id>/', edit, name='edit'),
]