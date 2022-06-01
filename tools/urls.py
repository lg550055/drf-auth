from django.urls import path
from .views import ToolList, ToolDetail


urlpatterns = [
  path('', ToolList.as_view(), name='tool_list'),
  path('<int:pk>/', ToolDetail.as_view(), name='tool_detail')
]
