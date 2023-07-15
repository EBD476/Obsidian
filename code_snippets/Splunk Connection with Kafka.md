 ### Connect kafka to splunk
 
 - create splunk hec 8088
 ```bash
 > docker exec -it  kafka-kafka-1 bash
 > .$KAFKA_HOME/bin/connect-standalone.sh /etc/kafka/connect-standalone.properties
```
 
 ```bash
 > docker cp original-splunk-kafka-connect-v2.1.1.jar  kafka-kafka-1:/usr/share/java
 > docker cp splunk-kafka-connect-v2.1.1.jar kafka-kafka-1:/usr/share/java
``` 

  
 - apply this in kafka container bash:
  ```bash
curl localhost:8083/connectors -X POST -H "Content-Type: application/json" -d '{ "name": "kafka-connect-splunk", "config": { "connector.class": "com.splunk.kafka.connect.SplunkSinkConnector","topics":"test-topic","splunk.hec.token": "06c4f21e-5a29-4931-886e-a105d6af2fb0","splunk.hec.uri":"http://192.168.164.150:8088","splunk.indexes": "kafka"} }'
``` 
 
 
 - config below parameters in connect-standalone.properties file :
```properties
 schemas.enable=false
 key.converter.schemas.enable=false
 value.converter.schemas.enable=false
```

 ```shell
      # List active connectors
    curl http://localhost:8083/connectors 
    
	 # Get kafka-connect-splunk connector info
    curl http://localhost:8083/connectors/kafka-connect-splunk

    # Get kafka-connect-splunk connector config info
    curl http://localhost:8083/connectors/kafka-connect-splunk/config

    # Delete kafka-connect-splunk connector
    curl http://localhost:8083/connectors/kafka-connect-splunk -X DELETE

    # Get kafka-connect-splunk connector task info
    curl http://localhost:8083/connectors/kafka-connect-splunk/tasks
```


config file connect-standalone-no-schema.properties 

```properties
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# These are defaults. This file just demonstrates how to override some settings.
bootstrap.servers=localhost:9092

# The converters specify the format of data in Kafka and how to translate it into Connect data. Every Connect user will
# need to configure these based on the format they want their data in when loaded from or stored into Kafka
key.converter=org.apache.kafka.connect.json.JsonConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
# Converter-specific settings can be passed in by prefixing the Converter's setting with the converter we want to apply
# it to
key.converter.schemas.enable=false
value.converter.schemas.enable=false

offset.storage.file.filename=/tmp/connect.offsets
# Flush much faster than normal, which is useful for testing/debugging
offset.flush.interval.ms=10000

# Set to a list of filesystem paths separated by commas (,) to enable class loading isolation for plugins
# (connectors, converters, transformations). The list should consist of top level directories that include 
# any combination of: 
# a) directories immediately containing jars with plugins and their dependencies
# b) uber-jars with plugins and their dependencies
# c) directories immediately containing the package directory structure of classes of plugins and their dependencies
# Note: symlinks will be followed to discover dependencies or plugins.
# Examples: 
# plugin.path=/usr/local/share/java,/usr/local/share/kafka/plugins,/opt/connectors,
plugin.path=/usr/share/java

```

splunk-sink.properties
```properties
name=splunk-sink 
topics=test-topic 
tasks.max=1
bootstrap.servers=localhost:29092
splunk.hec.token=5445c3a8-d133-42df-bcea-06a245803973        
splunk.hec.url=https://localhost:8083
```


![[splunk-hec1.jpg]]

![[splunk-hec2.jpg]]