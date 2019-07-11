'''from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import PollList, PollDetail
from . import genericsviews
urlpatterns = [
    path("polls/", polls_list, name="polls_list"),
    path("polls/<int:pk>/", polls_detail, name="polls_detail"),
    path("apiview/",PollList.as_view(),name='PollList'),
    path("apiview/<int:pk>/", PollDetail.as_view(), name='PollList'),
   # path("apignview/",genericsviews.PollList.as_view()),
   # path("apigntestview/", genericsviews.PollDetail.as_view()),
    path("choices/", genericsviews.ChoiceList.as_view(), name="choice_list"),
    path("vote/", genericsviews.CreateVote.as_view(), name="create_vote"),


]'''

# urls.py
# ...
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')


urlpatterns = [
    # ...
]

urlpatterns += router.urls

# apiviews.py
# ...
from rest_framework import viewsets

from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer