#!/usr/bin/python3

"""Defines the Review model, which inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
