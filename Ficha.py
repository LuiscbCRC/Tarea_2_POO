from Dado import *

class Ficha:
    color = ""
    posicion = 0

    #no era parte del modelo, pero la Ficha necesita usar un dado
    #este atributo se define en las relaciones entre clases
    dado = Dado(6)
    
    
    def __init__(self, color):
        self.color = color
        self.posicion = 0
    
    def avanzar(self):
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(self.posicion)
    


