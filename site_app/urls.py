
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout),
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^register/', views.register),
    # url(r'^(?P<user_id>[0-9]+)/$', views.dashboard, name='dashboard'),
    url(r'^$', views.dashboard),
]
