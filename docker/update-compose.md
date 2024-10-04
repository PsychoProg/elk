Yes, you can update your `docker-compose.yaml` file to add or update another container without restarting the Elasticsearch container. Here's how you can do it:

1. **Modify the `docker-compose.yaml`**:
   You can add or update services in the `docker-compose.yaml` file. For example, if you want to add a new container (like Kibana or Logstash), you can add the following service without modifying the Elasticsearch service:

   ```yaml
   version: '3'
   services:
     elasticsearch:
       image: docker.elastic.co/elasticsearch/elasticsearch:8.0.0
       # ... other configs
       
     kibana:
       image: docker.elastic.co/kibana/kibana:8.0.0
       ports:
         - "5601:5601"
       environment:
         - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
   ```

2. **Use `docker-compose up` for the new or updated service**:
   To start or update the new container without affecting Elasticsearch, use the following command:

   ```bash
   docker-compose up -d kibana
   ```

   This command will start the Kibana container or update it without affecting the Elasticsearch container. The `-d` flag ensures that it runs in detached mode, and specifying `kibana` (or the updated container) prevents Docker from touching the other services (like Elasticsearch).

3. **Scaling a Specific Service**:
   If you are adding a new instance or updating an existing service, you can scale the service individually without impacting others:
   ```bash
   docker-compose up -d --scale kibana=2
   ```

4. **Restart a Specific Container**:
   If you just want to restart a single container (for example, `kibana`) without restarting Elasticsearch, you can do this by using:
   ```bash
   docker-compose restart kibana
   ```

In summary, Docker Compose allows you to update or add containers individually without having to restart the entire stack, including Elasticsearch. Just specify the service name in the `docker-compose up` or `docker-compose restart` commands, and it will only affect that container.