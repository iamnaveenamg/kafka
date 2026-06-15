import json

from confluent_kafka import Consumer

consumer_config={
    "bootstrap.servers": "localhost:9092",
    "group.id": "order-tracker", # Unique string that identifies the consumer group this consumer belongs to.
    "auto.offset.reset": "earliest" #It tells what to do when there is no initial offset or if the current offset does nit exit any more on the server
    # (E.g. Because  that data is deleted)
    # 1. earliest: Automatically reset the offset to the earliest offset
    # 2. latest:
    # 3. by_duration
    # 4. none
}

consumer=Consumer(consumer_config)

consumer.subscribe(["orders"])

print("Consumer is Running and Subscribed to orders topic")

try:
    while True:
        msg=consumer.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        value=msg.value().decode("utf-8")
        order=json.loads(value)
        print(f"Received order {order['quantity']} X {order['item']} from {order['user']}")

except KeyboardInterrupt:
    print("\n Stopping Consumer")

finally:
    consumer.close()

