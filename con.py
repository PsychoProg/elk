from kafka import KafkaProducer
import json

# Initialize Kafka producer to connect to your remote server via NGINX
producer = KafkaProducer(
    bootstrap_servers='192.168.35.5:9092',  # Replace with your server IP and NGINX port
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send some test messages to a topic
for i in range(10):
    data = {'number': i}
    producer.send('test_topic', value=data)
    print(f'Sent: {data}')

# Ensure all messages are sent
producer.flush()
