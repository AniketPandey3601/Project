from premalifescience.settings import STATICFILES_DIRS, STATIC_URL
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from . import views

     
admin.site.site_header="prema life sciences"
admin.site.site_title="welcome to our Dashboard"
admin.site.index_title="welcome to this portal"
urlpatterns = [
     path('',views.Home, name='Home'),
     path('AboutUS',views.AboutUS, name='AboutUS'),
     path('Contact',views.Contact, name='Contact'),
     path('products/<str:slug>',views.PRODUCTS, name='PRODUCTS'),
     path('products',views.PRODUCTSHOME, name='PRODUCTSHOME'),
     path('covid',views.COVID19SOLUTIONSHOME, name='COVID19SOLUTIONSHOME'),
     
     path('covid/<str:slug>',views.COVID19SOLUTIONS, name='COVID19SOLUTIONS'),
     path('media',views.MEDIA, name='MEDIA'),
     path('career',views.CAREER, name='CAREER')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)