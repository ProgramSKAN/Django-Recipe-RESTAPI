from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email as successful"""
        #django default user model expects username not gmail
        email='user@gmail.com'
        password='user1234'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))    
    
    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized(as the domain of email is case insensitive)"""
        email='user@GMAIL.COM'
        user=get_user_model().objects.create_user(email,'user1234')
        
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'user1234')
            # anything we run here should raise a value error,if not test fails.
    
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user=get_user_model().objects.create_superuser(
            'user#gmail.com',
            'user1234'
        )
        self.assertTrue(user.is_superuser) #comes from permissionMixin
        self.assertTrue(user.is_staff)