from django.urls import path
from . import views
from .forms import PostForm

urlpatterns=[
   # path('',views.post_list,name='post_list'),
    path('', views.post_new, name='post_new')
]