#!/usr/bin/python3


import unittest
from datetime import datetime
from models.place import Place

class TestPlace(unittest.TestCase):
    """Test Place class"""

    def setUp(self):
        """Set up for place tests"""
        self.place = Place()
        self.place.name = "My place"

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.place)
        self.assertIn("[Place]", rep)
        self.assertIn("'name': 'My place'", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict["name"], self.place.name)
        self.assertEqual(place_dict["__class__"], "Place")
        self.assertEqual(place_dict["created_at"], self.place.created_at.isoformat())
        self.assertEqual(place_dict["updated_at"], self.place.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        place_dict = self.place.to_dict()
        place_dict.pop("__class__", None)  # Remove __class__ key before passing to __init__
        new_place = Place(**place_dict)
        self.assertEqual(new_place.name, self.place.name)
        self.assertEqual(new_place.created_at, self.place.created_at)
        self.assertEqual(new_place.updated_at, self.place.updated_at)

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'name': 'My place',
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = Place(**n)
        self.assertEqual(new.name, 'My place')
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
