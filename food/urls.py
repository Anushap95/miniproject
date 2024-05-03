from django.urls import path
from .import views


urlpatterns = [
   path("",views.Index,name="Index"),
   path('', views.home, name='home'),
   path('menu/', views.menu, name='menu'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
   path("detail/<int:id>/", views.detail,name="detail"),
   path('add/',views.create_item,name='create_item'),
]