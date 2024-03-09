#!/usr/bin/python3
"""Module State - provides the State class definition."""

from models.base_model import BaseModel


class State(BaseModel):
    """Represents a state with a name attribute."""

    name = ""  # Name of the state.
