class Config:
    """
    Clase de configuración para rutas y parámetros del ETL de música.
    """
    # Ruta del archivo CSV de música (datos crudos)
    INPUT_PATH = '/workspaces/ETLProject/Extract/Files/music_dataset.csv'
    
    # Ruta del archivo de salida (datos limpios / transformados)
    OUTPUT_PATH = '/workspaces/ETLProject/Extract/Files/music_clean.csv'
    
    # Parámetros opcionales para estandarizar
    ENCODING = "utf-8"
    DATE_FORMAT = "%Y-%m-%d"   # por si el dataset incluye fechas (ej: fecha de lanzamiento)
