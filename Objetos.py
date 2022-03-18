

def main():
    class Persona():
        nombre = "Keiners"
        apellido = "Barraza"
        direccion = "Calle 14 Abis #36-54"
        telefono = "3012511784"

        #Definimos el metodo
        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")

    persona1 = Persona() #Creando una instancia de la Clase

    persona1.mostrarPersona()

    persona2 = Persona()
    persona2.nombre = "Carlos"
    persona2.apellido = "Valderrama"
    persona2.direccion = "Buenos Aires"
    persona2.telefono = "3051512"

    persona2.mostrarPersona()

if __name__ == "__main__":
    main()