#!/usr/bin/python3
"""
This file por valida Unittest of class States
"""
from datetime import datetime
from models.city import City
import unittest


class TestCity(unittest.TestCase):

    def setUp(self):
        """ Test for Setsup an instance of class city1 """
        self.city1 = City()
        self.city2 = City()
        self.city3 = City()

    def tearDown(self):
        """ Test for Delete an instance of class city1 """
        del self.city1
        del self.city1
        del self.city1

    def test_str(self):
        """ Test for validate str format in class city1"""
        string = "[{}] ({}) {}".format(self.city1.__class__.__name__,
                                       self.city1.id,
                                       self.city1.__dict__)
        self.assertEqual(str(self.city1), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        user2 = City()
        self.assertNotEqual(self.city1.id, user2.id)

    def test_validatearg(self):
        """ Test to validate argumets save in clas city"""
        self.city1.name = "Antioquia"
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertIsInstance(self.city1.name, str)


if __name__ == '__main__':
    unittest.main()
