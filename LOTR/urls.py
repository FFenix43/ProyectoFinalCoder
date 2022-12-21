from django.urls import path
from LOTR.views import *


urlspatterns = [
    path('', inicio),
    path('about me/', AboutMe),
]
