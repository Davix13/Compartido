import sys

def mapper():
    for linea in sys.stdin:
        # Eliminamos espacios en blanco al principio y al final de la línea
        linea = linea.strip()
        
        # Verificamos si la línea contiene la etiqueta "Dirección:"
        if linea.startswith("Dire"):
            # Si contiene la etiqueta, extraemos la MAC (la dirección Bluetooth)
            # La MAC está después de los dos puntos, así que la dividimos por los dos puntos y tomamos el segundo elemento
            mac = linea.split(" ")[1].strip()
            # Imprimimos la MAC para que sea la salida del mapper
            print("{} 1".format(mac))

if __name__ == "__main__":
    mapper()  # Llamamos a la función mapper para ejecutar el mapeo
