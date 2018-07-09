from django.conf.urls import url
from orders import views


urlpatterns = [
    url(r'^all/(?P<id>\d+)/$', views.allorder, name="allorder"),
    url(r'^create/$', views.order_create, name="create"),
   
]