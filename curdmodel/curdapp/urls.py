from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #url(r'^api', views.EmployeeDetailsCBV.as_view(),name='EmployeeDetailsCBV'),
    #url(r'^api/(?P<id>\d+)/$', views.EmployeeDetailsCBV.as_view()),
]
#url(r'^article/(\d+)/', 'viewArticle', name = 'article'),)