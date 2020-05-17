from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<id>', views.delete, name="delete")
]