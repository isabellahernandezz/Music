import pandas as pd

class Extractor:
    """
    Clase para extraer datos de archivos fuente.
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        """
        Extrae los datos del archivo especificado.
        """
        try:
            df = pd.read_csv(self.file_path)
            print(f"Datos extraídos correctamente de {self.file_path}")
            return df
        except Exception as e:
            print(f"Error al extraer datos: {e}")
            return None
