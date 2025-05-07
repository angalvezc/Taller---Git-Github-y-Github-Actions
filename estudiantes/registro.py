import csv

def cargar_estudiantes(nombre_archivo):
    estudiantes_validos = []

    try:
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
    except FileNotFoundError:
        print(f"Archivo no encontrado: {nombre_archivo}")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

    return estudiantes_validos

def mostrar_estudiantes_tabla(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x["Nombre"])
    print("\n{:<20} {:>5}".format("Nombre", "Nota"))
    print("-" * 26)
    for est in estudiantes_ordenados:
        print("{:<20} {:>5.2f}".format(est["Nombre"], est["Nota"]))



