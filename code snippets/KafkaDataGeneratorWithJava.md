
```shell
java -jar build/libs/kafka-data-generator-1.0.0.jar -message-count 10 -message-size 256 -topic test-topic -bootstrap.servers "localhost:29092"

$ java -jar build/libs/kafka-data-generator-1.0.0.jar -message-count 10000 -message-size 256 -topic test-topic -bootstrap.servers "localhost:29092" -eps 1000
```

kafka docker-compose.yml

```yml
version: '2'
services:
  zookeeper:
    image: mirror.baidubce.com/confluentinc/cp-zookeeper
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000
    ports:
      - 22181:2181
  
  kafka:
    image: mirror.baidubce.com/confluentinc/cp-kafka
    depends_on:
      - zookeeper
    ports:
      - 29092:29092
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9092,PLAINTEXT_HOST://localhost:29092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: PLAINTEXT:PLAINTEXT,PLAINTEXT_HOST:PLAINTEXT
      KAFKA_INTER_BROKER_LISTENER_NAME: PLAINTEXT
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1
```