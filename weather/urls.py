from django.contrib import admin
from django.urls import path,include
from weather import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<int:n>',views.delete,name='delete'),
    path('imperial',views.imperial,name='imperial')
]
