import csv

def importarCsv():
    datos = []
    with open('estudiantes.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            row[1] = float(row[1])
            if row[1] < 0 or row[1] > 5:
                print("Las notas deben estar entre 0 y 5")
            else:
                datos.append(row)
    
    print(datos)
    return datos

importarCsv()