import enum


class Format(enum.Enum):
    """
    The available format of the book.
    """
    EBOOK = "ebook"
    AUDIOBOOK = "audiobook"
    PAPERBACK = "paperback"
    HARDCOVER = "hardcover"
