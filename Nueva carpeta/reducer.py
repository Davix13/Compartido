import sys

# Diccionario para almacenar el recuento de cada dirección MAC
conteo_mac = {}

for linea in sys.stdin:
    # Dividir la línea en MAC y valor
    mac, valor = linea.strip().split(" ")
    
    # Incrementar el contador de la MAC en el diccionario o inicializarlo en 1 si es la primera vez que aparece
    conteo_mac[mac] = conteo_mac.get(mac, 0) + 1

# Imprimir el recuento de cada dirección MAC
for mac, count in conteo_mac.items():
    print(f"{mac}: {count}")
