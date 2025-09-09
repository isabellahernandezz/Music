from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.master("local[*]").appName("check-output").getOrCreate()

    # Leer Parquet generado
    df = spark.read.parquet("data/output/music_clean_final.parquet")

    # Mostrar primeras filas
    df.show(truncate=False)

    # Mostrar esquema
    df.printSchema()

if __name__ == "__main__":
    main()

