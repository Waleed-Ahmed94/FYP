from django.conf.urls import url
from . import views
from django.urls import path



urlpatterns = [
    path('',views.home, name="home"),
    path('classify', views.classify, name="classify"),
    path('classifyurl', views.classify_url, name="classifyurl")
]