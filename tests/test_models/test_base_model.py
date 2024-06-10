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

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)


     def test_created_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

if __name__ == '__main__':
    unittest.main()
