import enum


class Source(enum.Enum):
    """
    The source of the book- from the library, personally owned, or
    borrowed from a friend.
    """
    LIBRARY = "library"
    OWN = "own"
    BORROWED = "borrowed"
