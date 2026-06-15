import uuid
import json

from confluent_kafka import Producer

producer_config={
    "bootstrap.servers": "localhost:9092"
}

producer = Producer(producer_config)  # It will present in local host
 # bootstrap.servers= Provided the initial hosts that act as the starting point for Kafka client to discover the full set of alive servers in the cluster

def delivery_report(err, msg):
    if err:
        print(f"Delivery Failed: {err}")
    else:
        print(f"Delivered  {msg.value().decode('utf-8')}")
        print(f"Delovered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}.")

order={
    "order_id": str(uuid.uuid4()),
    "user": "Naveen",
    "item": "KFC",
    "quantity": 2
}

value = json.dumps(order).encode("utf-8")  # It will make JSON into string

producer.produce(
    topic="orders",
    value=value,
    callback=delivery_report # it is function
)

producer.flush()  # It will group of events and send them