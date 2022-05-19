from django.urls import path,include
from django import urls
from messageapp import views
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from messageapp import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
  
   
    path('message/', views.MessageList.as_view()),
    path('message/<int:pk>/', views.MessageDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)


