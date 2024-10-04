from kafka import KafkaProducer
import json

# Initialize Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send some test messages to a topic
for i in range(10):
    data = {'number': i}
    producer.send('test_topic', value=data)
    print(f'Sent: {data}')

# Ensure all messages are sent
producer.flush()
