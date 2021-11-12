#!/usr/bin/python3
"""
Class main BaseModel
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """Magic method or constructor"""
    """def __init__(self, *args, **kwargs):"""

    id = str(uuid.uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        """Inicialization of the attributes"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    setattr(self, key, value)
            # self.id = str(uuid.uuid4())
            # self.created_at = datetime.now()
            # self.updated_at = self.created_at
        else:
            self.id = type(self).id
            self.created_at = type(self).created_at
            self.updated_at = type(self).updated_at
            models.storage.new(self)

    def __str__(self):
        """This method return a string with the attributes"""
        return f"[{self.__class__.__name__ }] ({self.id}) {str(self.__dict__)}"

    def save(self):
        """updates the attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing
        all keys/values iniciliced"""
        dic = self.__dict__
        dic["__class__"] = self.__class__.__name__
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        return dic
