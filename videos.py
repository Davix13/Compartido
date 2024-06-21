import requests
import json

# URL del playlist JSON
playlist_url = "https://vod-adaptive-ak.vimeocdn.com/exp=1718812549~acl=%2F635b8d57-e6a7-4455-828c-43d8d1e943d1%2F%2A~hmac=5cfafbfaf335519b5ad75e02123067bd75cdb17bc993bc1526f81b41026b2b91/635b8d57-e6a7-4455-828c-43d8d1e943d1/v2/playlist/av/primary/playlist.json?omit=av1-hevc&pathsig=8c953e4f~bwmDyYPsiZLXf9YwPQuwM7jzgm0qjBQeLxSXZe9hTDw&qsr=1&rh=3yMON4"

# Hacer la solicitud al playlist JSON
response = requests.get(playlist_url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Cargar el contenido JSON
    playlist_json = response.json()

    # Guardar el JSON en un archivo local
    with open('playlist.json', 'w', encoding='utf-8') as f:
        json.dump(playlist_json, f, ensure_ascii=False, indent=4)

    print("Archivo JSON guardado correctamente.")
else:
    print(f"Error al obtener el archivo JSON: {response.status_code}")
