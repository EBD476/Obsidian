
https://archive.apache.org/dist/flink/
### Start flink scala shell 

```
./bin/start-scala-shell.sh local
```
### Batch Process

### Load Data
```scala
benv.readTextFile("./work/data/OnlineRetail.csv")
dataSet.count()
dataSet.first(5).print()

```

### Transformations

```scala
//reading csv 
val dataSet = benv.readTextFile("/work/data/OnlineRetail.csv")
dataSet.count()
dataSet.first(5).print()

val splitData = dataSet.map(line => (line.split(",")(2).trim(), line.split(",")(3).trim()))
splitData.first(5).print()

splitData.writeAsCsv("file:///work/data/out1.csv")
benv.execute()


```

```scala

//remove header by filtering out the first line
val noHeader = dataSet.filter(!_.startsWith("InvoiceNo"))
noHeader.first(5).print()

//show Description column
val splitData = noHeader.map(line => line.split(",")(2))
splitData.first(5).print()

//flatmap
val splitData = noHeader.flatMap(line => line.split(","))
splitData.first(5).print()

//show quantity column
val splitData = noHeader.map(line => line.split(",")(3))
splitData.first(5).print()

val goodrecords = noHeader.filter(line => line.split(",").length ==8)
goodrecords.count()

val errors = noHeader.filter(line => line.split(",").length !=8)
errors.count()
errors.first(5).print()

//show Description and quantity columns
val splitData = goodrecords.map(line => (line.split(",")(2).trim(), line.split(",")(3).trim().toInt))
splitData.first(5).print()


splitData.map(x => (x._1,x._2)).groupBy(0).sum(1).first(5).print()


scala> val mpDataSet = splitData.mapPartition{ in => in.map{(_,1)} }
mpDataSet: org.apache.flink.api.scala.DataSet[((String, Int), Int)] = org.apache.flink.api.scala.DataSet@6b5d10cd

scala> mpDataSet.first(5).print()
((WHITE HANGING HEART T-LIGHT HOLDER,6),1)
((WHITE METAL LANTERN,6),1)
((CREAM CUPID HEARTS COAT HANGER,8),1)
((KNITTED UNION FLAG HOT WATER BOTTLE,6),1)
((RED WOOLLY HOTTIE WHITE HEART.,6),1)

```

### Rebalance 
```scala

splitData.distinct.count()

splitData.minBy(1).print()

splitData.maxBy(1).print()

splitData.rebalance()

val both = goodrecords.union(errors)
both.count()

```


### Partitioning
```scala

val dataSet = benv.readTextFile("/work/data/OnlineRetail.csv")

val goodrecords = dataSet.filter(!_.startsWith("InvoiceNo")).filter(line => line.split(",").length ==8)
goodrecords.count()

//show Description and quantity columns
val splitData = goodrecords.map(line => (line.split(",")(2).trim(), line.split(",")(3).trim().toInt))
splitData.first(5).print()



splitData.getParallelism
splitData.setParallelism(-1)

val repar = splitData.partitionByHash(0).mapPartition{in => in.map{(_,1)}}


splitData.partitionByHash(0).setParallelism(5).countElementsPerPartition.collect
splitData.setParallelism(5).countElementsPerPartition.collect

splitData.getParallelism
splitData.setParallelism(-1)

val repar = splitData.partitionByRange(0).mapPartition{in => in.map{(_,1)}}
splitData.partitionByRange(0).setParallelism(5).countElementsPerPartition.collect
splitData.setParallelism(5).countElementsPerPartition.collect


splitData.getParallelism
splitData.setParallelism(-1)

class mypartitioner extends Partitioner[String]{ def partition(s: String, i: Int): Int = {return math.abs(s.hashCode%5)}}
val repar = splitData.partitionCustom(new mypartitioner,0).mapPartition{in => in.map{(_,1)}}

splitData.partitionCustom(new mypartitioner,0).setParallelism(5).countElementsPerPartition.collect
splitData.setParallelism(5).countElementsPerPartition.collect


splitData.getParallelism
splitData.setParallelism(-1)

val repar = splitData.sortPartition(1, Order.ASCENDING).mapPartition {in => in.map{(_,1)}}

splitData.sortPartition(1, Order.ASCENDING).setParallelism(5).countElementsPerPartition.collect

splitData.setParallelism(5).countElementsPerPartition.collect
```


### Aggregations

``` scala
import org.apache.flink.util._



val taxes = benv.readTextFile("/work/data/statesTaxRates.csv")
taxes.count()
taxes.first(5).print()


val taxesColumns = taxes.filter(!_.startsWith("State")).map(line => (line.split(",")(0).trim(), line.split(",")(1).trim().toFloat))
taxesColumns.first(5).print()

val populations = benv.readTextFile("/work/data/statesPopulation.csv")
populations.count()
populations.first(5).print()


val populationsColumns = populations.filter(!_.startsWith("State")).map(line => (line.split(",")(0).trim(), line.split(",")(1).trim().toInt, line.split(",")(2).trim().toLong))
populationsColumns.first(5).print()

# reduce

val reduce1 = populationsColumns.groupBy(0).reduce(new ReduceFunction[(String, Int, Long)] {
      override def reduce(intermediateResult: (String, Int, Long), next: (String, Int, Long)): (String, Int, Long) = {
        (intermediateResult._1,intermediateResult._2, intermediateResult._3 + next._3)
      }
    })
reduce1.first(5).print()

#reduceGroup


val groupreduce1 = populationsColumns.groupBy(0).reduceGroup(new GroupReduceFunction[(String, Int, Long), (String, Int, Long)] {
      override def reduce(iterable: java.lang.Iterable[(String, Int, Long)], collector: Collector[(String, Int, Long)]): Unit = {
        var sum = 0L
        var state =""
        var year = 0
        val itor = iterable.iterator
        while (itor.hasNext) {
          val t = itor.next()
          state = t._1
          year = t._2
          sum += t._3
        }
        collector.collect(state, year, sum)
      }
    })
 
groupreduce1.first(5).print()

populationsColumns.groupBy(0).sum(2).first(5).print()
populationsColumns.filter(_._1 == "Alabama").sum(2).first(5).print()
populationsColumns.filter(_._1 == "Alabama").min(2).first(5).print()
populationsColumns.filter(_._1 == "Alabama").max(2).first(5).print()


val cogroup = taxesColumns.coGroup(populationsColumns).where(0).equalTo(0){new CoGroupFunction[(String, Float), (String, Int, Long), (String, Float, Long)] { override def coGroup(left: java.lang.Iterable[(String, Float)], right: java.lang.Iterable[(String, Int, Long)], collector: Collector[(String, Float, Long)]): Unit = { 
	var state = ""; var sum = 0L; var tax = 0.0f
	val ritor = right.iterator
    while (ritor.hasNext) {
    	val t = ritor.next()
    	state = t._1
    	sum += t._3 }
	val litor = left.iterator
	if (litor.hasNext) {
		val t = litor.next()
		state = t._1
		tax = t._2 }
	collector.collect((state, tax, sum) ) }}}

cogroup.first(5).print()

```


### Join

```scala
import org.apache.flink.util._


//innerjoin of the 2 datasets
val innerJoin = taxesColumns.join(populationsColumns).where(0).equalTo(0)
innerJoin.first(5).print()

//extract state, taxrate and population from the joined dataset
val stateRatePop = innerJoin.map(x => (x._1._1, x._1._2, x._2._3))
stateRatePop.first(5).print()

//add up population per state
stateRatePop.groupBy(0).sum(2).first(5).print()

val lojoin = taxesColumns.leftOuterJoin(populationsColumns).where(0).equalTo(0) {(x,y) => (if (y==null) (x._1,x._2, 0, 0) else (x._1, x._2, y._2.toInt, y._3.toInt))}

lojoin.first(2).print()

lojoin.filter(_._4 == 0).first(2).print()


val rojoin = taxesColumns.rightOuterJoin(populationsColumns).where(0).equalTo(0) {(x,y) => (if (x==null) (y._1, 0, y._2.toInt, y._3.toInt) else (x._1, x._2, y._2.toInt, y._3.toInt))}

rojoin.first(2).print()

rojoin.filter(_._2 == 0).first(2).print()


val fojoin = taxesColumns.fullOuterJoin(populationsColumns).where(0).equalTo(0) {(x,y) => (if (x==null) (y._1, 0, y._2.toInt, y._3.toInt) else if (y==null) (x._1,x._2, 0, 0) else (x._1, x._2, y._2.toInt, y._3.toInt))}

fojoin.first(2).print()

fojoin.filter(_._2 == 0).first(2).print()


val lajoin = taxesColumns.leftOuterJoin(populationsColumns).where(0).equalTo(0) {(x,y) => (if (y==null) (x._1,x._2) else (None, None))}.filter(_._1 != None)

lajoin.first(2).print()


val lsjoin = taxesColumns.leftOuterJoin(populationsColumns).where(0).equalTo(0) {(x,y) => (if (y==null) (None, None) else (x._1,x._2) )}.filter(_._1 != None)

lsjoin.first(2).print()


val crossjoin = taxesColumns.cross(populationsColumns){(x,y) => (x,y)}

crossjoin.first(2).print()


val crossjoin = taxesColumns.cross(populationsColumns){(x,y) => if (x._1 == y._1) (x._1,y._1,x._2,y._2.toInt, y._3.toInt) else (None, None, None, None, None)}.filter(_._1 != None)

crossjoin.first(2).print()
```