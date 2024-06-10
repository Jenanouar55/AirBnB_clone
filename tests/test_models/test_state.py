#!/usr/bin/python3


import unittest
from datetime import datetime
from models.state import State

class TestState(unittest.TestCase):
    """Test State class"""

    def setUp(self):
        """Set up for state tests"""
        self.state = State()
        self.state.name = "California"

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.state)
        self.assertIn("[State]", rep)
        self.assertIn("'name': 'California'", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict["name"], self.state.name)
        self.assertEqual(state_dict["__class__"], "State")
        self.assertEqual(state_dict["created_at"], self.state.created_at.isoformat())
        self.assertEqual(state_dict["updated_at"], self.state.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        state_dict = self.state.to_dict()
        state_dict.pop("__class__", None)  # Remove __class__ key before passing to __init__
        new_state = State(**state_dict)
        self.assertEqual(new_state.name, self.state.name)
        self.assertEqual(new_state.created_at, self.state.created_at)
        self.assertEqual(new_state.updated_at, self.state.updated_at)

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'name': 'California',
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = State(**n)
        self.assertEqual(new.name, 'California')
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
