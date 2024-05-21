#!/usr/bin/python3
"""
Defines the Review model, which inherits from BaseModel
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Blueprint for Review objects.

    Attributes:
        user_id (str): The ID of the user who wrote the review.
        place_id (str): The ID of the place being reviewed.
        text (str): The text content of the review.
    """
    user_id: str = ""
    place_id: str = ""
    text: str = ""
