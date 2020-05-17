from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse #to generate our api url


#rest_framework test helper tools
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL=reverse('user:create')

def create_user(**params):
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the user API (public)"""

    def setUp(self):
        self.client=APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload={
            'email':'user@gamil.com',
            'password':'user1234',
            'name':'test name'
        }
        res=self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_201_CREATED)
        user=get_user_model().objects.get(**res.data) #check id user object actually created.**res,data get dictionary object of reponse with id 
        self.assertTrue(user.check_password(payload['password'])) # check if password is true
        self.assertNotIn('password',res.data) #ensure password is not returned in the response

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload={'email':'user@gamil.com','password':'user1234'}
        create_user(**payload) #** unwinds payload

        res=self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """Test that the password must be more than 5 characters"""
        payload={'email':'user@gamil.com','password':'us'}
        res=self.client.post(CREATE_USER_URL,payload)

        self.assertEqual(res.status_code,status.HTTP_400_BAD_REQUEST)
        user_exists=get_user_model().objects.filter(
            email=payload['email']
            ).exists()
        self.assertFalse(user_exists) #if this email exists already return false.(since every test function refreshes database the same email used to create above wont conflict)
