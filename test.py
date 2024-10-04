from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='185.123.68.48:10023')
print("Connected to Kafka!")
