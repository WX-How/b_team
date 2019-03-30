from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^add_t/$',views.add_t),
    url(r'^show_team/$',views.show_team),
    url(r'^update_t/(\d+)/$',views.update_t),
    url(r'^delete_t/(\d+)/$',views.delete_t),
    url(r'^add_p/(\d+)/$',views.add_p),
    url(r'^show_p/(\d+)/$',views.show_p),
    url(r'^update_p/(\d+)/$',views.update_p),
    url(r'^delete_p/(\d+)/$', views.delete_p),
]