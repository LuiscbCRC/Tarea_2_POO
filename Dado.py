from random import *

class Dado:

    caras=0

    #este atributo no estaba en el modelo explícitamente
    #pero se necesita para poder crear los números aleatorios
    rnd=Random(42)

    def __init__(self, numCaras):
        self.caras=numCaras
    
    def lanzar(self):
        return self.rnd.randint(1, self.caras)
