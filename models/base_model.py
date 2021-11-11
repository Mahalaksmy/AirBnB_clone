#!/usr/bin/python3
"""
Class main BaseModel
"""
import uuid
from datetime import date, time, datetime


class BaseModel:
    """Magic method or constructor"""
    """def __init__(self, *args, **kwargs):"""

    def __init__(self, name=None, my_number=None):
        """Inicialization of the attributes"""
        self.my_number = my_number
        self.name = name
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """This method return a string with the attributes"""
        stri = '[' + self.__class__.__name__ + '] ' + '('
        stri += self.id + ') ' + str(self.__dict__)
        return stri

    def save(self):
        """updates the attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values iniciliced"""
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
