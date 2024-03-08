#!/usr/bin/python3
"""
BaseModel Module
This module provides the BaseModel class, which is the cornerstone for all
future classes in our project.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class is the foundation for all other higher-level classes
    that will be created later. It encapsulates common attributes and methods
    that will be inherited by other subclasses.
    """

    def __init__(self, *args, **kwargs):
        """
        The constructor for BaseModel, responsible for initializing new
        instances. If 'kwargs' is provided, it recreates an instance from a
        dictionary representation of a BaseModel.
        """
        if kwargs:
            # Rebuild from dictionary if 'kwargs' is provided
            for key, value in kwargs.items():
                if key in ["created_at", "updated_at"]:
                    # Convert string to datetime for these keys
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    # Set all other attributes directly
                    setattr(self, key, value)
        else:
            # Create new instance with unique ID and timestamps
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the BaseModel instance, including the class
        name, id, and dictionary of the instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        Updates 'updated_at' with the current datetime to reflect the last
        modification time.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Generates a dictionary representation of the instance, which includes
        all attributes. Useful for serialization purposes.
        """
        new_dict = self.__dict__.copy()
        # Add class name to the dictionary
        new_dict["__class__"] = self.__class__.__name__
        # Convert datetime objects to strings in ISO format
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
