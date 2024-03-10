#!/usr/bin/python3
"""Module Review - provides the Review class definition."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represents a review by storing ids and review text."""

    place_id = ""  # ID of the place being reviewed.
    user_id = ""  # ID of the user who wrote the review.
    text = ""  # Content of the review.
