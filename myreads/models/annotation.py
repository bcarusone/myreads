import uuid
from typing import List, Optional
from datetime import datetime

from myreads.models.book import Book


class Annotation():
    id: uuid.UUID
    created_at: datetime
    updated_at: datetime
    book: Book
    page: int
    location: int
    quote: str
    note: str
    tags: Optional(List[str])

    def __init__(
        self,
        book: Book,
        quote: str,
        page: int = None,
        location: int = None,
        note: str = None,
        tags: List[str] = None
    ):
        self.id = uuid.uuid4()
        self.book = book
        self.quote = quote
        self.page = page
        self.location = location
        self.note = note
        self.tags = tags
