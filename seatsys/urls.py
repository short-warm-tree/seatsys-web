"""seatsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from login import views as login_views
from stuinfo import views as stuinfo_views
from seat import views as seat_views
from weixin import views as weixin_views
from timing import views as timing_views
urlpatterns = [
    url(r'^$',login_views.index),
    url(r'^login/$',login_views.checkin,name='login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stuinfo/',stuinfo_views.show,name='show'),
    url(r'^login/showfreeseat/$',seat_views.showfreeseat,name='showfreeseat'),
    url(r'^login/showcredit/$',stuinfo_views.showcredit,name='showcredit'),
    url(r'^logout/$',login_views.logout,name='logout'),
    url(r'^logout/showseat/$',seat_views.showseat,name='showseat'),
    url(r'^seat/leave/$',seat_views.leave,name='leave'),
    url(r'^seat/seatinfo/$',seat_views.seatinfo),
    url(r'^seat/order',seat_views.order),
    url(r'^seat/signout',seat_views.signout),
    url(r'^weixin/$',weixin_views.index),
    url(r'timing/$',timing_views.index),
    url(r'^gettoken/$',timing_views.auto_get_token),
]
