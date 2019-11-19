from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('inicio', views.post_list, name='post_list' ),
    path('formulario', views.post_web2, name='post_web2' ),
    path('contacto', views.post_web3, name='post_web3' ),
]