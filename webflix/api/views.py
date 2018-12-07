from rest_framework import generics
from series import models
from rest_framework import permissions
from . import serializers

class ListSeries(generics.ListCreateAPIView):
  queryset = models.Serie.objects.all()
  serializer_class = serializers.serieSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


