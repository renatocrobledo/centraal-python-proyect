from django.db import models
from django.contrib.auth.models import User

class Serie(models.Model):

    CATEGORIES_CHOICES = (
        ('horror', 'Horror'),
        ('comedy', 'Comedy'),
        ('action', 'Action'),
        ('drama', 'Drama'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)

    def __str__(self):
      return self.name

class UserProfile(models.Model):
  user = models.OneToOneField(User, related_name="profile", on_delete=models.DO_NOTHING)
  role = models.CharField(max_length=50)

  def __str__(self):
    return f'{ self.user} > {self.role}'