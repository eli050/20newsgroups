from kafka import KafkaConsumer
import threading
import json



class Consumer:
    def __init__(self, topic, bootstrap_servers="broker:9092", group_id="my-group"):
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=[bootstrap_servers],
            auto_offset_reset="earliest",
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode("utf-8"))
        )
        self.thread = threading.Thread(target=self._consume, daemon=True)

    def start(self):
        self.thread.start()


    def _consume(self):
        pass

