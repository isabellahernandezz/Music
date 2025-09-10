import argparse
import logging
from pyspark.sql import SparkSession
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def build_spark(app_name=Config.SPARK_APP_NAME, master="local[*]"):
    """Crea una sesión Spark."""
    return SparkSession.builder \
        .appName(app_name) \
        .master(master) \
        .config("spark.jars.packages", "org.xerial:sqlite-jdbc:3.34.0") \
        .getOrCreate()

def main(args):
    logging.info("🚀 Iniciando ETL con PySpark")

    # Crear sesión Spark
    spark = build_spark(master=args.master)

    # EXTRACTION
    logging.info(f"🔎 Extrayendo datos desde: {args.input}")
    extractor = Extractor(spark, args.input, Config.CSV_OPTIONS)
    df_raw = extractor.extract()

    logging.info("👀 Mostrando los primeros registros del dataset extraído")
    df_raw.show(5)  # Muestra los primeros 5 registros en consola

    # TRANSFORMATION
    logging.info("⚙️ Aplicando transformaciones...")
    transformer = Transformer(df_raw)
    df_transformed = transformer.transform()

    logging.info("👀 Mostrando los primeros registros transformados")
    df_transformed.show(5)

    # LOADING
    logging.info(f"💾 Guardando resultados en: {args.output}")
    loader = Loader(df_transformed)
    loader.save(args.output, fmt=args.format)

    logging.info("✅ Pipeline ETL finalizado con éxito")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline ETL con PySpark")
    parser.add_argument("--master", type=str, default="local[*]", help="Modo Spark (ej. local[*] o yarn)")
    parser.add_argument("--input", type=str, default=Config.INPUT_PATH, help="Ruta de entrada (CSV)")
    parser.add_argument("--output", type=str, default=Config.OUTPUT_PATH, help="Ruta de salida")
    parser.add_argument("--format", type=str, default="parquet", choices=["parquet", "csv"], help="Formato de salida principal")
    args = parser.parse_args()

    main(args)
