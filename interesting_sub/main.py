from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from pymongo import MongoClient
from interesting_sub.cons import InterestingConsumer
from subscribers.DAL import SubDAL

URI = "mongodb://localhost:27017"
COLLECTION_NAME = "interesting_data"

DAL:SubDAL|None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global DAL
    DAL = SubDAL(MongoClient(URI), COLLECTION_NAME)
    consumer_service = InterestingConsumer("interesting_topic")
    consumer_service.start()
    yield
    consumer_service.consumer.close()
    print("Shutting down")


app = FastAPI(lifespan=lifespan)




@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/data")
def get_data():
    try:
        assert DAL is not None
        return DAL.get_articles()
    except AssertionError as e:
        return {"error": "Data Access Layer not initialized", "details": str(e)}


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8001)