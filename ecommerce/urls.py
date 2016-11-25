from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^order/$', views.order_form, name='order_form'),
    url(r'^order_execute/$', views.order_execute, name='order_execute'),
]