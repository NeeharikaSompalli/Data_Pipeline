#!/bin/bash

mkdir DIC
cd DIC

echo "Git clone"

git clone https://github.ncsu.edu/araja2/DIC_Data_Pipeline.git

echo "Download Nifi"

wget http://apache.claz.org/kafka/2.0.0/kafka-2.0.0-src.tgz

tar -xzf kafka-2.0.0-src.tgz

BASEDIR=$(dirname "$0")

cp $BASEDIR/DIC_Data_Pipeline/Kafka_Config/server.properties $BASEDIR/kafka-2.0.0-src/config/




 
