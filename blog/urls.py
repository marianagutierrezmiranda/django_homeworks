from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page2', views.page2, name='page2'),
    path('article', views.article, name='article'),
    path('about', views.about, name='about'),
    path('emails', views.emails, name='emails'),
    
]
