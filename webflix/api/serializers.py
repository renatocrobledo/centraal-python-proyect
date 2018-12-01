from rest_framework import serializers
from series import models

class serieSerializer(serializers.ModelSerializer):
  class Meta:
    fields = (
      'name',
      'release_date',
      'rating',
      'category',
    )
    model = models.Serie