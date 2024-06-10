#!/usr/bin/python3

import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Test Amenity class"""

    def setUp(self):
        """Set up for amenity tests"""
        self.my_model = Amenity()
        self.my_model.name = "Pool"

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.my_model)
        self.assertIn("[Amenity]", rep)
        self.assertIn("'name': 'Pool'", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        my_model_json = self.my_model.to_dict()
        self.assertEqual(my_model_json["name"], self.my_model.name)
        self.assertEqual(my_model_json["__class__"], "Amenity")
        self.assertEqual(my_model_json["created_at"], self.my_model.created_at.isoformat())
        self.assertEqual(my_model_json["updated_at"], self.my_model.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        my_model_json = self.my_model.to_dict()
        my_model_json.pop("__class__", None)  # Remove __class__ key before passing to __init__
        my_new_model = Amenity(**my_model_json)
        self.assertEqual(my_new_model.name, self.my_model.name)
        self.assertEqual(my_new_model.created_at, self.my_model.created_at)
        self.assertEqual(my_new_model.updated_at, self.my_model.updated_at)

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'name': 'Pool',
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = Amenity(**n)
        self.assertEqual(new.name, 'Pool')
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
