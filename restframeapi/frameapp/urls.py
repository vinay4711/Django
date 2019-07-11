from django.urls import path
from . import views
from django.conf.urls import url
#prajwalview
urlpatterns = [
    #url(r'^api', views.EmployeeDetailsCBV.as_view(),name='EmployeeDetailsCBV'),
    #url(r'^api/(?P<id>\d+)/$', views.EmployeeDetailsCBV.as_view()),
    path('test/',views.MusicianListView.as_view(),name='MusicianListView'),
    url(r'^api/musicians/(?P<pk>\d+)/$', views.MusicianView.as_view()),
    url(r'^api/pri',views.prajwalview.as_view(),name='prajwalview'),
    ]