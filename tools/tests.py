from json import tool
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tool


class ToolTest(APITestCase):
  @classmethod
  def setUpTestData(cls):
    testuser1 = get_user_model().objects.create_user(
      username='testuser1', password='pass'
    )
    testuser1.save()

    test_tool = Tool.objects.create(
      name='hammer',
      owner=testuser1,
      description='Small hammer'
    )
    test_tool.save()

  def setUp(self):
    self.client.login(username='testuser1', password='pass')

  def test_tools_model(self):
    tool = Tool.objects.get(id=1)
    actual_owner = str(tool.owner)
    actual_name = str(tool.name)
    actual_description = str(tool.description)
    self.assertEqual(actual_owner, 'testuser1')
    self.assertEqual(actual_name, 'hammer')
    self.assertEqual(actual_description, 'Small hammer')
    
  def test_get_tool_list(self):
      url = reverse("tool_list")
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      tools = response.data
      self.assertEqual(len(tools), 1)
      self.assertEqual(tools[0]["name"], "hammer")

  def test_get_tool_by_id(self):
      url = reverse("tool_detail", args=(1,))
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      tool = response.data
      self.assertEqual(tool["name"], "hammer")

  def test_create_tool(self):
      url = reverse("tool_list")
      data = {"owner": 1, "name": "pliers", "description": "basic pliers"}
      response = self.client.post(url, data)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      tools = Tool.objects.all()
      self.assertEqual(len(tools), 2)
      self.assertEqual(Tool.objects.get(id=2).name, "pliers")

  def test_update_tool(self):
      url = reverse("tool_detail", args=(1,))
      data = {
          "owner": 1,
          "name": "hammer",
          "description": "Medium hammer",
      }
      response = self.client.put(url, data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      tool = Tool.objects.get(id=1)
      self.assertEqual(tool.name, data["name"])
      self.assertEqual(tool.owner.id, data["owner"])
      self.assertEqual(tool.description, data["description"])

  def test_delete_tool(self):
      url = reverse("tool_detail", args=(1,))
      response = self.client.delete(url)
      self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
      tools = Tool.objects.all()
      self.assertEqual(len(tools), 0)

  def test_authentication_required(self):
      self.client.logout()
      url = reverse("tool_list")
      response = self.client.get(url)
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
