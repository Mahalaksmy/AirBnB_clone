#!/usr/bin/python3
""" Testing for test base """
import unittest
from models.base_model import BaseModel
import models
from datetime import datetime


class Test_clase_m(unittest.TestCase):
	""" Test for class mode """
	Model = BaseModel()
	def test_none(self):
		
		self.assertIsNone(None, self.Model.__dict__.values())
	
	def test_BaseM(self):
		""" Test for testModel global """
		model_id = BaseModel()
		id = model_id.id
		self.assertNotEqual(id, self.Model.id)


if __name__ == '__main__':
	unittest.main()
