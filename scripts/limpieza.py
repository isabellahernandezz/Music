import pandas as pd

def limpiar_csv(input_file="high_popularity_spotify_data.csv", output_file="high_popularity_spotify_data_limpio.csv"):
    # Cargar el archivo CSV
    df = pd.read_csv(input_file)

    print("📊 Dataset cargado con éxito")
    print("Filas y columnas originales:", df.shape)

    
    # 1. Eliminar duplicados
    df = df.drop_duplicates()
    print(" Duplicados eliminados. Tamaño actual:", df.shape)

    # 2. Eliminar filas con valores vacíos
    df = df.dropna()
    print(" Filas vacías eliminadas. Tamaño actual:", df.shape)

    # 3. Resetear índices
    df = df.reset_index(drop=True)

    # 4. Revisar y convertir tipos de datos si es necesario

    for col in df.columns:
        if df[col].dtype == "object":
            try:
                df[col] = pd.to_numeric(df[col])
                print(f"ℹ️ Columna convertida a numérica: {col}")
            except:
                pass  

    # Guardar archivo limpio
    df.to_csv(output_file, index=False)
    print(f" Archivo limpio guardado como {output_file}")


if __name__ == "__main__":
    limpiar_csv()