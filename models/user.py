#!/usr/bin/python3
"""Module User - provides the User class definition."""

from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user with personal details."""

    email = ""  # Email address of the user.
    password = ""  # Password for user authentication.
    first_name = ""  # First name of the user.
    last_name = ""  # Last name of the user.
