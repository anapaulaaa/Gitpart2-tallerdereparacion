from clientes import Cliente
from equipos import Equipo

clientes = []

def buscar_cliente(nombre):
    for cliente in clientes:
        if cliente.nombres.lower() == nombre.lower():
            return cliente
    return None

def menu():
    while True:
        print("\n--- Taller de Reparación ---")
        print("1. Ingresar Cliente")
        print("2. Ver Clientes")
        print("3. Agregar Equipo")
        print("4. Ver Equipos por Cliente")
        print("5. Salir")
        print("-" * 40)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            apellidos = input("Apellidos: ")
            nombres = input("Nombres: ")
            telefono = input("Teléfono: ")
            c = Cliente()
            c.ingresar_datos(apellidos, nombres, telefono)
            clientes.append(c)
            print("Cliente agregado exitosamente.")

        elif opcion == "2":
            if not clientes:
                print("No hay clientes registrados.")
            else:
                for c in clientes:
                    print(c)

        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente: ")
            cliente = buscar_cliente(nombre)
            if cliente:
                numero_parte = input("Número de Parte: ")
                tipo = input("Tipo de equipo (teléfono, portátil, PC, etc.): ")
                descripcion = input("Descripción del problema: ")
                eq = Equipo()
                eq.ingresar_equipo(numero_parte, tipo, descripcion)
                cliente.agregar_equipo(eq)
                print("Equipo agregado al cliente.")
            else:
                print("Cliente no encontrado.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del cliente: ")
            cliente = buscar_cliente(nombre)
            if cliente:
                cliente.ver_equipos()
            else:
                print("Cliente no encontrado.")

        elif opcion == "5":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()
