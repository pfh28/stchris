from django.shortcuts import render
from .models import Treasure, Hunt
from .serializers import TreasureSerializer, HuntSerializer
from rest_framework import permissions, viewsets

class TreasureViewSet(viewsets.ModelViewSet):
    queryset = Treasure.objects.all()
    serializer_class = TreasureSerializer


class HuntViewSet(viewsets.ModelViewSet):
    queryset = Hunt.objects.all()
    serializer_class = HuntSerializer