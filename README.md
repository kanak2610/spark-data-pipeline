# Spark Data Pipeline

## 📌 Objective
The objective of this project is to design and implement an end-to-end data pipeline using Apache Spark.  
It focuses on efficient data processing, schema handling, transformations, filtering, null management, and saving results in optimized formats (CSV/Parquet).  
The project also highlights Spark’s architecture, lazy evaluation, and performance concepts such as shuffle and predicate pushdown.

## ⚙️ Project Explanation
This project demonstrates how Spark can be applied to large-scale datasets for cleaning, transformation, and aggregation.  
Key concepts covered include:
- Spark architecture (Driver, Cluster Manager, Executors)
- Lazy Evaluation and DAG lineage
- Reading data from CSV and Parquet formats
- Applying transformations (filter, select, rename, cast, add new columns)
- Handling null values and schema modifications
- Performance optimization using wide transformations and predicate pushdown
- Saving processed data into multiple formats

## 🚀 Steps
1. **Read Data** → Load CSV/Parquet with schema handling  
2. **Transform Data** → Apply filtering, column selection, renaming, casting, and add calculated columns  
3. **Handle Nulls** → Drop or filter records with missing values  
4. **Optimize** → Use Parquet for faster queries and reduced storage  
5. **Write Output** → Save results into CSV and Parquet formats  
6. **Best Practices** → Avoid `collect()`, use `show()` for samples, prefer Parquet for large datasets  

## 📂 Output
- PySpark code (`pipeline.py`)  
- Processed dataset saved in `output/csv` and `output/parquet`  
- Performance insights: Parquet is faster and more efficient compared to CSV  

## ✅ Conclusion
This project showcases how Apache Spark can be leveraged to build scalable and efficient data pipelines.  
By applying transformations, handling schema and nulls, and saving data in optimized formats, Spark ensures high performance even with large datasets.  
The pipeline is generic, reusable, and can be applied to any dataset for cleaning, transformation, and aggregation tasks.

## ▶️ How to Run
```bash
spark-submit pipeline.py
