#!/usr/bin/python3
""" Test for the sub class User"""
import unittest
from models.user import User


class TestUser(unittest.TestLoader):
    """ Test for the sub class User"""

    def SetUp(self):
        """Sets up the class of the User"""
        self.u1 = User()
    
    def tearDown(self):
        """Tear down the class of the User"""
        del self.u1 
        
if __name__ == '__main__':
    unittest.main()