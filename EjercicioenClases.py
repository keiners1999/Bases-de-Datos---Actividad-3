#
#Calcular Devengado

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
            self.pension=(self.__sueldo*0.04)
            self.salud= (self.__sueldo*0.0375)

            if self.__sueldo <2000000:
                self.alimentacion= 80000
                self.transporte= 60000
            else:
                self.alimentacion= 0
                self.transporte= 0

            self.sueldoDevengado = self.__sueldo + self.alimentacion + self.transporte
            self.sueldoDeducciones = self.__sueldo - self.pension - self.salud
        def mostrarEmpleado(self):
            super().mostrarPersona()
            print(f"Transporte: {self.transporte}")
            print(f"Alimentación: {self.alimentacion}")
            print(f"Pensión: {self.pension}")
            print(f"Salud: {self.salud}")
            print(f"Sueldo DEVENGADO: {self.sueldoDevengado}") 
            print(f"Sueldo DEDUCCIONES {self.sueldoDeducciones}")

    empleado1 =Empleado()
    empleado1.mostrarEmpleado()


if __name__ == "__main__":
    main()