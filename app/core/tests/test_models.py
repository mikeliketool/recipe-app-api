from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.validators import ValidationError


class ModelTests(TestCase):
  def test_create_user_with_email_success(self):
    email = 'test@londonappdev.com'
    password = 'Testpass123'
    user = get_user_model().objects.create_user(email,
                                                password=password)

    self.assertEqual(user.email, email)
    self.assertTrue(user.check_password(password))

  def test_new_user_email_normalized(self):
    email = 'test@LONDONAPPDEV.com'
    user = get_user_model().objects.create_user(email, 'test123')

    self.assertEqual(user.email, email.lower())

  def test_new_user_invalid_email_none(self):
    with self.assertRaises(ValidationError):
      get_user_model().objects.create_user(None, 'test123')

  def test_new_user_invalid_email_empty(self):
    with self.assertRaises(ValidationError):
      get_user_model().objects.create_user('', 'test123')

  def test_new_user_invalid_email_format(self):
    with self.assertRaises(ValidationError):
      get_user_model().objects.create_user('test', 'test123')
