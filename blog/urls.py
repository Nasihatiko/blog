from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_lists, name='posts_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url')
]