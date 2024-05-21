#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """Serializes instances and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {key: obj.to_dict()
                        for key, obj in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """Deserializes JSON file to __objects(only(__file_path) exists)"""
        try:
            with open(self.__file_path, "r") as f:
                json_objects = json.load(f)
                for obj in json_objects.values():
                    self.new(BaseModel(**obj))
        except FileNotFoundError:
            pass
