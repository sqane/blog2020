from django.urls import path
from .views import main_page,new_post

app_name = 'main'

urlpatterns = [
    path('', main_page, name='blog'),
    path('new_post/', new_post, name='new_post'),
]
