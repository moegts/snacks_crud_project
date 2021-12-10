  
from django.test import TestCase 
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

# class SnacksCRUDTests(TestCase):
#     def setUp(self):
#         self.user = get_user_model().objects.create_user(
#             username = 'test',
#             email = 'test@test.test',
#             password = 'test@1234'
#         )
#         self.snack = Snack.objects.create(
#             title = 'Shawerma',
#             description  = '🟢',
#             purchaser = self.user
#         )
