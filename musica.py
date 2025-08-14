# Script para buscar canciones con la API de iTunes
import requests

def buscar_cancion(nombre):
    url = "https://itunes.apple.com/search"
    params = {
        "term": nombre,
        "media": "music",
        "limit": 5
    }
    response = requests.get(url, params=params)
    data = response.json()

    print(f"\nResultados para '{nombre}':\n")
    for track in data.get("results", []):
        print(f"- {track['trackName']} — {track['artistName']}")

if __name__ == "__main__":
    termino = input("🔍 Ingresa el nombre de la canción o artista: ")
    buscar_cancion(termino)
