from pymongo import MongoClient
from datetime import datetime
from subscribers.DAL import SubDAL
from subscribers.consumer import Consumer
from pprint import pprint


URI = "mongodb://mongodb:27017"
COLLECTION_NAME = "interesting_data"
class InterestingConsumer(Consumer):
    """Consumer for interesting articles."""
    def _consume(self):
        """Consume messages and store them in MongoDB."""
        dal = SubDAL(client=MongoClient(URI), collection_name=COLLECTION_NAME)
        for message in self.consumer:
            pprint(message.offset)
            for mess in message.value:
                data = {
                    "articles": mess,
                    "timestamp": datetime.now()
                }
                dal.add_articles(data)