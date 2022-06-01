from rest_framework import generics
from .models import Tool
from .permissions import IsOwnerOrReadOnly
from .serializers import ToolSerializer


class ToolList(generics.ListCreateAPIView):
  queryset = Tool.objects.all()
  serializer_class = ToolSerializer


class ToolDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly, )
  queryset = Tool.objects.all()
  serializer_class = ToolSerializer
