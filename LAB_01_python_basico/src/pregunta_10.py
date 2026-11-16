import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_10():
    """
    Para cada registro del archivo, en el mismo orden en que aparecen,
    retorne una tupla con la letra de la primera columna (`letter`), la
    cantidad de elementos de la cuarta columna (`codes`) y la cantidad de
    pares de la quinta columna (`metrics`). El resultado es una lista con una
    tupla por registro.

    Ejemplo del formato de la respuesta:

        [("E", 3, 5), ("A", 3, 4), ("B", 4, 4), ...]
    """
    registros = []

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 4:
                letra = columnas[0]
                cantidad_codes = len(columnas[3].split(","))
                cantidad_metrics = len(columnas[4].split(","))
                registros.append((letra, cantidad_codes, cantidad_metrics))

    return registros


if __name__ == "__main__":
    print(registros := pregunta_10())
