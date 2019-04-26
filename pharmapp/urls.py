from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url(r'^$', views.profile,name='profile'),
    url('^profile/',views.pharmacy,name='pharmacy'),
    
    # url(r'^place/', views.location,name='locations'),
    # url(r'^image/(\d+)',views.single_images,name ='images')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)