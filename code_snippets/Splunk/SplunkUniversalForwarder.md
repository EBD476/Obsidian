Step 2: Install Forwarder
Step 3: Enable boot-start/init script:

```shell
 > /opt/splunkforwarder/bin/splunk enable boot-start
  (start splunk: /opt/splunkforwarder/splunk start)
```

		
Step 4: Enable Receiving input on the Index Server

```shell
 /opt/splunk/bin/splunk enable listen 9997
```


Step 5: Configure Forwarder connection to Index Server:
```shell
  ./bin/splunk add forward-server 192.168.164.150:9997
```

	
Step 6: Test Forwarder connection:

```shell
 /opt/splunkforwarder/bin/splunk list forward-server
```


Step 7: Add Data:

```shell
/opt/splunkforwarder/bin/splunk add monitor /path/to/app/logs/ -index main -sourcetype %app%	
```


Step 8 (Optional): Install and Configure UNIX app on Indexer and *nix forwarders:

On the Splunk Server, go to Apps -> Manage Apps -> Find more Apps Online -> Search for ‘Splunk App for Unix and Linux’ -> Install the "Splunk App for Unix and Linux'

Restart Splunk if prompted, Open UNIX app -> Configure

Step 9 (Optional): Customize UNIX app configuration on forwarders:

``` 
Look at inputs.conf in /opt/splunkforwarder/etc/apps/unix/local/ and /opt/splunkforwarder/etc/apps/unix/default/
```


splunk docker-compose file :

```yaml

version: "3.6"

services:
  so1:
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    container_name: so1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_PASSWORD=<password>
    ports:
      - 8000:8000
      - 
```

splunk docker-composer-splunk-indexer-cluster.yml 

```yaml

version: "3.6"

networks:
  splunknet:
    driver: bridge
    attachable: true

services:
  sh1:
    networks:
      splunknet:
        aliases:
          - sh1
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    hostname: sh1
    container_name: sh1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1,idx2,idx3
      - SPLUNK_SEARCH_HEAD_URL=sh1
      - SPLUNK_CLUSTER_MASTER_URL=cm1
      - SPLUNK_ROLE=splunk_search_head
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  cm1:
    networks:
      splunknet:
        aliases:
          - cm1
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    command: start
    hostname: cm1
    container_name: cm1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1,idx2,idx3
      - SPLUNK_SEARCH_HEAD_URL=sh1
      - SPLUNK_CLUSTER_MASTER_URL=cm1
      - SPLUNK_ROLE=splunk_cluster_master
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  idx1:
    networks:
      splunknet:
        aliases:
          - idx1
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    command: start
    hostname: idx1
    container_name: idx1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1,idx2,idx3
      - SPLUNK_SEARCH_HEAD_URL=sh1
      - SPLUNK_CLUSTER_MASTER_URL=cm1
      - SPLUNK_ROLE=splunk_indexer
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  idx2:
    networks:
      splunknet:
        aliases:
          - idx2
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    command: start
    hostname: idx2
    container_name: idx2
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1,idx2,idx3
      - SPLUNK_SEARCH_HEAD_URL=sh1
      - SPLUNK_CLUSTER_MASTER_URL=cm1
      - SPLUNK_ROLE=splunk_indexer
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  idx3:
    networks:
      splunknet:
        aliases:
          - idx3
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    command: start
    hostname: idx3
    container_name: idx3
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1,idx2,idx3
      - SPLUNK_SEARCH_HEAD_URL=sh1
      - SPLUNK_CLUSTER_MASTER_URL=cm1
      - SPLUNK_ROLE=splunk_indexer
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml
```

splunk docker-composer-splunk-seach-head-cluster.yml

```yml
version: "3.6"

networks:
  splunknet:
    driver: bridge
    attachable: true

services:
  sh1:
    networks:
      splunknet:
        aliases:
          - sh1
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    hostname: sh1
    container_name: sh1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1
      - SPLUNK_SEARCH_HEAD_URL=sh2,sh3
      - SPLUNK_SEARCH_HEAD_CAPTAIN_URL=sh1
      - SPLUNK_ROLE=splunk_search_head_captain
      - SPLUNK_DEPLOYER_URL=dep1
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  sh2:
    networks:
      splunknet:
        aliases:
          - sh2
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    hostname: sh2
    container_name: sh2
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1
      - SPLUNK_SEARCH_HEAD_URL=sh2,sh3
      - SPLUNK_SEARCH_HEAD_CAPTAIN_URL=sh1
      - SPLUNK_ROLE=splunk_search_head
      - SPLUNK_DEPLOYER_URL=dep1
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  sh3:
    networks:
      splunknet:
        aliases:
          - sh3
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    hostname: sh3
    container_name: sh3
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1
      - SPLUNK_SEARCH_HEAD_URL=sh2,sh3
      - SPLUNK_SEARCH_HEAD_CAPTAIN_URL=sh1
      - SPLUNK_ROLE=splunk_search_head
      - SPLUNK_DEPLOYER_URL=dep1
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  dep1:
    networks:
      splunknet:
        aliases:
          - dep1
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    hostname: dep1
    container_name: dep1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1
      - SPLUNK_SEARCH_HEAD_URL=sh2,sh3
      - SPLUNK_SEARCH_HEAD_CAPTAIN_URL=sh1
      - SPLUNK_ROLE=splunk_deployer
      - SPLUNK_DEPLOYER_URL=dep1
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

  idx1:
    networks:
      splunknet:
        aliases:
          - idx1
    image: ${SPLUNK_IMAGE:-splunk/splunk:latest}
    hostname: idx1
    container_name: idx1
    environment:
      - SPLUNK_START_ARGS=--accept-license
      - SPLUNK_INDEXER_URL=idx1
      - SPLUNK_SEARCH_HEAD_URL=sh2,sh3
      - SPLUNK_SEARCH_HEAD_CAPTAIN_URL=sh1
      - SPLUNK_ROLE=splunk_indexer
      - SPLUNK_DEPLOYER_URL=dep1
    ports:
      - 8000
      - 8089
    volumes:
      - ./default.yml:/tmp/defaults/default.yml

```
