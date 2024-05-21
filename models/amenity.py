#!/usr/bin/python3
"""
Defines the Amenity model, which inherits from BaseModel
"""
import models
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Inherits from BaseModel.
    """
    name = ""