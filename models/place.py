#!/usr/bin/python3
"""
Defines the Place model, which inherits from BaseModel
"""
from .base_model import BaseModel
from typing import List


class Place(BaseModel):
    """
    Blueprint for Place objects.

    Attributes:
        city_id (str): The ID of the city where the place is located.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The maximum number of guests can stay at the place.
        price_by_night (int): The price per night to stay at the place.
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        amenity_ids (List[str]):list of amenity IDs associated with the place.
    """
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: List[str] = None

    def __init__(self, *args, **kwargs):
        """
        Initialize a new Place instance.
        """
        super().__init__(*args, **kwargs)
        if self.amenity_ids is None:
            self.amenity_ids = []
