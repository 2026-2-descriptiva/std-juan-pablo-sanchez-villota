import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_07():
    """
    Para cada valor distinto de la segunda columna (`value`), construya la
    lista de letras de la primera columna (`letter`) que aparecen con ese
    valor. Conserve las letras repetidas y el orden en que aparecen en el
    archivo. Retorne una lista de tuplas `(valor, letras)` ordenada por el
    valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["E", "B", "E"]), (2, ["A", "E"]), ...]
    """
    letras_por_valor = {}

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 1:
                letra = columnas[0]
                valor = int(columnas[1])
                letras_por_valor.setdefault(valor, []).append(letra)

    return sorted(letras_por_valor.items())


if __name__ == "__main__":
    print(pregunta_07())
