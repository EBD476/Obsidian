
### Producer 

```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic first_topic --create --partitions 3 --replication-factor 1

kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic
```

#### Produce messages to the topic from the file (see the end of the command)
```shell
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic < topic-input.txt
```

### Produce messages with key in the Kafka Console 

By default messages sent to a Kafka topic will result in messages with `null` keys.

We must use the properties `parse.key` and `key.separator` to send the key alongside messages.

In this example, the separator between the key and the value is: `:`

``` shell
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic first_topic --property parse.key=true --property key.separator=:
```


### Consumer

```shell
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic
```
Use the `--from-beginning` option

```shell
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --from-beginning 
```

By default, the console consumer will show only the value of the Kafka record. Using this command you can show both the key and value.

Using the `formatter` `kafka.tools.DefaultMessageFormatter` and using the properties `print.timestamp=true` `print.key=true` `print.value=true`:

```shell
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --formatter kafka.tools.DefaultMessageFormatter --property print.timestamp=true --property print.key=true --property print.value=true --from-beginning

CreateTime:1641810588071	null	hello
CreateTime:1641823304170	name	Stephane
CreateTime:1641823301294	example key	example value
```

More properties are available such as:

- `print.partition`
- `print.offset`
- `print.headers`
- `key.separator`
- `line.separator`
- `headers.separator`

### Create Consumer Group Example

You cannot have more consumers in a group than partitions in your Kafka topic, and therefore we first need to create a Kafka topic with a few partitions (in the example 3).

```shell
kafka-topics.sh --bootstrap-server localhost:9092 --topic first_topic --create --partitions 3 --replication-factor 1

kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-first-application 
```

Open a new terminal/shell window and launch a second consumer in the same consumer group `my-first-application` (note we're using the exact same command)

```shell
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic first_topic --group my-first-application 
```