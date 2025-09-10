import argparse
import logging
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Configuración de logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def build_spark(app_name="ETL Spotify", master="local[*]"):
    """Crea una sesión Spark."""
    return SparkSession.builder \
        .appName(app_name) \
        .master(master) \
        .getOrCreate()

def generate_graphs(df_transformed):
    """Genera gráficos seguros usando Matplotlib y Seaborn."""
    df_pd = df_transformed.toPandas()
    sns.set(style="whitegrid", palette="pastel")

    # Histograma de popularidad
    plt.figure(figsize=(10,6))
    sns.histplot(df_pd['popularity'], bins=30, kde=True, color='purple')
    plt.title('Distribución de Popularidad de Canciones')
    plt.xlabel('Popularidad')
    plt.ylabel('Cantidad de canciones')
    plt.tight_layout()
    plt.savefig("data/output/popularity_histogram.png")
    plt.close()

    # Top 10 artistas más populares
    top_artists = df_pd.groupby('artist')['popularity'].mean().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_artists.values, y=top_artists.index, palette="viridis")
    plt.title('Top 10 artistas más populares')
    plt.xlabel('Popularidad promedio')
    plt.ylabel('Artista')
    plt.tight_layout()
    plt.savefig("data/output/top10_artists.png")
    plt.close()

    logging.info("✅ Gráficos generados en data/output/")

def main(args):
    logging.info("🚀 Iniciando ETL con PySpark + Gráficos")

    # Crear carpeta de salida si no existe
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    # Crear sesión Spark
    spark = build_spark(master=args.master)

    # Leer CSV
    logging.info(f"🔎 Leyendo datos desde: {args.input}")
    df_raw = spark.read.csv(args.input, header=True, inferSchema=True)
    df_raw.show(5)

    # Transformaciones básicas (solo ejemplo)
    logging.info("⚙️ Aplicando transformaciones básicas")
    df_transformed = df_raw.withColumn("popularity", df_raw["popularity"].cast("integer"))
    df_transformed.show(5)

    # Guardar resultado
    logging.info(f"💾 Guardando resultado en: {args.output}")
    if args.format == "parquet":
        df_transformed.write.mode("overwrite").parquet(args.output)
    else:
        df_transformed.write.mode("overwrite").csv(args.output, header=True)

    # Generar gráficos
    logging.info("📊 Generando gráficos de análisis")
    generate_graphs(df_transformed)

    logging.info("✅ Pipeline ETL finalizado con éxito")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pipeline ETL simple con PySpark + Gráficos")
    parser.add_argument("--master", type=str, default="local[*]", help="Modo Spark (local[*] o yarn)")
    parser.add_argument("--input", type=str, required=True, help="Ruta de entrada CSV")
    parser.add_argument("--output", type=str, required=True, help="Ruta de salida Parquet/CSV")
    parser.add_argument("--format", type=str, default="parquet", choices=["parquet", "csv"], help="Formato de salida")
    args = parser.parse_args()

    main(args)
