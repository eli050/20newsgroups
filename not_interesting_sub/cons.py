from pymongo import MongoClient
from datetime import datetime
from subscribers.DAL import SubDAL
from subscribers.consumer import Consumer


URI = "mongodb://mongodb:27017"
COLLECTION_NAME = "not_interesting_data"
class NotInterestingConsumer(Consumer):
    """Consumer for not interesting articles."""
    def _consume(self):
        """Consume messages and store them in MongoDB."""
        dal = SubDAL(client=MongoClient(URI), collection_name=COLLECTION_NAME)
        for message in self.consumer:
            for mess in message.value:
                data = {
                    "articles": mess,
                    "timestamp": datetime.now()
                }
                dal.add_articles(data)