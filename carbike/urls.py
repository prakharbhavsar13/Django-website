from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('news', views.news, name='news'),
    path('contact', views.contact, name='contact'),
    path('accessories', views.accessories, name='accessories'),
    path('bikes', views.bikes, name='bikes'),
path('cars', views.cars, name='cars'),
path('form', views.form, name='form'),
path('login', views.login, name='login'),
path('logout', views.logout, name='logout'),

]