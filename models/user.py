#!/usr/bin/python3
"""
User class.
"""
from models import storage
from models.base_model import BaseModel


class User(BaseModel):
    """
    doc string for the User Class
    """
    def __init__(self, *args, **kwargs):
        """
        Initilizer for User
        Public class attributes:
            email: string - empty string
            password: string - empty string
            first_name: string - empty string
            last_name: string - empty string
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        if (kwargs is not None) and (len(kwargs) > 0):
            super(User, self).__init__(*args, **kwargs)
        else:
            super(User, self).__init__()
