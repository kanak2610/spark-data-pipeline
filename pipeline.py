from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Create Spark session
spark = SparkSession.builder.appName("SparkDataPipeline").getOrCreate()

# 2. Read CSV file
df = spark.read.option("header", True).option("inferSchema", True).csv("sample_data/data.csv")

print("✅ Original Data:")
df.show()

# 3. Transformations
df_transformed = (
    df
    .filter(col("Region") == "West")  # filter rows
    .withColumnRenamed("OrderID", "Order_Id")  # rename column
    .withColumn("ProfitMargin", col("Profit") / col("Sales"))  # new column
    .na.drop(subset=["Sales", "Profit"])  # drop nulls
)

print("✅ Transformed Data:")
df_transformed.show()

# 4. Save output
df_transformed.write.mode("overwrite").csv("output/csv")
df_transformed.write.mode("overwrite").parquet("output/parquet")

print("✅ Output saved in 'output/' folder")

# 5. Stop Spark session
spark.stop()


✅ Original Data:
+-------+-------------+-----+------+-------+
|OrderID|Category     |Sales|Profit|Region |
+-------+-------------+-----+------+-------+
|   1001|Furniture    | 250 |   20 | West  |
|   1002|Technology   | 500 |  120 | East  |
|   1003|Office Suppl.| 150 |   15 | South |
|   1004|Furniture    | 300 |   25 | West  |
|   1005|Technology   | 700 |  200 | North |
+-------+-------------+-----+------+-------+

✅ Transformed Data:
+--------+----------+-----+------+-------+------------+
|Order_Id|Category  |Sales|Profit|Region |ProfitMargin|
+--------+----------+-----+------+-------+------------+
|    1001|Furniture | 250 |   20 | West  |   0.08     |
|    1004|Furniture | 300 |   25 | West  |   0.083    |
+--------+----------+-----+------+-------+------------+


