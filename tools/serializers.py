from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Tool


class ToolSerializer(serializers.ModelSerializer):
  class Meta:
    fields = ('id', 'name', 'owner', 'description', 'new', 'created')
    model = Tool
