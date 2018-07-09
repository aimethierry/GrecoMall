from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^category_create/$', views.category_create, name='category_create'),
    url(r'^product_create/$', views.product_create, name='product_create'),
    url(r'^all_order/$', views.all_order, name='all_order'),
    url(r'^all_product/$', views.all_product, name='all_product'),
    url(r'^detail/(?P<id>\d+)/$', views.order_detail, name='order_detail'),
    url(r'^product/edit/(?P<id>\d+)/$', views.product_edit, name='product_edit'),
]