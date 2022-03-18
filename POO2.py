


def main():
    class Persona():
        def __init__(self):
            self.nombre = input("ingrese el nombre: ")
            self.apellido = input("ingrese el apellido: ")
            self.direccion = input("ingrese la direccion: ")
            self.telefono = input("ingrese el telefono: ")
            
    
        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}") 

   

    class Empleado(Persona):
        def __init__(self):
            super().__init__()
            self.__sueldo = float (input("ingrese el sueldo: "))
            self.alimentacion = 0
            self.transporte = 0
            self.pension = 0
        
            if self.__sueldo < 2000000:
                self.alimentacion = 80000
                self.transporte = 60000
                self.pension = 0
            else:
                self.alimentacion = 0
                self.transporte = 0

            self.pension = self.__sueldo *0.04
            self.salud = self.__sueldo * 0.0375
            
            
            self.dev = self.alimentacion + self.transporte
                
            
            
            self.ded = self.pension + self.salud
            
        
        def mostrarempleados(self):
            super().mostrarPersona()
            print(f"Sueldo: {self.__sueldo}")
            print(f"Devengado: {self.dev}")
            print(f"Deducciones: {self.ded}")
            print(f"Total a pagar: {self.pension + self.__sueldo + self.dev + self.ded}")

        def calcularDevengado():
            dev = self.__sueldo
        
    
    empleado1 = Empleado()
    #empleado1.sueldo = 4000000
    empleado1.mostrarempleados()






if __name__=="__main__":
    main()