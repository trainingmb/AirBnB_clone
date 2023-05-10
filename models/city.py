#!/usr/bin/python3
"""
City class.
"""
from models import storage
from models.base_model import BaseModel


class City(BaseModel):
    """
    Doc string for the City Class
    """
    def __init__(self, *args, **kwargs):
        """
        Public class attributes:
        state_id: string - empty string:
                  it will be the State.id
        name: string - empty string
        """
        self.state_id = ""
        self.name = ""
        if (kwargs is not None) and (len(kwargs) > 0):
            super(City, self).__init__(*args, **kwargs)
        else:
            super(City, self).__init__()
