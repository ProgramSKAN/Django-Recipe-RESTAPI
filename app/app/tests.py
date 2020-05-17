#Django looks for any folder or file that begins with test for unit testing
#for testing: all the files,folders,test function must begin with 'test'

from django.test import TestCase
from app.calculator import add,subtract


class CalcTests(TestCase):
    #test function must begin with name 'test'
    def test_add_numbers(self): 
        """Test that two numbers are added together"""
        self.assertEqual(add(3,8),11)
    
    def test_subtract_numbers(self):
        """Test that values are subtracted and returned"""
        self.assertEqual(subtract(5,11),6)