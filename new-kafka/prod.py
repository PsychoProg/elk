from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic
import time

# Kafka server details
KAFKA_SERVER = '192.168.35.215:10024'
TOPIC_NAME = 'test_topic'

def create_topic():
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_SERVER, 
        client_id='test_admin'
    )

    topic_list = []
    topic_list.append(NewTopic(name=TOPIC_NAME, num_partitions=1, replication_factor=1))
    admin_client.create_topics(new_topics=topic_list, validate_only=False)

    print(f"Topic '{TOPIC_NAME}' created successfully")

def produce_messages():
    producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)

    for i in range(10):
        message = f"Message {i}"
        producer.send(TOPIC_NAME, value=message.encode('utf-8'))
        print(f"Sent: {message}")
        time.sleep(1)  # Simulating delay in sending messages

    producer.flush()

def consume_messages():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=KAFKA_SERVER,
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group'
    )

    print(f"Reading messages from topic '{TOPIC_NAME}':")
    for message in consumer:
        print(f"Received: {message.value.decode('utf-8')}")

if __name__ == "__main__":
    # Step 1: Create a topic
    create_topic()

    # Step 2: Produce messages to the topic
    produce_messages()

    # Step 3: Consume messages from the topic
    consume_messages()
