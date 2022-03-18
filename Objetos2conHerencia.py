def main():
    class Persona():
        def __init__(self):
            self.nombre =input("Ingrese el nombre ")
            self.apellido=input("Ingrese el apellido ")
            self.direccion=input("Ingrese la dirección ")
            self.telefono=input("Ingrese su numero de teléfono ")

        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}")
        
    class Empleado(Persona):
        def __init__(self):
            super().__init__()

            self.__sueldo= float(input("Ingrese el sueldo:   ")) #El __ es para que la variable no pueda ser modificada por fuera
            self.alimentacion= 0
            self.transporte= 0
            self.pension=0

        def mostrarEmpleado(self):
            super().mostrarPersona()
            print(f"Sueldo: {self.__sueldo}") #Hay que hacer el llamado con el __ tal como se definio
            print(f"Transporte: {self.transporte}")
            print(f"Alimentación: {self.alimentacion}")
            print(f"Pensión: {self.pension}")

    empleado1 =Empleado()
    empleado1.mostrarEmpleado()


if __name__ == "__main__":
    main()