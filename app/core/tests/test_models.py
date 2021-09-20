from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creat user with email successful'''
        email = "moha@moha.com"
        password ="moha"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    def test_new_user_email_normelized(self):
        '''Test email for new user is normalized'''
        email = "moha@MOHA.COM"
        password ="moha"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None,password='moha')

    def test_create_new_superuser(self):
        '''Test create a new superuser'''
        user = get_user_model().objects.create_superuser(email='moha@moha.com',password='moha')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


    