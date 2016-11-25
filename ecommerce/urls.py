from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart_list/$', views.cart_list, name='cart_list'),
    url(r'^cart_add/(?P<product_id>[0-9]+)/$', views.cart_add, name='cart_add'),
    url(r'^cart_delete/(?P<product_id>[0-9]+)/$', views.cart_delete, name='cart_delete'),
    url(r'^cart_reset/$', views.cart_reset, name='cart_reset'),
    url(r'^order/$', views.order_form, name='order_form'),
    url(r'^order_execute/$', views.order_execute, name='order_execute'),
    url(r'^products/$', views.product_list, name='product_list'),
    url(r'^order_history/$', views.order_history, name='order_history'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),

]
