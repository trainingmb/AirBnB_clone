#!/usr/bin/python3
"""
Review class.
"""
from models import storage
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Doc string for the Review Class
    """
    def __init__(self, *args, **kwargs):
        """
        Public class attributes:
        place_id: string - empty string:
            it will be the Place.id
        user_id: string - empty string:
            it will be the User.id
        text: string - empty string
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        if (kwargs is not None) and (len(kwargs) > 0):
            super(Review, self).__init__(*args, **kwargs)
        else:
            super(Review, self).__init__()
