
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns=[ 
  url(r'^$',views.home,name='home'),   
  url(r'^request/$', views.post_request, name='post_request'),
  url(r'^view_pharmacy', views.view_pharmacy,name='view_pharmacy'),
  url(r'^create_pharmacy/',views.create_pharmacy,name='create_pharmacy'), 
  url(r'^create_medecines/',views.create_medecines,name='create_medecines'),
  url(r'^create_insurances/',views.create_insurances,name='create_insurances'),
  url(r'^search_pharmacy/',views.search_pharmacy,name='search_pharmacy'),
 
     
]  
 

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)