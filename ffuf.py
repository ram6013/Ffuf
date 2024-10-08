import requests
import sys

def ffuf(url, diccionario, cookies = None):
    if "FFUF" not in url:
        print("Error 001: No se encuentra la palabra FFUF.")
        sys.exit(1)
    url = url.split("FFUF")[0]
    print(url)
    with open(diccionario, "r") as archivo:
        for linea in archivo: 
            palabra = linea.strip()
            objetivo = url + palabra 
            try:
                respuesta = requests.get(objetivo, cookies=cookies)
            except requests.exceptions.RequestException as e:
                print(f"Error al hacer la solicitud a {objetivo}: {e}")
                continue
            if respuesta.status_code == 200:
                print("(+)Ruta abierta encontrada: " + objetivo)
            elif respuesta.status_code == 301 or respuesta.status_code == 302:
                print("(--)Se ha encontrado una ruta de redirección: " + objetivo)
            elif respuesta.status_code == 403:
                print("(-)Se ha encontrado una ruta protegida: " + objetivo)

    


if len(sys.argv) < 3:
    print("Necesito que me des una url que contenga FFUF, un diccionario con las palabras a probar y ls coockies(opcional)")
    sys.exit(1)
url = sys.argv[1]
diccionario = sys.argv[2]
cookies = None
if len(sys.argv) == 4:
    cookies = {'session': sys.argv[3]}

ffuf(url, diccionario, cookies)
