# Setting up the Airflow Cluster
### 1. Install and Configure the Master Node (Server A)
Install the system-level dependencies:
sudo apt-get update
sudo apt-get install -y libmysqlclient-dev python3 python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev

### Install and configure MySQL as the Airflow backend database 
Install Airflow and the required dependencies:
pip install 'apache-airflow[mysql]' 'apache-airflow[celery]' 'apache-airflow[rabbitmq]' 'apache-airflow[crypto]' 'apache-airflow[password]'

### Create an Airflow user with the "Admin" role :
airflow create_user -r Admin -u airflow -e your_email@domain.com -f Airflow -l Admin -p password

Initialize the Airflow database:
airflow initdb

### 2. Set up the Worker Nodes (Server B)
Install the system-level dependencies (same as step 1 above).
Install Airflow and the required dependencies (same as step 3 above).
Install Celery and the RabbitMQ message broker 

pip install celery==4.3.0

Set up RabbitMQ server and enable the management console .

### 3. Configure Airflow for Cluster Mode
Update the airflow.cfg file on both the Master and Worker nodes:
Set the executor to CeleryExecutor 
.
Configure the sql_alchemy_conn, broker_url, and celery_result_backend settings to point to the appropriate databases and message broker 
.
Set dags_are_paused_at_creation = True and load_examples = False 
.
Restart the Airflow services after making the configuration changes:
airflow webserver -p 8000
airflow scheduler
airflow worker

### 4. Verify the Airflow Cluster
Access the Airflow web UI at http://<IP-ADDRESS/HOSTNAME>:8000 (or the default port 8080) 
.
Ensure that the Airflow webserver, scheduler, and workers are running correctly.
