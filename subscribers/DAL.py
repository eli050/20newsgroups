from typing import Any
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from subscribers.models import SubOut, SubIn

class DALError(Exception):
    """Custom exception for Data Access Layer errors."""
    pass

class SubDAL:
    """Data Access Layer for subscriber articles."""
    def __init__(self, client:MongoClient, collection_name: str, db_name: str = "articles_db"):
        self.client = client
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    @staticmethod
    def _to_article_out(subscriber:dict[str, Any]) -> SubOut:
        """Convert a MongoDB document to a SubOut model."""
        return SubOut(
            articles=subscriber["articles"],
            timestamp=subscriber["timestamp"]
        )

    def add_articles(self, article_data: dict):
        """Add a new article to the collection."""
        try:
            self.collection.insert_one(article_data)
            return self._to_article_out(article_data)
        except PyMongoError as e:
            raise DALError(f"Error adding article: {e}")

    def get_articles(self):
       """Retrieve all articles from the collection."""
       try:
           return [self._to_article_out(sub) for sub in self.collection.find({})]
       except PyMongoError as e:
           raise DALError(f"Error retrieving articles: {e}")