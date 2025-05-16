class Equipo:
    def __init__(self):
        self.__numero_parte = ""
        self.__tipo = ""
        self.__descripcion = ""

    def ingresar_equipo(self, numero_parte, tipo, descripcion):
        self.numero_parte = numero_parte
        self.tipo = tipo
        self.descripcion = descripcion

    def __str__(self):
        return f"Número de Parte: {self.numero_parte}, Tipo: {self.tipo}, Problema: {self.descripcion}"

    @property
    def numero_parte(self):
        return self.__numero_parte

    @numero_parte.setter
    def numero_parte(self, value):
        self.__numero_parte = value

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, value):
        self.__tipo = value

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, value):
        self.__descripcion = value
