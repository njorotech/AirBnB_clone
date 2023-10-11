#!/usr/bin/python3
"""A module for a class that serializes instances
to a JSON file and deserializes JSON file to instances
"""

import os
import json


class FileStorage:
    """serializes instances to a JSON file and deserializes 
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""

        return self.__objects
    
    def get_objects(self):
        """get the objects values"""

        return self.__objects
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = obj['__class__']
        obj_id = obj['id']
        obj_key = class_name + '.' + obj_id
        self.__objects[obj_key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        with open(self.__file_path, "a") as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                self.__objects = json.load(f)
