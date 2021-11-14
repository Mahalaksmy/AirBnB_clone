#!/usr/bin/python3
"""
This file por valida Unittest of class States
"""
from datetime import datetime
from models.state import State
import unittest


class TestState(unittest.TestCase):

    def setUp(self):
        """ Test for Setsup an instance of class State """
        self.state1 = State()
        self.state2 = State()
        self.state3 = State()

    def tearDown(self):
        """ Test for Delete an instance of class State """
        del self.state1
        del self.state2
        del self.state3

    def test_str(self):
        """ Test for validate str format"""
        string = "[{}] ({}) {}".format(self.state1.__class__.__name__,
                                       self.state1.id,
                                       self.state1.__dict__)
        self.assertEqual(str(self.state1), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        user2 = State()
        self.assertNotEqual(self.user1.id, user2.id)

    def test_validatearg(self):
        """ Test to validate argumets save """
        self.state1.name = "Antioquia"
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertIsInstance(self.state1.name, str)


if __name__ == '__main__':
    unittest.main()
