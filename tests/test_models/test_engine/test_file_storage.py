#!/usr/bin/python3
"""
All test for file storage
"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import models


class Test_FS(unittest.TestCase):
    """Test for FileStorage """
    Fs = FileStorage()

    def test_basic(self):
        """Tests for FS Class"""
        dicti = self.Fs.class_dict
        self.assertIsInstance(dicti, dict)

    def test_doc_FileStorage(self):
        """test doc for class"""
        self.assertIsNotNone(self.Fs.__doc__)

    def test_doc_FileStorage_all(self):
        """ Test doc for all method """
        self.assertIsNotNone(self.Fs.all.__doc__)

    def test_FS_all(self):
        """ Test for all method """
        self.Fs.all()
        with self.assertRaises(TypeError):
            self.Fs.all("PYTHON")

    def test_FS_new(self):
        """ Test for new method"""
        with self.assertRaises(TypeError):
            self.Fs.new()

    def test_doc_FileStorage_new(self):
        """ Test for new method """

        self.assertIsNotNone(self.Fs.new.__doc__)

    def test_save(self):
        """ Test for save method """
        self.assertIsNotNone(self.Fs.save.__doc__)

    def test_reload(self):
        """ Test for reload method """
        self.assertIsNotNone(self.Fs.reload.__doc__)

if __name__ == '__main__':
    unittest.main()
