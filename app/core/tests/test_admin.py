from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse #allows us to generate URLs for Django admin page
from django.test import Client #allows us to make test requests to our application in a unit test

class AdminSiteTests(TestCase):

    def setUp(self):#setup function runs before every test
        self.client=Client()
        self.admin_user=get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='admin1234'
        )
        self.client.force_login(self.admin_user)
        self.user=get_user_model().objects.create_user(
            email='user@gmail.com',
            password='user1234',
            name='test full name'
        )
    
    def test_users_listed(self):
        """Test that users are listed on user page"""
        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)
