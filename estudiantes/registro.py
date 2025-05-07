import csv
def cargar_estudiantes(nombre_archivo):
    estudiantes_validos = []

    with open(nombre_archivo, newline='', encoding='utf-8') as archivo_csv:
        lector = csv.DictReader(archivo_csv)
        for fila in lector:
            try:
                nota = float(fila["Nota"])
                if 0.0 <= nota <= 5.0:
                    estudiantes_validos.append({
                        "Nombre": fila["Nombre"],
                        "Nota": nota
                    })
                else:
                    print(f"Nota fuera de rango para {fila['Nombre']}: {nota}")
            except ValueError:
                print(f"Nota inválida para {fila['Nombre']}: {fila['Nota']}")

    return estudiantes_validos



