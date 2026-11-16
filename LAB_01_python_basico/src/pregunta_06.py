import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_06():
    """
    La quinta columna (`metrics`) contiene pares `clave:valor` separados por
    comas. Para cada clave, encuentre el valor mínimo y el valor máximo que
    aparecen en todo el archivo. Retorne una lista de tuplas
    `(clave, mínimo, máximo)` ordenada alfabéticamente por la clave.

    Observe que el orden es mínimo y luego máximo, al contrario de la
    pregunta 5.

    Ejemplo del formato de la respuesta:

        [("aaa", 1, 9), ("bbb", 1, 9), ...]
    """
    valores = {}

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 4:
                # La quinta columna luce así: "aaa:1,bbb:2,ccc:3"
                for par in columnas[4].split(","):
                    clave, valor = par.split(":")
                    valores.setdefault(clave, []).append(int(valor))

    return [(clave, min(lista), max(lista)) for clave, lista in sorted(valores.items())]


if __name__ == "__main__":
    print(pregunta_06())
