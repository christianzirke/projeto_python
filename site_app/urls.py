
from django.conf.urls import url
from django.contrib.auth import views as auth_views

from .import views

urlpatterns = [
    url(r'^login/$', auth_views.login),
    url(r'^logout/$', auth_views.logout,   {'next_page': '/'}),
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^register/$', views.register),
    url(r'^follow_company/(?P<company_id>[0-9]+)/?$', views.follow_company),
    url(r'^unfollow_company/(?P<company_id>[0-9]+)/?$', views.unfollow_company),
    url(r'^password_reset/$', auth_views.password_reset, {"template_name":"registration/password_reset_form.html"}),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^$', views.dashboard),
]
