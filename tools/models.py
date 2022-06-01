from pydoc import describe
from django.contrib.auth import get_user_model
from django.db import models


class Tool(models.Model):
  name = models.CharField(max_length=32)
  owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  description = models.CharField(max_length=256)
  new = models.BooleanField(default=False)
  created = models.DateField(auto_now_add=True)
  modified = models.DateField(auto_now=True)

  def __str__(self):
    return self.name
