#!/usr/bin/python3
"""
Place class.
"""
from models import storage
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Doc string for the Place Class
    """
    def __init__(self, *args, **kwargs):
        """
        Public class attributes:
            city_id: string
                empty string: it will be the City.id
            user_id: string
                empty string: it will be the User.id
            name: string
                empty string
            description: string
                empty string
            number_rooms: integer
                0
            number_bathrooms: integer
                0
            max_guest: integer
                0
            price_by_night : integer
                0
            latitude: float
                0.0
            longitude: float
                0.0
            amenity_ids: list of string
                empty list: it will be the list of
                Amenity.id later
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longtitude = 0.0
        self.amenity_ids = []
        if (kwargs is not None) and (len(kwargs) > 0):
            super(Place, self).__init__(*args, **kwargs)
        else:
            super(Place, self).__init__()
