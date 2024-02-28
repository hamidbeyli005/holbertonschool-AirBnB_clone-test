#!/usr/bin/python3


import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

        FileStorage._FileStorage__objects = {}
    
    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)
    
    def test_all(self):      
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save(self):
        self.storage.new(self.model)
        self.storage.save()

        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))
 
    def test_reload(self):
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        objs = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + self.model.id, objs)
