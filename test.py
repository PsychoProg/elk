from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='185.123.68.48:10023')
print("Connected to Kafka!")



docker save -o elk1.tar docker.elastic.co/elasticsearch/elasticsearch:8.15.1;\
docker save -o elk2.tar docker.elastic.co/elasticsearch/elasticsearch:8.15.1;\
docker save -o elk3.tar elastic/kibana:8.15.1;\
docker save -o elk4.tar confluentinc/cp-zookeeper:latest;\
docker save -o elk5.tar confluentinc/cp-kafka:latest;\
docker save -o elk6.tar neo4j:5.20.0


zip elk.zip elk{1..6}.tar 