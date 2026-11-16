import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_05():
    """
    Para cada letra de la primera columna (`letter`), encuentre el valor
    máximo y el valor mínimo de la segunda columna (`value`). Retorne una lista
    de tuplas `(letra, máximo, mínimo)` ordenada alfabéticamente por la letra.

    Ejemplo del formato de la respuesta:

        [("A", 9, 2), ("B", 9, 1), ...]
    """
    valores = {}

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 1:
                letra = columnas[0]
                valor = int(columnas[1])
                # Si la letra no existe aún, arranca con una lista vacía
                valores.setdefault(letra, []).append(valor)

    return [(letra, max(lista), min(lista)) for letra, lista in sorted(valores.items())]


if __name__ == "__main__":
    print(pregunta_05())
