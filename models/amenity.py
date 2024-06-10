#!/usr/bin/python3
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class representing an amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize the Amenity instance"""
        super().__init__(*args, **kwargs)
