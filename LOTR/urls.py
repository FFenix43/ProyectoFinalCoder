from django.urls import path
from LOTR.views import *


urlpatterns = [
    path('home/', home, name="home"),
    path('about me/', AboutMe, name= "aboutme"),
    path('', login, name= "login"),
    path('signup/', signup, name= "signup"),
    path('indice/', indice, name= "indice"),
    path('blogs/', blogs, name= "blogs"),
]
