#!/usr/bin/python3
"""
This file por valida Unittest of class States
"""
from datetime import datetime
from models.review import Review
import unittest


class TestReview(unittest.TestCase):

    def setUp(self):
        """ Test for Setsup an instance of class city1 """
        self.review1 = Review()
        self.review2 = Review()
        self.review3 = Review()

    def tearDown(self):
        """ Test for Delete an instance of class city1 """
        del self.review1
        del self.review2
        del self.review3

    def test_argmts(self):
        """ Test for Delete an instance of class city1 """
        new = Review()
        self.assertEqual(new.place_id, "")
        self.assertEqual(new.user_id, "")
        self.assertEqual(new.text, "")
        
    def test_str(self):
        """ Test for validate str format in class city1"""
        string = "[{}] ({}) {}".format(self.review1.__class__.__name__,
                                       self.review1.id,
                                       self.review1.__dict__)
        self.assertEqual(str(self.review1), string)

    def test_equal(self):
        """ Test for validate id between both instances """
        user2 = Review()
        self.assertNotEqual(self.review1.id, user2.id)

    def test_validatearg(self):
        """ Test to validate argumets save in clas city"""
        self.review1.name = "Antioquia"
        self.assertTrue(hasattr(self.review1, "name"))
        self.assertIsInstance(self.review1.name, str)


if __name__ == '__main__':
    unittest.main()
