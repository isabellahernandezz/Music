import os
import sqlite3
import pandas as pd
from pyspark.sql import DataFrame
from Config.config import Config

class Loader:
    def __init__(self, df: DataFrame):
        self.df = df

    def save(self, output_path: str, fmt: str = "parquet"):
        # Asegurar que la carpeta de salida existe
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Guardar en Parquet
        self.df.write.mode("overwrite").parquet(
            Config.OUTPUT_PATH.replace(".parquet", "_final.parquet")
        )

        # Guardar en CSV
        self.df.write.mode("overwrite").option("header", True).csv(
            Config.OUTPUT_PATH.replace(".parquet", "_csv")
        )

        # Guardar en SQLite usando pandas
        pdf = self.df.toPandas()  # convertir a Pandas
        conn = sqlite3.connect(Config.SQLITE_DB_PATH)
        pdf.to_sql(Config.SQLITE_TABLE, conn, if_exists="replace", index=False)
        conn.close()

        print("✅ Datos guardados en Parquet, CSV y SQLite (con pandas)")
