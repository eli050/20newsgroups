from fastapi import FastAPI
from contextlib import asynccontextmanager
from pymongo import MongoClient
from not_interesting_sub.cons import NotInterestingConsumer
from subscribers.DAL import SubDAL
import uvicorn

URI = "mongodb://mongodb:27017"
COLLECTION_NAME = "not_interesting_data"

DAL:SubDAL|None = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Initialize the consumer service and DAL."""
    global DAL
    DAL = SubDAL(MongoClient(URI), COLLECTION_NAME)
    consumer_service = NotInterestingConsumer("not_interesting_topic")
    consumer_service.start()
    yield
    consumer_service.consumer.close()
    print("Shutting down")


app = FastAPI(lifespan=lifespan)




@app.get("/")
def health_check():
    """Health check endpoint."""
    return {"status": "ok"}

@app.get("/data")
async def get_data():
    """Fetch data from the DAL."""
    try:
        assert DAL is not None
        return DAL.get_articles()
    except AssertionError as e:
        return {"error": "Data Access Layer not initialized", "details": str(e)}

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8002)