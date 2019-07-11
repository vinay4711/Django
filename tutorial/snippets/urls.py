from django.urls import path
from . import views

urlpatterns = [
    path('snippets/', views.SnippetViewSet),
    path('snippets/<int:pk>/', views.UserViewSet),
]