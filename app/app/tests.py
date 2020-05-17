#Django looks for any folder or file that begins with test for unit testing
#for testing: all the files,folders,test function must begin with 'test'

from django.test import TestCase
from app.calculator import add


class CalcTests(TestCase):
    #test function must begin with name 'test'
    def test_add_numbers(self): 
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)