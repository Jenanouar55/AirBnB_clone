#!/usr/bin/python3


import unittest
from datetime import datetime
from models.review import Review

class TestReview(unittest.TestCase):
    """Test Review class"""

    def setUp(self):
        """Set up for review tests"""
        self.review = Review()
        self.review.text = "Great place"

    def test_str_representation(self):
        """Test __str__ representation of the instance"""
        rep = str(self.review)
        self.assertIn("[Review]", rep)
        self.assertIn("'text': 'Great place'", rep)

    def test_to_dict_method(self):
        """Test to_dict method creates accurate dictionary representation"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["text"], self.review.text)
        self.assertEqual(review_dict["__class__"], "Review")
        self.assertEqual(review_dict["created_at"], self.review.created_at.isoformat())
        self.assertEqual(review_dict["updated_at"], self.review.updated_at.isoformat())

    def test_kwargs_initialization(self):
        """Test instance creation with dictionary representation"""
        review_dict = self.review.to_dict()
        review_dict.pop("__class__", None)  # Remove __class__ key before passing to __init__
        new_review = Review(**review_dict)
        self.assertEqual(new_review.text, self.review.text)
        self.assertEqual(new_review.created_at, self.review.created_at)
        self.assertEqual(new_review.updated_at, self.review.updated_at)

    def test_kwargs_one(self):
        """Test instantiation with kwargs"""
        n = {
            'text': 'Great place',
            'created_at': '2024-06-08T12:00:00.000000',
            'updated_at': '2024-06-08T12:00:00.000000'
        }
        new = Review(**n)
        self.assertEqual(new.text, 'Great place')
        self.assertEqual(new.created_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))
        self.assertEqual(new.updated_at, datetime.fromisoformat('2024-06-08T12:00:00.000000'))

if __name__ == '__main__':
    unittest.main()
