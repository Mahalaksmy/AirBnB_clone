#!/usr/bin/python3
"""Class FileStorage"""
import os
import json
from models.base_model import BaseModel


class FileStorage():
    """Class FileStorage"""

    __file_path = './file.json'
    __objects =  {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        save_dic = {}
        for k, v in self.__objects.items():
            save_dic[k] = v.to_dict()

        with open(self.__file_path, "w") as write_file:
            json.dump(save_dic, write_file)

    def reload(self):
        """ eserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as write_file:
                save_dic = json.load(write_file)
                for v in save_dic.values():
                    self.new(eval(v["__class__"])(**v))
