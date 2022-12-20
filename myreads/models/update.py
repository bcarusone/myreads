import uuid
from typing import List, Optional
from datetime import datetime

from myreads.models.book import Book
from myreads.models.annotation import Annotation


class Update():
    id: uuid.UUID
    created_at: datetime
    book: Book
    current_page: int
    annotations: List[Annotation]

    def __init__(
        self,
        book: Book,
        current_page: int,
        annotations: Optional(List[Annotation]) = None
    ):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.book = book
        self.current_page = current_page
        self.annotations = annotations
