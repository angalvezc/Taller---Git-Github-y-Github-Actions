import estudiantes.registro as registro

def main():
    
    nombre_archivo = 'estudiantes.csv'

    estudiantes = registro.cargar_estudiantes(nombre_archivo)

   
    registro.mostrar_estudiantes_tabla(estudiantes)

   
    registro.calcular_promedio(estudiantes)

if __name__ == "__main__":
    main()
