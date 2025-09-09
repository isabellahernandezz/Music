README.md
# 🎶 Proyecto ETL en PySpark con SQLite

Este proyecto implementa un **pipeline ETL (Extract → Transform → Load)** para procesar datasets musicales de Spotify usando **PySpark**.  
Los datos se limpian, transforman y se almacenan en múltiples formatos: **Parquet, CSV y SQLite**.

---

## 📂 Estructura del Proyecto



Music/
├── Config/
│ └── config.py # Configuración de rutas y parámetros
├── Extract/
│ └── extractor.py # Lógica de extracción de datos (CSV → Spark DataFrame)
├── Transform/
│ └── transformer.py # Transformaciones y limpieza de datos
├── Load/
│ └── loader.py # Carga en Parquet, CSV y SQLite
├── data/
│ ├── input/ # Archivos de entrada (CSV originales)
│ │ ├── sample_music.csv
│ │ ├── high_popularity_spotify_data_limpio.csv
│ └── output/ # Resultados del ETL (Parquet, CSV, SQLite)
│ ├── music_clean_final.parquet
│ ├── music_clean_csv/
│ └── etl_data.db
├── main.py # Orquestación del pipeline ETL
├── scripts/
│ └── verificar_salida.py # Script auxiliar para validar outputs
└── README.md # Documentación


---

## ⚙️ Requisitos

- Python 3.10+
- PySpark
- Pandas
- SQLite (viene incluido con Python)

Instala dependencias:
```bash
pip install pyspark pandas
🚀 Ejecución del ETL
1. Ejemplo con dataset de prueba
python main.py --master local[*] \
  --input data/input/sample_music.csv \
  --output data/output/music_clean.parquet \
  --format parquet

2. Ejemplo con dataset real
python main.py --master local[*] \
  --input data/input/high_popularity_spotify_data_limpio.csv \
  --output data/output/music_clean.parquet \
  --format parquet



🛠️ Transformaciones aplicadas

Normalización de columnas (artist, duration_ms, popularity).

Cálculo de duration_min y duration_sec.

Clasificación de popularidad en categorías:

high (>= 80)

medium (50–79)

low (< 50)





🔄 Flujo de Trabajo con GitFlow

El repositorio sigue la metodología GitFlow:

main → rama estable con versiones de producción.

develop → rama de desarrollo activo.

feature/* → ramas para nuevas funcionalidades.

release/* → ramas de preparación para despliegue.

Ejemplo:

git checkout develop
git checkout -b feature/nueva-transformacion
# ... desarrollar ...
git commit -am "Agrego nueva transformación en Transformer"
git push origin feature/nueva-transformacion


Cuando esté listo:

git checkout develop
git merge feature/nueva-transformacion

📚 Frameworks recomendados (para versiones futuras)

Airflow → Orquestación y programación de ETLs.

Luigi → Pipelines académicos y de investigación.

Spark MLlib → Análisis predictivo sobre datos transformados.

Delta Lake → Control de versiones en datos (Parquet avanzado)