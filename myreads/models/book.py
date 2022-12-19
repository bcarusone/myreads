import uuid
from typing import List
from datetime import datetime, date

from myreads.models.category import Category
from myreads.models.format import Format
from myreads.models.genre import Genre
from myreads.models.source import Source
from myreads.models.annotation import Annotation
from myreads.models.update import Update
from myreads.models.reading_method import ReadingMethod
from myreads.models.status import Status
from myreads.models.collection import Collection


class Book():
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    title: str
    subtitle: str
    author: List[str]
    publish_date: date
    publish_location: str
    num_pages: int
    public_rating: float
    num_ratings: int
    citation: str
    series: str
    num_in_series: int
    narrator: str
    description: str
    isbn10: str
    isbn13: str
    cover: str
    category: Category
    genre: List[Genre]
    rating: int
    review: str
    current_page: int
    current_location: int
    percent_read: float
    reading_method: ReadingMethod
    priority: int
    date_started: date
    date_completed: date
    summary: str
    annotations: List[Annotation]
    source: Source
    status: Status
    format: Format
    updates: List[Update]
    collections: List[Collection]

    def __init__(self):
        pass

    def get_citation(self):
        pass

    def start(self):
        pass

    def update_status(self):
        pass

    def add_update(self):
        pass

    def complete(self):
        pass
