The Elasticsearch container might take longer to start due to a few common factors such as memory settings, disk space, and system resources. Here are some steps you can take to improve the startup time:

1. **Increase JVM Heap Size**:
   Elasticsearch by default allocates JVM heap size which may be too low. Increase it by adding the following in your `docker-compose.yaml` under the Elasticsearch service:
   ```yaml
   environment:
     - "ES_JAVA_OPTS=-Xms2g -Xmx2g"
   ```
   Adjust `2g` based on your available memory (usually, 50% of your total memory for Elasticsearch).

2. **Adjust Virtual Memory Settings**:
   Elasticsearch requires sufficient virtual memory. On your server, run:
   ```bash
   sudo sysctl -w vm.max_map_count=262144
   ```
   To make this persistent across reboots, add the following to `/etc/sysctl.conf`:
   ```
   vm.max_map_count=262144
   ```

3. **Disk Performance**:
   Check your disk I/O speed, as Elasticsearch is disk-heavy. If you're using a slow disk, consider upgrading to SSDs or ensuring there is enough free space.

4. **Resource Constraints in Docker**:
   Make sure you're not restricting Elasticsearch with low CPU or memory limits in your `docker-compose.yaml`. If you've set any limits, increase them:
   ```yaml
   deploy:
     resources:
       limits:
         memory: 4g
         cpus: "2.0"
   ```

5. **Check Elasticsearch Logs**:
   Check the logs from the Elasticsearch container to see if there are any specific errors causing slow startup:
   ```bash
   docker logs <elasticsearch-container-id>
   ```

6. **Ensure Correct Configuration**:
   Ensure that your `docker-compose.yaml` is correctly configured with the necessary volume mounts and environment variables, like:
   ```yaml
   volumes:
     - esdata:/usr/share/elasticsearch/data
   ```

Optimizing these aspects should help Elasticsearch container start faster.