#!/usr/bin/python3
"""
Class User
which inherits from
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Create attributes for user """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
