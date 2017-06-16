from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^company/(?P<company_id>[0-9]+)/$', views.company_details, name='company_details'),
    url(r'^(?P<user_id>[0-9]+)/$', views.dashboard, name='dashboard')
]
