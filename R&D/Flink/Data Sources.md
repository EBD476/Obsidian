### Get data from datasource

```scala
// Data type for words with count
case class WordWithCount(word: String, count: Long)
// get input data by connecting to the socket
val text = senv.socketTextStream("127.0.0.1", 9000, '\n')
// parse the data, group it, window it, and aggregate the counts
val windowCounts = text
.flatMap { w => w.split("\\s") }
.map { w => WordWithCount(w, 1) }
.keyBy("word")
.timeWindow(Time.seconds(5), Time.seconds(1))
.sum("count")
// print the results with a single thread, rather than in parallel
windowCounts.print().setParallelism(1)
senv.execute("Socket Window WordCount")




// Data type for words with count
case class WordWithCount(word: String, count: Long)
// get input data by connecting to the socket
val text = senv.readFileStream("file:///work/data/streaming1.log")
// parse the data, group it, window it, and aggregate the counts
val windowCounts = text
.flatMap { w => w.split("\\s") }
.map { w => WordWithCount(w, 1) }
.keyBy("word")
.timeWindow(Time.seconds(5), Time.seconds(1))
.sum("count")
// print the results with a single thread, rather than in parallel
windowCounts.print().setParallelism(1)
senv.execute("File Stream WordCount")


import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer011
import org.apache.flink.streaming.util.serialization.SimpleStringSchema
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumerBase
import java.util.Properties
val properties = new Properties()
properties.setProperty("bootstrap.servers", "localhost:9092")
properties.setProperty("group.id", "test")

val myConsumer = new FlinkKafkaConsumer011[String](
  "flink1",
  new SimpleStringSchema,
  properties)

val stream = senv.addSource(myConsumer)

case class WordWithCount(word: String, count: Long)
val windowCounts = stream
.flatMap { w => w.split("\\s") }
.map { w => WordWithCount(w, 1) }
.keyBy("word")
.timeWindow(Time.seconds(5), Time.seconds(1))
.sum("count")
// print the results with a single thread, rather than in parallel
windowCounts.print().setParallelism(1)
senv.execute("Kafka Stream WordCount")
```