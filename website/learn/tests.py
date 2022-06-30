from django.test import TestCase, Client

class TestBasicNonLoginViews(TestCase):

	def test_homepage(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'learn/index.html')