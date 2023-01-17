import enum


class Status(enum.Enum):
    """
    Current reading status for a book
    """
    TO_READ = "to read"
    DID_NOT_FINISH = "did not finish"
    PAUSED = "paused"
    READ = "read"
