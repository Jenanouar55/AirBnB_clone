#!/usr/bin/python3
"""
Defines the User model, which inherits from BaseModel
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    Blueprint for a User object.

    Public attributes that will use FileStorage in the engine
    folder to manage serialization and deserialization of User.

    Attributes:
        email (str): The user's email address.
        password (str): The user's password.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
    """
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
