#!/usr/bin/python3
import json
import os


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects


    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, 'w') as f:
            with open(self.__file_path, 'w') as f:
                temp = {}
                temp.update(FileStorage.__objects)
                for key, val in temp.items():
                    temp[key] = val.to_dict()
                    json.dump(temp, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value["__class__"]
                    cls = globals()[cls_name]
                    self.__objects[key] = cls(**value)
