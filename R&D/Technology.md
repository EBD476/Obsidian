
### Upstash
Upstash is **a serverless database with Redis API and durable storage**. It provides: Low latency data. Durable storage. Ease of use
https://console.upstash.com/
##### Producer
```java
public static void main(String[] args) throws Exception {
2  var props = new Properties();
3  props.put("bootstrap.servers", "clean-molly-10571-us1-kafka.upstash.io:9092");
4  props.put("sasl.mechanism", "SCRAM-SHA-256");
5  props.put("security.protocol", "SASL_SSL");
6  props.put("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"Y2xlYW4tbW9sbHktMTA1NzEkOZ_WLByoKm95492tP4xo8jQnvy3BNxIdj2eedcU\" password=\"********\";");
7  props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
8  props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
9  
10  try (var producer = new KafkaProducer<String, String>(props)) {
11    // ...
12  }
13}
```


##### Consumer

```java
1public static void main(String[] args) throws Exception {
2  var props = new Properties();
3  props.put("bootstrap.servers", "clean-molly-10571-us1-kafka.upstash.io:9092");
4  props.put("sasl.mechanism", "SCRAM-SHA-256");
5  props.put("security.protocol", "SASL_SSL");
6  props.put("sasl.jaas.config", "org.apache.kafka.common.security.scram.ScramLoginModule required username=\"Y2xlYW4tbW9sbHktMTA1NzEkOZ_WLByoKm95492tP4xo8jQnvy3BNxIdj2eedcU\" password=\"********\";");
7  props.put("key.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
8  props.put("value.deserializer", "org.apache.kafka.common.serialization.StringDeserializer");
9  props.put("auto.offset.reset", "earliest");
10  props.put("group.id", "$GROUP_NAME");
11  
12  try(var consumer = new KafkaConsumer<String, String>(props)) {
13    // ...
14  }
15}
```


#### Node
```javascript
const { Kafka } = require('kafkajs')
2 
3const kafka = new Kafka({
4  brokers: ['clean-molly-10571-us1-kafka.upstash.io:9092'],
5  sasl: {
6    mechanism: 'scram-sha-256',
7    username: 'Y2xlYW4tbW9sbHktMTA1NzEkOZ_WLByoKm95492tP4xo8jQnvy3BNxIdj2eedcU',
8    password: '********',
9  },
10  ssl: true,
11})
12 
13const producer = kafka.producer()
14producer.connect()
15// ...
16producer.disconnect()
17 
18const consumer = kafka.consumer({ groupId: '$GROUP_NAME' })
19consumer.connect()
20// ...
21consumer.disconnect()
```


### supabase

Build production-grade applications with a Postgres database, Authentication, instant APIs, 
Realtime, Functions, Storage and Vector embeddings
https://supabase.com/
