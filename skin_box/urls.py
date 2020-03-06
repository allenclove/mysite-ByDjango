from django.urls import path
from . import views

# start with blog
urlpatterns = [
    #http://localhost:8000/blog/
    path('', views.lolskin, name='lolskin'),
    path('get_access_token/', views.get_access_token, name='get_access_token'),
]
