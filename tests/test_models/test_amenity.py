#!/usr/bin/python3
"""
This file por valida Unittest of class States
"""
from datetime import datetime
from models.amenity import Amenity
import unittest


class TestState(unittest.TestCase):

    def setUp(self):
        """ Test for Setsup an instance of class State """
        self.amenity1 = Amenity()
        self.amenity2 = Amenity()
        self.amenity3 = Amenity()

    def tearDown(self):
        """ Test for Delete an instance of class State """
        del self.amenity1
        del self.amenity2
        del self.amenity3

    def test_test_argmts(self):
        """ Test arguments of the class"""
        new = Amenity(name="Holberton",
                      first_name="Betty",
                      last_name="Holberton",
                      email="airbnb@holbertonschool.com",
                      password="root",
                      created_at="2021-11-12T20:21:42.356737",
                      updated_at="2021-11-12T20:21:42.356737",
                      id="0e5ad480-ebf5-4bc8-9771-2a0e8daff36d")
        self.assertEqual(new.name, "Holberton")

    def test_str(self):
        """ Test for validate str format"""
        string = "[{}] ({}) {}".format(self.amenity1.__class__.__name__,
                                       self.amenity1.id,
                                       self.amenity1.__dict__)
        self.assertEqual(str(self.amenity1), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity1.id, amenity2.id)

    def test_validatearg(self):
        """ Test to validate argumets save """
        self.amenity1.name = "Antioquia"
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertIsInstance(self.amenity1.name, str)


if __name__ == '__main__':
    unittest.main()
