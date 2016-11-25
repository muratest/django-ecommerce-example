from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart_list/$', views.cart_list, name='cart_list'),
    #url(r'^cart_add/(?<>)$', views.cart_list, name='cart_list'),
    #url(r'^cart_delete/$', views.cart_list, name='cart_list'),
    #url(r'^cart_reset/$', views.cart_list, name='cart_list'),
    url(r'^order/$', views.order_form, name='order_form'),
    url(r'^order_execute/$', views.order_execute, name='order_execute'),
    url(r'^products/$', views.product_list, name='product_list'),
]
