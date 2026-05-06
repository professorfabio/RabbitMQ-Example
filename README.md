# RabbitMQ-Example
Example based on Tanenbaum &amp; van Steen (2025)

# Steps to run:

## Ports to open on the firewall (security group on AWS):
```
5671-5672
```

## Install the RabbitMQ broker on a server machine:
You may use the provided script for installation (install_rabbitmq.sh) -- run it with sudo
See details on: https://www.rabbitmq.com/docs/install-debian#apt-quick-start

### Once installed, put the broker to run:
```
sudo systemctl start rabbitmq-server
```
### Then create a new RabbitMQ user and password:
```
sudo rabbitmqctl add_user myuser abc123
```
### Now create a vhost in the RabbitMQ server (a vhost is like a container for message queues)?
```
sudo rabbitmqctl add_vhost my_vhost
```
### And give the new user the required permisssions to access the vhost:
```
sudo rabbitmqctl set_permissions -p my_vhost myuser ".*" ".*" ".*"
```

## Install the RabbitMQ python client on the machines where producers and consumers will run:
```
pip install rabbitpy
```

