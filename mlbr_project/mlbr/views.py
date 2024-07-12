from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .serializers import TeamSerializer, PlayerSerializer
from .models import Team, Player

def teams_list(request):
    teams = Team.objects.all().values('name', 'location', 'division')
    teams_list = list(teams)
    return JsonResponse(teams_list, safe=False)

class TeamList(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
