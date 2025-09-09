import os

class Config:
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Archivos de entrada y salida
    INPUT_PATH = os.path.join(BASE_DIR, "data/input/sample_music.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "data/output/music_clean.parquet")

    # Base de datos (solo para pruebas locales)
    SQLITE_DB_PATH = os.path.join(BASE_DIR, "data/output/etl_data.db")
    SQLITE_TABLE = "music_clean"

    # Opciones de lectura de CSV
    CSV_OPTIONS = {
        "header": True,
        "inferSchema": True,
        "multiLine": False,
        "mode": "PERMISSIVE"
    }

    # Nombre por defecto de la aplicación Spark
    SPARK_APP_NAME = "music-etl"
