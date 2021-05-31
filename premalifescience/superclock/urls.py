from django.urls import path
from . import views

urlpatterns = [
     path("clock",views.index, name='index'),

]