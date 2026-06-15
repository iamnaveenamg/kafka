# kafka
Apache Kafka is an open-source, distributed event streaming platform used to collect, process, store, and route streams of data at massive scale. It acts as a highly scalable and fault-tolerant "central nervous system" for applications, allowing different systems to publish and subscribe to real-time data.



# kafka- Commands

### Install confluent-kafka dependency
`pip3 install confluent-kafka`

### Validate that the topic was created in kafka container
`docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092`

### Describe that topic and see its partitions
`docker exec -it kafka kafka-topics --bootstrap-server localhost:9092 --describe --topic new_orders`

#### View all events in a topic
`docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning`


#### Commands for Installing virtual Environment
`python -m venv .venv'
`.\.venv\Scripts\Activate.ps1`

