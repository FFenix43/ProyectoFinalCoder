from django.urls import path
from LOTR.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home/', home, name="home"),
    path('about me/', AboutMe, name= "aboutme"),
    path('', login_request, name= "login"),
    path('signup/', signup_request, name= "signup"),
    path('logout/', LogoutView.as_view(), name="logout"),
    #path('indice/', indice, name= "indice"),
    path('blogs/', blogs, name= "blogs"),
    path('buscarBlogs', BuscarBlogs, name="buscarBlogs"),
    path('crearBlogs/', CrearBlog, name="crearBlogs"),
    path('editarPerfil/', editarPerfil, name="editarPerfil"),
    path('login/', login_request, name="login"),
]
