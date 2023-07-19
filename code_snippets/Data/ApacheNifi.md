### Standalone Instance secured with HTTPS and Single User Authentication

docker for apache nifi
```shell
docker run --name nifi -p 8081:8081 -d  -e NIFI_WEB_HTTP_PORT='8081' apache/nifi:latest
```

The following command can be used to find the generated credentials on operating systems with grep installed:
```
docker logs nifi | grep Generated
```

NiFi logs the generated credentials as follows:

```
Generated Username [USERNAME]
Generated Password [PASSWORD]
```

Single User Authentication credentials can be specified using environment variables as follows:

```
docker run --name nifi \
  -p 8443:8443 \
  -d \
  -e SINGLE_USER_CREDENTIALS_USERNAME=admin \
  -e SINGLE_USER_CREDENTIALS_PASSWORD=ctsBtRBKHRAx69EqUghvvgEvjnaLjFEB \
  apache/nifi:latest
```

### Standalone Instance secured with HTTPS and Mutual TLS Authentication 

```
docker run --name nifi \
  -v /User/dreynolds/certs/localhost:/opt/certs \
  -p 8443:8443 \
  -e AUTH=tls \
  -e KEYSTORE_PATH=/opt/certs/keystore.jks \
  -e KEYSTORE_TYPE=JKS \
  -e KEYSTORE_PASSWORD=QKZv1hSWAFQYZ+WU1jjF5ank+l4igeOfQRp+OSbkkrs \
  -e TRUSTSTORE_PATH=/opt/certs/truststore.jks \
  -e TRUSTSTORE_PASSWORD=rHkWR1gDNW3R9hgbeRsT3OM3Ue0zwGtQqcFKJD2EXWE \
  -e TRUSTSTORE_TYPE=JKS \
  -e INITIAL_ADMIN_IDENTITY='CN=Random User, O=Apache, OU=NiFi, C=US' \
  -d \
  apache/nifi:latest
```