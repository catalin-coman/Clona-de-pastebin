from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'textbin'

urlpatterns = [
    # userlist page
    path('', views.HomeView.as_view(), name='home'), 

    # textlist page
    url(r'^(?P<pk>[0-9]+)/$', views.TextsView.as_view(), name='textlist'),

    #create user
    url(r'user/add/$', views.UserCreate.as_view(), name='user-add'),

    #create text
    url(r'text/add/$', views.TextCreate.as_view(), name='text-add'),

    #edit text
    url(r'text/(?P<pk>[0-9]+)/$', views.TextUpdate.as_view(), name='text-edit'),

    #delete text
    url(r'text/delete/(?P<pk>[0-9]+)/$', views.TextDelete.as_view(), name='text-delete'),
]
