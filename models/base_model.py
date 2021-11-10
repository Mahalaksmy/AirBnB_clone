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
    # name = None

    def __init__(self, id=None, created_at=None, updated_at=None, name=None):
        '''Inicialization'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at
        self.name = name
        # type(self).__name__ 

    def __str__(self):
        """ I do'nt understand """
        str = '[' + self.name + '] ' + '('
        # str += self.id + ')'
        # name.__class__.__name__
        return str

    def save(self):
        self.updated_at = datetime.now()

    # def to_dict(self):
    #     pass
