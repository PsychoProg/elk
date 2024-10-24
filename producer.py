from kafka import KafkaProducer
import json

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='192.168.1.102:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send some test messages to a topic
for i in range(10):
    data = {'number': i}
    producer.send('testtopic', value=data)
    print(f'Sent: {data}')

# Ensure all messages are sent
producer.flush()


# /bin/kafka-topics --create --topic users.test --replication-factor 1 --partitions 2 --bootstrap_server zookeeper:2181