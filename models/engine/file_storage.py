#!/usr/bin/python3
"""
File storage Class
"""
import json
import os


class FileStorage(object):
    """
    docstring for FileStorage
    """
    __file_path = "file.json"
    __objects = {}
    def __init__(self):
        """
        Initiliazer for the FileStorage
        Object
        """
        pass

    def all(self):
        """
        Returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__,
                             obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file
        (path: __file_path)
        """
        tempdict = {}
        if len(self.__file_path) > 0:
            for key, value in self.__objects.items():
                tempdict[key] = value.to_dict()
            with open(self.__file_path, 'w') as file:
                json.dump(tempdict, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
        """
        from models.base_model import BaseModel
        tempdict = {}
        newobjs = {}
        if len(self.__file_path) > 0 and os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as file:
                tempdict = (json.load(file))
            for key, value in tempdict.items():
                if value["__class__"] == "BaseModel":
                    newobjs[key] = BaseModel(**value)
            self.__objects = newobjs
