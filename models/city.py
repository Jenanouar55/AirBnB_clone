#!/usr/bin/python3
"""
Defines the City model, which inherits from BaseModel
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    Blueprint for City objects.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id: str = ""
    name: str = ""
