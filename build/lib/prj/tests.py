import unittest
from pyramid import testing


#my views
from prj import main
from prj.views import home,view_topic

class ViewTests(unittest.TestCase):

	
	def setUp(self):
		from webtest import TestApp
		self.testapp = TestApp(app)
		app = main({})
		
	
	def test_root(self):
		res = self.testapp.get('/', status=200)
		self.failUnless('Pyramid' in res.body)
