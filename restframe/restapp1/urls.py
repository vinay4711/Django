from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #url(r'^api', views.EmployeeDetailsCBV.as_view(),name='EmployeeDetailsCBV'),
    #url(r'^api/(?P<id>\d+)/$', views.EmployeeDetailsCBV.as_view()),
    path('test/',views.CompanySealizedviewlist.as_view(),name='CompanySealizedviewlist'),
    ]