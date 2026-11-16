import gzip
import os

ruta_archivo = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "..", "data", "data.csv.gz"
)


def pregunta_09():
    """
    Cuente cuántas veces aparece cada clave en la quinta columna (`metrics`)
    de todo el archivo. Retorne un diccionario `{clave: cantidad}` con las
    claves en orden alfabético.

    Ejemplo del formato de la respuesta:

        {"aaa": 13, "bbb": 16, "ccc": 23, ...}
    """
    conteo = {}

    with gzip.open(ruta_archivo, "rt") as archivo:
        for linea in archivo:
            columnas = linea.strip().split("\t")
            if len(columnas) > 4:
                for par in columnas[4].split(","):
                    clave = par.split(":")[0]  # solo interesa la clave
                    conteo[clave] = conteo.get(clave, 0) + 1

    return dict(sorted(conteo.items()))


if __name__ == "__main__":
    print(pregunta_09())
