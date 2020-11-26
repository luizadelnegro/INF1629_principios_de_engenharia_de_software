from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views
#from frequency.views import  UserHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
 
 
 