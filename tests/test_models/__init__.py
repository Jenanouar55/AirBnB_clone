#!/usr/bin/python3
"""
test_amenity
"""

import unittest
from datetime import datetime
import os
from models.amenity import Amenity
import models


class TestAmenity(unittest.TestCase):
    """Class for testing the Amenity model"""

    def test_instance_initialization(self):
        """Test instance creation and attributes"""
        my_model = Amenity()
        self.assertEqual(type(my_model), Amenity)
        d = datetime.now().replace(microsecond=0)
        self.assertEqual(my_model.created_at.replace(microsecond=0), d)
        self.assertEqual(my_model.updated_at.replace(microsecond=0), d)
        self.assertEqual(my_model.name, "")
        self.assertTrue(type(my_model.id) is str)
        my_model.name = "Betty"
        self.assertEqual(my_model.name, "Betty")

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        my_model = Amenity()
        rep = str(my_model)
        self.assertIn("[Amenity] (", rep)
        self.assertIn(")", rep)
        self.assertIn("'id': '", rep)
        self.assertIn("'created_at': ", rep)
        self.assertIn("'updated_at': ", rep)
        self.assertIn("'name': ''", rep)

    def test_str_representation_with_name(self):
        """Test __str__ representation of the instance with a name"""
        my_model = Amenity()
        my_model.name = "Betty"
        rep = str(my_model)
        self.assertIn("[Amenity] (", rep)
        self.assertIn(")", rep)
        self.assertIn("'id': '", rep)
        self.assertIn("'created_at': ", rep)
        self.assertIn("'updated_at': ", rep)
        self.assertIn("'name': 'Betty'", rep)

    def test_save_method(self):
        """Test save method updates 'updated_at' attribute"""
        my_model = Amenity()
        updated = my_model.updated_at
        my_model.save()
        self.assertNotEqual(updated, my_model.updated_at)

    def test_no_save_if_no_change(self):
        """Ensure 'updated_at' does not change without save"""
        my_model = Amenity()
        updated = my_model.updated_at
        my_model.name = "hi@hi"
        self.assertEqual(updated, my_model.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        my_model = Amenity()
        my_model_json = my_model.to_dict()
        self.assertEqual(my_model_json["__class__"], "Amenity")
        self.assertEqual(my_model_json["created_at"], my_model.created_at.isoformat())
        self.assertEqual(my_model_json["updated_at"], my_model.updated_at.isoformat())
        self.assertEqual(my_model_json["id"], my_model.id)
        self.assertEqual(my_model_json["name"], my_model.name)

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        my_model = Amenity()
        my_model_json = my_model.to_dict()
        my_new_model = Amenity(**my_model_json)
        self.assertTrue(type(my_new_model.id) is str)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(type(my_new_model), Amenity)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertTrue(my_model is not my_new_model)

    def tearDown(self):
        """Deallocating resources"""
        models.storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
