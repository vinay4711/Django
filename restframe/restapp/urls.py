from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    #url(r'^api', views.EmployeeDetailsCBV.as_view(),name='EmployeeDetailsCBV'),
    #url(r'^api/(?P<id>\d+)/$', views.EmployeeDetailsCBV.as_view()),
    path('test/',views.update_model_detailsview,name='update_model_detailsview'),
    path('json/test1',views.JsonCBV.as_view(),name='JsonCBV'),
    path('json/test2',views.JsonCBV2.as_view(),name='JsonCBV2'),
    path('json/emp',views.EmployeeDetailsCBV.as_view(),name='EmployeeDetailsCBV'),
    path('se/emplist',views.EmployeeSealizedviewlist.as_view(),name='EmployeeSealizedviewlist'),
    path('se/Uplist', views.UpdateSealizedviewlist.as_view(), name='UpdateSealizedviewlist')


]