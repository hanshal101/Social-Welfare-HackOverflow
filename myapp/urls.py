from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.index, name='index'),
    path('createaccount', views.createaccount, name='createaccount'),
    path('login', views.login, name='login'),
    path('updates' , views.updates, name = ('updates')),
    path('chat', views.chat , name='chat'),
    path('chat', views.locate, name='locate'),

    
]