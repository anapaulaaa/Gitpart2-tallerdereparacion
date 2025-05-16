from equipos import Equipo

class Cliente:
    def __init__(self):
        self.__apellidos = ""
        self.__nombres = ""
        self.__telefono = ""
        self.__equipos = []

    def ingresar_datos(self, apellidos, nombres, telefono):
        self.apellidos = apellidos
        self.nombres = nombres
        self.telefono = telefono
        self.equipos = []

    def agregar_equipo(self, equipo):
        if isinstance(equipo, Equipo):
            self.equipos.append(equipo)

    def ver_equipos(self):
        if not self.equipos:
            print("Este cliente no tiene equipos registrados.")
        else:
            for i, equipo in enumerate(self.equipos, 1):
                print(f"\nEquipo {i}:")
                print(equipo)

    def __str__(self):
        return f"{self.nombres} {self.apellidos} - Tel: {self.telefono}"

    @property
    def nombres(self):
        return self.__nombres

    @nombres.setter
    def nombres(self, value):
        self.__nombres = value

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, value):
        self.__apellidos = value

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, value):
        self.__telefono = value

    @property
    def equipos(self):
        return self.__equipos

    @equipos.setter
    def equipos(self, value):
        self.__equipos = value

