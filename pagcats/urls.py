from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.post_list, name='post_list' ),
    path('inicio', views.post_list, name='post_list' ),
    path('formulario', views.post_web2, name='post_web2' ),
    path('contacto', views.post_web3, name='post_web3' ),
    path('login',LoginView.as_view(), name='login_url'),
    path('registro',views.post_register, name='register_url'),
    #path('logout',),
]