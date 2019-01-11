# DIC_Data_Pipeline

## VCL Servers
- Nifi : 152.46.19.29
- Zookeeper and Kafka : 152.46.16.84
- Spark : 152.46.17.65
- ELK : 152.46.17.12

## Firewall entries

#### To open a port in the firewall(Nifi)
- sudo iptables -I INPUT -p tcp -m tcp --dport 65401 -j ACCEPT

#### Check if the port is added to open list in iptables
- sudo iptables -S | grep 65401

#### To open a port in the firewall(Kafka)
- sudo iptables -I INPUT -p tcp -m tcp --dport 9092 -j ACCEPT

#### Check if the port is added to open list in iptables
- sudo iptables -S | grep 9092

## Apache Nifi

#### Properties: nifi.properties

Change the following entries in nifi.properties file
 
- nifi.web.http.host=152.46.19.29
- nifi.web.http.port=65401


#### Start Nifi
- ./nifi.sh start

#### To access the GUI
- http://152.46.19.29:65401/nifi/


## Apache Zookeeper

#### Properties : zookeeper.properties

#### Start zookeeper
- ./zkServer.sh


## Apache Kafka

#### Properties : server.properties

#### Start kafka
- ./kafka-server-start.sh ../config/server.properties

#### Add new topic to kafka
- bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

#### List all topics
- bin/kafka-topics.sh --list --zookeeper localhost:2181

#### Producer command
- bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test

#### Consumer command
- bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning

## ELK

#### To access Kibana GUI
- http://152.46.17.12:5601
