def main():
    class Persona():
        def __init__(self):
            self.nombre =input("Ingrese el nombre")
            self.apellido=input("Ingrese el apellido")
            self.direccion=input("Ingrese la dirección")
            self.telefono=input("Ingrese su numero de teléfono")

        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
        
    persona1 = Persona()
    persona1.mostrarPersona()

    persona2 = Persona()
    persona2.mostrarPersona()

if __name__ == "__main__":
    main()