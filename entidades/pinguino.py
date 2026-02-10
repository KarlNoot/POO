class Pinguino:
    def __init__ (self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def saludar (self):
        #Esta funcion  va a hacer que el pinguino salude
        return f"Hola, me llamo {self.nombre}"
    