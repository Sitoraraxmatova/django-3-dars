from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.main,name="home"),
    path('about/',views.main1,name="about"),
    path('content/',views.main3,name="content"),
]
