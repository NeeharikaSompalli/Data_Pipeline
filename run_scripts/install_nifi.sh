#!/bin/bash

mkdir DIC
cd DIC

echo "Git clone"

git clone https://github.ncsu.edu/araja2/DIC_Data_Pipeline.git

echo "Download Nifi"

wget http://apache.cs.utah.edu/nifi/1.7.1/nifi-1.7.1-bin.tar.gz

tar -xzf nifi-1.7.1-bin.tar.gz

echo "Copying config files from git repo to Nifi/conf"

BASEDIR=$(dirname "$0")

cp $BASEDIR/DIC_Data_Pipeline/NiFi_Config/nifi.properties $BASEDIR/nifi-1.7.1/conf/




 
