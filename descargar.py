import os
import json
import requests

# Ruta del archivo JSON local
playlist_file = 'playlist.json'

# Leer la lista de reproducción desde el archivo JSON local
with open(playlist_file, 'r') as f:
    playlist = json.load(f)

segment_files = []

# Obtener la base_url del JSON
base_url = 'https://vod-adaptive-ak.vimeocdn.com/exp=1718976019~acl=%2F635b8d57-e6a7-4455-828c-43d8d1e943d1%2F%2A~hmac=cb8aef1ea348babf0500e27d7ca19acb2404677f1463f6db7616f689a9b56c45/635b8d57-e6a7-4455-828c-43d8d1e943d1/v2/range/avf/'

# Obtener la lista de segmentos del primer video
video_segments = playlist['video'][0]['segments']

# Descargar cada segmento
for segment in video_segments:
    segment_url = base_url + segment['url']
    segment_filename = segment['url'].split('/')[-1].split('?')[0]  # Extraer el nombre del archivo sin los parámetros de la URL
    
    print(f"Descargando {segment_filename} desde {segment_url}")
    
    segment_response = requests.get(segment_url, stream=True)
    
    if segment_response.status_code == 200:
        with open(segment_filename, 'wb') as segment_file:
            for chunk in segment_response.iter_content(chunk_size=8192):
                segment_file.write(chunk)
        segment_files.append(segment_filename)
    else:
        print(f"Error al descargar {segment_filename}: {segment_response.status_code}")

# Crear un archivo de texto que contenga la lista de archivos de segmentos
with open('segments.txt', 'w') as f:
    for segment_file in segment_files:
        f.write(f"file '{segment_file}'\n")

# Combinar los segmentos usando ffmpeg
output_file = 'output.mp4'
ffmpeg_command = f'ffmpeg -f concat -safe 0 -i segments.txt -c copy {output_file}'
os.system(ffmpeg_command)

print(f"Video combinado guardado como {output_file}")
