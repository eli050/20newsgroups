from pymongo import MongoClient
from datetime import datetime
from subscribers.DAL import SubDAL
from subscribers.consumer import Consumer
from pprint import pprint
import time

URI = "mongodb://localhost:27017"
COLLECTION_NAME = "interesting_data"
class InterestingConsumer(Consumer):
    def _consume(self):
        dal = SubDAL(client=MongoClient(URI), collection_name=COLLECTION_NAME)
        for message in self.consumer:
            pprint(message.offset)
            for mess in message.value:
                data = {
                    "articles": mess,
                    "timestamp": datetime.now()
                }
                dal.add_articles(data)