from django.urls import path

from . import views

urlpatterns = [
    path('indexapi/', views.index, name='index'),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('indexhtml',views.index_html,name='index_html'),
    path('qtype/<int:question_id>', views.question_Type_byid, name='question_Type_byid'),


]