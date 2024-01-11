from django.urls import path
from . import views
urlpatterns = [
    path("" , views.home , name = "home"),
    path("course/<slug>" , views.course , name ="course"),
    path("<any>" , views.any , name = "any")
]