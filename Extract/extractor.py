from pyspark.sql import SparkSession
from Config.config import Config

class Extractor:
    def __init__(self, spark: SparkSession, file_path: str = None, options: dict = None):
        self.spark = spark
        self.file_path = file_path or Config.INPUT_PATH
        self.options = options or Config.CSV_OPTIONS

    def extract(self):
        print(f"🔎 Extrayendo desde: {self.file_path}")
        df = self.spark.read.options(**self.options).csv(self.file_path)
        print(f"✅ Columnas detectadas: {df.columns}")
        return df
