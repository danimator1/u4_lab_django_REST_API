from django.urls import path
from .views import teams_list, TeamList, TeamDetail, PlayerList, PlayerDetail
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('teams/simple/', teams_list, name='teams_list'),
    path('teams/', TeamList.as_view(), name='team_list'),
    path('teams/<int:pk>/', TeamDetail.as_view(), name='team_detail'),
    path('players/', PlayerList.as_view(), name='player_list'),
    path('players/<int:pk>/', PlayerDetail.as_view(), name='player_detail'),
]