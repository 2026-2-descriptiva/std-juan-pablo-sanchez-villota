import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_12():
    """
    Para cada letra de la primera columna (`letter`), sume todos los valores
    numéricos de los pares `clave:valor` de la quinta columna (`metrics`).
    Retorne un diccionario `{letra: suma}` con las letras en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"A": 177, "B": 187, "C": 114, ...}
    """
    sumas = {}

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 4:
                letra = columnas[0]
                for par in columnas[4].split(","):
                    valor = int(par.split(":")[1])  # la parte derecha del par
                    sumas[letra] = sumas.get(letra, 0) + valor

    return dict(sorted(sumas.items()))


if __name__ == "__main__":
    print(pregunta_12())
