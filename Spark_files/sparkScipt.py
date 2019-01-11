pyspark --packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.3.1  --master yarn --deploy-mode client --executor-memory 4g --num-executors 4 --driver-memory 2g



from pyspark.sql.types import *	
from pyspark.sql.functions import *

findMood_udf = udf(lambda text : "positive" if(len(text)%3 == 0) else("negative" if(len(text)%3 == 1) else "neutral"), StringType())
findURL_udf = udf(lambda id : "https://twitter.com/i/web/status/" + str(id), StringType())

#events1 = spark.read.format("kafka").option("kafka.bootstrap.servers", "ip-172-31-59-152.ec2.internal:6667,ip-172-31-66-6.ec2.internal:6667,ip-172-31-66-109.ec2.internal:6667").option("subscribe", "incomingtweets").option("startingOffsets","earliest").load()
#events2 = events1.selectExpr("CAST(value AS STRING)").where(events1.value.contains('created_at'))
#events2.write.mode("overwrite").format("text").save("/tmp/sparkSchema")
smallBatchSchema = spark.read.json("/tmp/sparkSchema/part-00000-f39b4931-33a8-42cf-ba4a-8b3967b6ed2e-c000.txt").schema
 
events3 = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "ip-172-31-59-152.ec2.internal:6667").option("subscribe", "incomingtweets").option("startingOffsets","earliest").option("failOnDataLoss","false").load()
events4 = events3.selectExpr("CAST(value AS STRING)").where(events3.value.contains('created_at'))
dataDf = events4.selectExpr("CAST(value AS STRING) as json").select( from_json("json", schema=smallBatchSchema).alias("data")).select("data.*")
intermediateDf = dataDf.select("id", "timestamp_ms", "created_at", "user.name", "text", "user.location", "lang", "entities.hashtags.text", "retweet_count", "favorite_count").where("lang = 'en'")
intermediateDf = intermediateDf.toDF("id", "timestamp_ms", "created_at", "user_name", "tweet", "location", "language", "hashtags","retweet_count", "favorite_count")
finalDf = intermediateDf.select("id", (intermediateDf.timestamp_ms/1000).cast("timestamp").alias("tweet_time"), "user_name", "tweet", "location", "language", "hashtags", "retweet_count", "favorite_count")
finalDf2 = finalDf.withColumn("mood", findMood_udf(finalDf.tweet)).withColumn("url", findURL_udf(finalDf.id))

query_window = finalDf2.selectExpr("to_json(struct(*)) AS value").writeStream.format("kafka").option("kafka.bootstrap.servers", "ip-172-31-59-152.ec2.internal:6667,ip-172-31-66-6.ec2.internal:6667,ip-172-31-66-109.ec2.internal:6667").option("topic", "outgoingtweets").option("checkpointLocation", "/tmp/spark_checkpoint_dir").start()


query_window = finalDf2.writeStream.outputMode("append").format("memory").queryName("myTable_window").start()
spark.sql("select tweet_time from myTable_window").show(10,False)
spark.sql("select hashtags, url from myTable_window where language = 'en' and size(hashtags) <> 0").show(10,False)
