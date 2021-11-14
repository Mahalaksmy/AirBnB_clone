#!/usr/bin/python3
"""Class User
which inherits from
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class User Init"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
