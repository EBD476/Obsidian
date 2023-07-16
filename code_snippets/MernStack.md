#### Install mongodb
```shell
> docker run -d -p 27017:27017 --name example-mongo mongo:latest
> docker exec -it <CONTAINER_NAME> bash
> docker logs test-mongo --follow

> docker network create test-network
> docker run -d --network test-network --name test-mongo mongo:latest

docker run -d -p 27017:27017 --name test-mongo -v data-vol:/data/db mongo:latest
```

Security
----------------------------------------------------------------------------------------------
```shell
docker run -d 
-p 27017:27017 
--name test-mongo 
-v mongo-data:/data/db 
-e MONGODB_INITDB_ROOT_USERNAME=sample-db-user
-e MONGODB_INITDB_ROOT_PASSWORD=sample-password 
mongo:latest

docker run \
--detach \
--name=[container_name] \
--env="MYSQL_ROOT_PASSWORD=my_password" \
--publish 6603:3306 \
--volume=/root/docker/[container_name]/conf.d:/etc/mysql/conf.d \
--volume=/storage/docker/mysql-data:/var/lib/mysql \
mysql

```
