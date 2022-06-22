from django.test import TestCase, Client

class TestBasicNonLoginViews(TestCase):

	def test_testhomepage(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'learn/index.html')