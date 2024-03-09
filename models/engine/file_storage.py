#!/usr/bin/python3
"""Module FileStorage - handles serialization and deserialization of JSON."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serializes instances to JSON and deserializes JSON to instances."""

    __file_path = "file.json"  # JSON file path.
    __objects = {}  # Stores all objects by '<class name>.id'.

    def all(self):
        """Return the dictionary '__objects'."""
        return self.__objects

    def new(self, obj):
        """Set 'obj' in '__objects' with key '<obj class name>.id'."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize '__objects' to the JSON file specified by '__file_path'."""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file to '__objects' if '__file_path' exists."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for key, value in obj_dict.items():
                cls_name = value['__class__']
                cls_dict = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Place": Place,
                    "Amenity": Amenity,
                    "Review": Review,
                }
                self.__objects[key] = cls_dictcls_name
        except FileNotFoundError:
            pass
