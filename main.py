# main.py
import logging
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader


# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Iniciando proceso ETL")

    try:
        # Rutas de entrada y salida
        input_path = "/workspaces/Music/high_popularity_spotify_data_limpio.csv"
        output_path = "/workspaces/Music/high_popularity_spotify_data_final.csv"

        # 1. EXTRAER
        logging.info("Extrayendo datos...")
        extractor = Extractor(input_path)
        df_raw = extractor.extract()
        if df_raw is None or df_raw.empty:
            logging.error("No se pudieron extraer datos.")
            return
        logging.info(f"Datos extraídos correctamente de {input_path} ({len(df_raw)} registros)")

        # 2. TRANSFORMAR
        logging.info("Transformando datos...")
        transformer = Transformer(df_raw)
        df_clean = transformer.transform()
        logging.info(f"Datos transformados: {len(df_clean)} registros")

        # 3. CARGAR
        logging.info("Cargando datos...")
        loader = Loader(df_clean)
        loader.to_csv(output_path)
        logging.info(f"Datos guardados en {output_path}")

    except Exception as e:
        logging.error(f"Error en el proceso ETL: {e}")

if __name__ == "__main__":
    main()
