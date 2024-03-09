#!/usr/bin/python3
"""Module Amenity - provides the Amenity class definition."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represents an amenity with a name attribute."""

    name = ""  # Name of the amenity.
