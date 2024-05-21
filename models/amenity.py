#!/usr/bin/python3
"""
Defines the Amenity model, which inherits from BaseModel
"""
from .base_model import BaseModel


class Amenity(BaseModel):
    """
    Blueprint for Amenity objects.

    Attributes:
        name (str): The name of the amenity.
    """
    name: str = ""
