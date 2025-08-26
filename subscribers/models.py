from datetime import datetime
from pydantic import BaseModel


class SubOut(BaseModel):
    """Model for outputting subscriber articles."""
    articles: str
    timestamp: datetime

class SubIn(BaseModel):
    """Model for inputting subscriber articles."""
    articles: str
    timestamp: datetime




