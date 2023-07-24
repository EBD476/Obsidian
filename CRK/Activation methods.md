####  recompile java 

- modify and compile BaseLicenseCheckService.java 
 ```bash
 javac  -cp "C:\Users\E_Dehghani\Downloads\Compressed\flowable-trial\flowable\tomcat\webapps\flowable-design\WEB-INF\lib\flowable-license-1.4.3.jar;C:\Users\E_Dehghani\Downloads\Compressed\flowable-trial\flowable\tomcat\webapps\flowable-design\WEB-INF\lib\flowable-engine-common-api-6.8.0.14.jar;C:\Users\E_Dehghani\Downloads\Compressed\flowable-trial\flowable\tomcat\webapps\flowable-design\WEB-INF\lib\slf4j-api-1.7.36.jar;C:\Users\E_Dehghani\Downloads\Compressed\flowable-trial\flowable\tomcat\webapps\flowable-design\WEB-INF\lib\spring-core-5.3.24.jar" BaseLicenseCheckService.java
```

- extract jar file and replace BaseLicenseCheckService.class

- create new jar package from changed files
 ```bash
"C:\Program Files\Java\jdk-11.0.17\bin\jar" cvf flowable-license-1.4.3.jar 
```
  