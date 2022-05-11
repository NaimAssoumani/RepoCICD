import unittest
from app import app

class TestHello(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()
    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World!\n')
    def test_about(self):
        rv = self.app.get('/about')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'The about page')
    def test_project(self):
	rv = self.app.get('/projects/')
	self.assertEqual(rv.status, '200 OK')
	self.assertEqual(rv.data, b'The project page')
if __name__ == '__main__':
    unittest.main()
