import enum


class ReadingMethod(enum.Enum):
    """
    The method in which the book should be read.
    - Technical: A book that is technical in nature and will require
        significant brain power and focus to read.
    - Actionable: A book whose contents have actionable advice I
        want to apply to my life.
    - Interest: A book on a topic that I am interested in learning
        more about.
    - Leisure: A book I am reading purely for pleasure.
    """
    TECHNICAL = "technical"
    ACTIONABLE = "actionable"
    INTEREST = "interest"
    LEISURE = "leisure"
