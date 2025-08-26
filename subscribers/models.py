from datetime import datetime
from pydantic import BaseModel


class SubOut(BaseModel):
    articles: str
    timestamp: datetime

class SubIn(BaseModel):
    articles: str
    timestamp: datetime




