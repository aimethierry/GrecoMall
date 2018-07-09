from django.conf.urls import url
from product import views


urlpatterns = [
    url(r'^$', views.product_list, name="product_list"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    url(r'^(?P<id>\d+)/$', views.category_detail, name='category_detail'),

]