from fastapi import FastAPI

from data_reader import DataReader
from producer import Producer

app = FastAPI()


@app.get("/publish_interesting")
def publish_message():
    """Publish a message to the interesting_topic."""
    producer = Producer()
    dr = DataReader()
    data = dr.read_interesting_data()
    return producer.publish_message(topic="interesting_topic", message=data)

@app.get("/publish_not_interesting")
def publish_not_interesting_message():
    """Publish a message to the not_interesting_topic."""
    producer = Producer()
    dr = DataReader()
    data = dr.read_not_interesting_data()
    return producer.publish_message(topic="not_interesting_topic", message=data)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="localhost", port=6005)


