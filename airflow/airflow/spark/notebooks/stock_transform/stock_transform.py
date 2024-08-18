# README:
# SPARK_APPLICATION_ARGS contains stock-market/AAPL/prices.json
# SPARK_APPLICATION_ARGS will be passed to the Spark application as an argument -e when running the Spark application from Airflow
# - Sometimes the script can stay stuck after "Passing arguments..."
# - Sometimes the script can stay stuck after "Successfully stopped SparkContext"
# - Sometimes the script can show "WARN TaskSchedulerImpl: Initial job has not accepted any resources; check your cluster UI to ensure that workers are registered and have sufficient resources"
# The easiest way to solve that is to restart your Airflow instance
# astro dev kill && astro dev start
# Also, make sure you allocated at least 8gb of RAM to Docker Desktop
# Go to Docker Desktop -> Preferences -> Resources -> Advanced -> Memory

# Import the SparkSession module
from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import explode, col
from pyspark.sql.types import DateType

import os
import sys

if __name__ == '__main__':

    def app():
        # Create a SparkSession
        spark = SparkSession.builder.appName("FormatStock") \
            .config("fs.s3a.access.key", os.getenv("AWS_ACCESS_KEY_ID", "minio")) \
            .config("fs.s3a.secret.key", os.getenv("AWS_SECRET_ACCESS_KEY", "minio123")) \
            .config("fs.s3a.endpoint", os.getenv("ENDPOINT", "http://host.docker.internal:9000")) \
            .config("fs.s3a.connection.ssl.enabled", "false") \
            .config("fs.s3a.path.style.access", "true") \
            .config("fs.s3a.attempts.maximum", "1") \
            .config("fs.s3a.connection.establish.timeout", "5000") \
            .config("fs.s3a.connection.timeout", "10000") \
            .getOrCreate()

        # Read a JSON file from an MinIO bucket using the access key, secret key, 
        # and endpoint configured above
        df = spark.read.option("header", "false") \
            .json(f"s3a://{os.getenv('SPARK_APPLICATION_ARGS')}/prices.json")

        # Explode the dates (keys) into rows
        df_exploded = df.select(explode(col("*")).alias("date", "values"))

        # Select and rename columns to match the desired structure
        df_transformed = df_exploded.select(
            col("date"),
            col("values.`1. open`").alias("open"),
            col("values.`2. high`").alias("high"),
            col("values.`3. low`").alias("low"),
            col("values.`4. close`").alias("close"),
            col("values.`5. volume`").alias("volume")
        )

        # Store in Minio
        df_transformed.write \
            .mode("overwrite") \
            .option("header", "true") \
            .option("delimiter", ",") \
            .csv(f"s3a://{os.getenv('SPARK_APPLICATION_ARGS')}/formatted_prices")

    app()
    os.system('kill %d' % os.getpid())