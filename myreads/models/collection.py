import uuid
from typing import List
from datetime import datetime

from myreads.models.book import Book


class Collection():
    id: uuid.UUID
    name: str
    books: List[Book]
    created_at: datetime
    updated_at: datetime

    def __init__(self, name: str, books_to_add: List[Book]):
        self.id = uuid.uuid4()
        self.name = name
        self.books = books_to_add
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def add_to_collection(self, book: Book) -> bool:
        pass

    def remove_from_collection(self, book: Book) -> bool:
        pass

    def rename_collection(self, new_name: str) -> bool:
        pass
