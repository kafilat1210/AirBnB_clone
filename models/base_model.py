#!/usr/bin/python3
"""Module BaseModel - contains the BaseModel class definition."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """Defines common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            # Create instance from dictionary if kwargs is not empty.
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    # String to datetime conversion.
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    # Set attribute if key is not '__class__'.
                    setattr(self, key, value)
        else:
            # Assign default values if kwargs is empty.
            self.id = str(uuid.uuid4())  # Unique id assignment.
            self.created_at = datetime.now()  # Current datetime assignment.
            self.updated_at = self.created_at  # Same datetime as created_at.
            models.storage.new(self)

    def __str__(self):
        """String representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update 'updated_at' with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Dictionary representation of the BaseModel instance."""
        # Instance dictionary copy creation.
        new_dict = self.__dict__.copy()
        # Class name addition to the dictionary.
        new_dict["__class__"] = self.__class__.__name__
        # Datetime to string conversion in ISO format.
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

