#!/usr/bin/python3

import unittest
from datetime import datetime
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Test BaseModel class"""

    def setUp(self):
        """Set up for BaseModel tests"""
        self.model = BaseModel()

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.model)
        self.assertIn("[BaseModel]", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"], self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"], self.model.updated_at.isoformat())

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = BaseModel(**n)
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
