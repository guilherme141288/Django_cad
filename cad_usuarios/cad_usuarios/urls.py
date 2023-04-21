

from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    path('', views.home , name='home'),
    
    #link usuarios
    path ('usuario/' , views.usuarios, name='listagem_usuarios')


]
