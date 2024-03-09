#!/usr/bin/python3
"""Module City - provides the City class definition."""

from models.base_model import BaseModel


class City(BaseModel):
    """Represents a city with related information."""

    state_id = ""  # Identifier of the state a city belongs to.
    name = ""  # Name of the city.
