#!/usr/bin/python3
"""
BaseModel class.
"""
import uuid
from datetime import datetime as dt


class BaseModel(object):
    """docstring for BaseModel"""
    def __init__(self, *args, **kwargs):
        """
            The initializer for BaseModel
            Creates: id, created_at and updated_at
            Can also create a BaseModel from a dict
        """
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == 'created_at':
                    object.__setattr__(self,
                                       key,
                                       dt.fromisoformat(value))
                elif key == 'updated_at':
                    object.__setattr__(self,
                                       key,
                                       dt.fromisoformat(value))
                elif key == "__class__":
                    pass
                else:
                    object.__setattr__(self, key, value)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        Creates the String representation of BaseModel in
        the form of:
        [<class name>] (<self.id>) <self.__dict__>
        """
        s = "[{2}] ({0}) {1}".format(self.id, self.__dict__,
                                     self.__class__.__name__)
        return s

    def save(self):
        """
        Updates the updated_at to current time
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_rep = self.__dict__
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["updated_at"] = self.updated_at.isoformat()
        dict_rep["created_at"] = self.created_at.isoformat()
        return dict_rep
