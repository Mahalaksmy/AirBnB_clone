#!/usr/bin/python3
"""
This file por valida Unittest of class Place
"""
from datetime import datetime
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):

    def setUp(self):
        """ Test for Setsup an instance of class Place() """
        self.place1 = Place()
        self.place2 = Place()
        self.place3 = Place()

    def tearDown(self):
        """ Test for Delete an instance of class Place() """
        del self.place1
        del self.place2
        del self.place3

    def test_str(self):
        """ Test for validate str format"""
        string = "[{}] ({}) {}".format(self.state1.__class__.__name__,
                                       self.state1.id,
                                       self.state1.__dict__)
        self.assertEqual(str(self.state1), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        user2 = Place()
        self.assertNotEqual(self.place1.id, user2.id)

    def test_validatearg(self):
        """ Test to validate argumets save """
        self.place1.name = "Antioquia"
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertIsInstance(self.state1.name, str)


if __name__ == '__main__':
    unittest.main()
