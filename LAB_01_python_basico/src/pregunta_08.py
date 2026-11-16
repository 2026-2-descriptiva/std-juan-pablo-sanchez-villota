import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_08():
    """
    Repita la pregunta 7, pero ahora cada lista de letras debe contener cada
    letra una sola vez y estar ordenada alfabéticamente. Retorne una lista de
    tuplas `(valor, letras)` ordenada por el valor.

    Ejemplo del formato de la respuesta:

        [(0, ["C"]), (1, ["B", "E"]), (2, ["A", "E"]), ...]
    """
    letras_por_valor = {}

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 1:
                letra = columnas[0]
                valor = int(columnas[1])
                # set() descarta automáticamente las letras repetidas
                letras_por_valor.setdefault(valor, set()).add(letra)

    return [
        (valor, sorted(letras)) for valor, letras in sorted(letras_por_valor.items())
    ]


if __name__ == "__main__":
    print(pregunta_08())
