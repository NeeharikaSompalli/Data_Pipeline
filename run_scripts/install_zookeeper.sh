#!/bin/bash

mkdir DIC
cd DIC

echo "Git clone"

git clone https://github.ncsu.edu/araja2/DIC_Data_Pipeline.git

echo "Download Nifi"

wget http://apache.claz.org/zookeeper/zookeeper-3.4.13/zookeeper-3.4.13.tar.gz

tar -xzf zookeeper-3.4.13.tar.gz

echo "Copying config files from git repo to Zookeeper/conf"

BASEDIR=$(dirname "$0")

cp $BASEDIR/DIC_Data_Pipeline/Zookeeper_Config/zoo.cfg $BASEDIR/zookeeper-3.4.13/conf/




 
