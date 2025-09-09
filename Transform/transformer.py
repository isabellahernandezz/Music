import os
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

class Transformer:
    def __init__(self, df: DataFrame):
        self.df = df

    def transform(self) -> DataFrame:
        df = self.df

        # ✅ Asegurar columna "artist" desde "track_artist"
        if "track_artist" in df.columns:
            df = df.withColumn("artist", F.trim(F.lower(F.col("track_artist"))))
        else:
            # fallback si ya existe
            df = df.withColumn("artist", F.trim(F.lower(F.col("artist"))))

        # ✅ Renombrar "track_popularity" a "popularity" si existe
        if "track_popularity" in df.columns:
            df = df.withColumnRenamed("track_popularity", "popularity")

        # ✅ Filtro por popularidad
        if "popularity" in df.columns:
            df = df.filter(F.col("popularity") > 80)

        # ✅ Duración en minutos/segundos si existe duration_ms
        if "duration_ms" in df.columns:
            df = df.withColumn("duration_min", (F.col("duration_ms") / 60000).cast("double")) \
                   .withColumn("duration_sec", (F.col("duration_ms") / 1000).cast("int"))

        # ✅ Categoría de popularidad
        if "popularity" in df.columns:
            df = df.withColumn(
                "popularity_category",
                F.when(F.col("popularity") >= 90, F.lit("High"))
                 .when((F.col("popularity") >= 70) & (F.col("popularity") < 90), F.lit("Medium"))
                 .otherwise(F.lit("Low"))
            )

        # ✅ Join con géneros si existe el archivo
        genres_path = os.path.join("data", "input", "genres.csv")
        if os.path.exists(genres_path):
            genres = df.sparkSession.read.option("header", True).csv(genres_path)
            if "artist" in genres.columns:
                df = df.join(genres, on="artist", how="left")

        return df
