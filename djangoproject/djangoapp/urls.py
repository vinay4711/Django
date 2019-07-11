from django.urls import path
from . import views,views1,model_view,views_vinay
from django.conf.urls import url
urlpatterns = [
    url(r'^test', views.hello,name='test'),
    url(r'^show', views.show, name='show'),
    url(r'^index', views.index, name='index'),
    url(r'^api', views1.index, name='index'),
    url(r'^student', model_view.student_index, name='student_index'),
    url(r'^Mobile', model_view.mobile_index, name='mobile_index'),
    url(r'^vinayinfo', views_vinay.vinayinfo, name='vinayinfo'),
    url(r'^emp', model_view.emp, name='emp'),





    ]