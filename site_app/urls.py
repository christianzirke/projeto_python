from django.conf.urls import url

from .import views

urlpatterns = [
    url(r'^(?P<company_id>[0-9]+)/$', views.company_details, name='company_details')
]
