#!/usr/bin/python3
"""
Defines the State model, which inherits from BaseModel
"""
from .base_model import BaseModel


class State(BaseModel):
    """
    Blueprint for State objects.

    Attributes:
        name (str): The name of the state.
    """
    name: str = ""
