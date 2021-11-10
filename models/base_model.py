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
    def __init__(self, id, created_at, updated_at):

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at

    def __str__(self):
        """ I do'nt understand """
        pass

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        pass
