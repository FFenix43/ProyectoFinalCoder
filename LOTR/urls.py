from django.urls import path
from LOTR.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name="home"),
    path('about me/', AboutMe, name= "aboutme"),
    path('login/', login_request, name= "login"),
    path('signup/', signup_request, name= "signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    #path('indice/', indice, name= "indice"),
    path('blogs/', BlogsList.as_view(), name= "blogs"),
    path('buscarBlogs', BuscarBlogs, name="buscarBlogs"),
    path('crearBlogs/', CrearBlog, name="crearBlogs"),
    path('verblogs/<id>', VerBlogs, name="VerBlogs"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    #path('login/', login_request, name="login"),
    path('agregarAvatar/', obtenerAvatar, name="avatar"),
    path('aboutme/', aboutme, name="aboutme"),
    path('chat/', chat, name="chat"),

    path('prueba/', prueba, name="prueba"),
]
