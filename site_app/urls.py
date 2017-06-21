
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', auth_views.logout,   {'next_page': '/'}),
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^register/', views.register),
    url(r'^$', views.dashboard),
]
