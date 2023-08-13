
[PM2](https://github.com/Unitech/pm2) is a Node.js monitoring tool that enables the monitoring of Node.js application performance in production. It allows you to keep your application running forever, reload without downtime, and facilitate common system admin tasks.

![[Pasted image 20230725110045.png]]


With PM2, you can run applications in cluster mode. Use the following command to install the PM2 module:

```shell
npm install pm2 -g
```


You can daemonize your app by running the application source file (e.g., `app.js`), like so:

```shell
pm2 start app.js
```

```shell
$ pm2 start "npm run start"
$ pm2 start "ls -la"
$ pm2 start app.py
```

#### Configuration File

When managing multiple application at the same time or having to specify multiple options, you can use a configuration file. Example with this ecosystem.config.js file:

```shell
module.exports = {
  apps : [{
    name   : "limit worker",
    script : "./worker.js",
    args   : "limit"
  },{
    name   : "rotate worker",
    script : "./worker.js",
    args   : "rotate"
  }]
}
```

Then to start both apps:

```shell
$ pm2 start ecosystem.config.js
```

### Restart

To restart an application:

```
$ pm2 restart api
```

To restart all applications:

```
$ pm2 restart all
```

To restart multiple apps at once:

```
$ pm2 restart app1 app3 app4
```

### Stop

To stop a specified application:

```
$ pm2 stop api
$ pm2 stop [process_id]
```

To stop them all:

```
$ pm2 stop all
```

To stop multiple apps at once:

```
$ pm2 stop app1 app3 app4
```

Note: this will not delete the application from PM2 application list. See next section to delete an application.

### Delete

To stop and delete an application:

```
$ pm2 delete api
```

To delete them all:

```
$ pm2 delete all
```

## Listing Applications

To list all running applications:

```
$ pm2 list
# Or
$ pm2 [list|ls|l|status]
```

![image](https://user-images.githubusercontent.com/757747/123511260-a3f78e00-d680-11eb-8907-3f1017ef7dc8.png)

To specify which order you want the application to be listed:

```
$ pm2 list --sort name:desc
# Or
$ pm2 list --sort [name|id|pid|memory|cpu|status|uptime][:asc|desc]
```

### Terminal Dashboard

PM2 gives you a simple way to monitor the resource usage of your application. You can monitor memory and CPU easily and straight from your terminal with:

```
pm2 monit
```

### Reset restart count

To reset the restart counter:

```
$ pm2 reset all
```