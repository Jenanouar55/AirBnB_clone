#!/usr/bin/python3


import unittest
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):
    """Test User class"""

    def setUp(self):
        """Set up for user tests"""
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.user)
        self.assertIn("[User]", rep)
        self.assertIn("'email': 'test@example.com'", rep)
        self.assertIn("'password': 'password'", rep)
        self.assertIn("'first_name': 'John'", rep)
        self.assertIn("'last_name': 'Doe'", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(user_dict["created_at"], self.user.created_at.isoformat())
        self.assertEqual(user_dict["updated_at"], self.user.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        user_dict = self.user.to_dict()
        user_dict.pop("__class__", None)  # Remove __class__ key before passing to __init__
        new_user = User(**user_dict)
        self.assertEqual(new_user.email, self.user.email)
        self.assertEqual(new_user.password, self.user.password)
        self.assertEqual(new_user.first_name, self.user.first_name)
        self.assertEqual(new_user.last_name, self.user.last_name)
        self.assertEqual(new_user.created_at, self.user.created_at)
        self.assertEqual(new_user.updated_at, self.user.updated_at)

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'email': 'test@example.com',
            'password': 'password',
            'first_name': 'John',
            'last_name': 'Doe',
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = User(**n)
        self.assertEqual(new.email, 'test@example.com')
        self.assertEqual(new.password, 'password')
        self.assertEqual(new.first_name, 'John')
        self.assertEqual(new.last_name, 'Doe')
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
