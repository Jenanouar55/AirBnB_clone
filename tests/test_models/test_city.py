#!/usr/bin/python3


import unittest
from datetime import datetime
from models.city import City

class TestCity(unittest.TestCase):
    """Test City class"""

    def setUp(self):
        """Set up for city tests"""
        self.city = City()
        self.city.name = "San Francisco"

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.city)
        self.assertIn("[City]", rep)
        self.assertIn("'name': 'San Francisco'", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["name"], self.city.name)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["created_at"], self.city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], self.city.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        city_dict = self.city.to_dict()
        city_dict.pop("__class__", None)  # Remove __class__ key before passing to __init__
        new_city = City(**city_dict)
        self.assertEqual(new_city.name, self.city.name)
        self.assertEqual(new_city.created_at, self.city.created_at)
        self.assertEqual(new_city.updated_at, self.city.updated_at)

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'name': 'San Francisco',
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = City(**n)
        self.assertEqual(new.name, 'San Francisco')
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
