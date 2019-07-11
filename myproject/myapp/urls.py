from django.urls import path
from . import views,student,durgaview
from django.conf.urls import url
urlpatterns = [
    url(r'^test', views.index,name='index'),
    url(r'^age',views.getAge,name='getAge'),
    path('leadname',views.LeadName,name='LeadName'),
    path('Apivinayinfo',durgaview.empdataview,name='empdataview'),
    url(r'^Apivinayinfojson', durgaview.empdataview_json, name='empdataview_json'),
    url(r'^apijsoncbv',views.jsonCBV.as_view(),name='jsonCBV'),
    #path('city',student.cityname,name='cityname'),
    #path('city', student.cityname, name='cityname')
   # path('strage'/age,student.studentage(),age=age)
]