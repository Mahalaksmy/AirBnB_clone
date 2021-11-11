#!/usr/bin/python3
"""
Class principal
"""

import uuid
from datetime import date, time, datetime


class BaseModel:
    """
    Magic method or constructor
    """
    """def __init__(self, *args, **kwargs):"""

    def __init__(self, id=None, created_at=None, updated_at=None):
        """Inicialization of the attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        #self.name = name

    def __str__(self):
        """This method return a string with the attributes"""
        """stri = '[' + self.__class__.__name__ + '] ' + '('
        stri += self.id + ') ' + str(self.__dict__)"""

        return f"[{self.__class__.__name__ }] ({self.id} {str(self.__dict__)}) "

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
