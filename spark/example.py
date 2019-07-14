from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import countDistinct

SPARK_SESSION_APP_NAME = "testing_spark"
SPARK_MASTER_URL = "spark://ip-10-0-1-112.eu-west-1.compute.internal:7077"


spark = SparkSession.builder.appName(SPARK_SESSION_APP_NAME).master(SPARK_MASTER_URL).getOrCreate()
df = spark.createDataFrame([['jorge', 31], ['jose', 32]],
                           schema=StructType([StructField("name", StringType()),
                                              StructField("age", IntegerType())]))
df.select(countDistinct(df['name']).alias('counter')).show()