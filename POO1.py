


def main():
    class Persona():
        nombre = "Dilan"
        apellido = "Ramirez"
        direccion = "cll 20"
        telefono = "3003144957"


        def mostrarPersona(self):
            print(f"Nombre: {self.nombre} {self.apellido}") 
    persona1 = Persona()
    persona1.nombre = "Pepe"
    persona1.mostrarPersona()

    persona2 = Persona()
    persona2.nombre = "Alan"
    persona2.apellido = "Brito"
    persona2.direccion = "cll 38"
    persona2.telefono = "300098712"
    persona2.mostrarPersona()

    persona3 = Persona()
    persona3.nombre = "Monica"
    persona3.apellido = "Galindo"
    persona3.direccion = "cll 15"
    persona3.telefono = "30109392"
    persona3.mostrarPersona()



if __name__=="__main__":
    main()