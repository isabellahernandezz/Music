class Transformer:
    """
    Clase para transformar datos extraídos.
    """
    def __init__(self, df):
        self.df = df

    def transform(self):
        """
        Aplica transformaciones al DataFrame.
        """
        try:
            # Renombrar columnas para compatibilidad con CSV
            df = self.df.copy()
            df.rename(columns={
                'track_popularity': 'popularity',
                'track_artist': 'artist'
            }, inplace=True)

            # Filtrar canciones populares
            df = df[df["popularity"] > 80].copy()

            # Convertir nombres de artistas a minúsculas
            df["artist"] = df["artist"].str.lower()

            # Convertir duración de ms a minutos
            if "duration_ms" in df.columns:
                df["duration_min"] = df["duration_ms"] / 60000

            print("Transformaciones aplicadas correctamente.")
            return df

        except Exception as e:
            print(f"Error en la transformación de datos: {e}")
            return self.df
