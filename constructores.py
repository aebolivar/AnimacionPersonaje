from fabricas import *
from guerrero import *

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getHeroe(self):
        guerrero = Guerrero()
        guerrero.set_sprites(self.__builder.get_sprites())

        return guerrero

class Constructor():
    def get_sprites(self): pass

class ConstructorGuerreros():
    def __init__(self):
        self.fabrica = FabricaSpritesGuerrero()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]


class ConstructorEnemigos():
    def __init__(self):
        self.fabrica = FabricaSpritesEnemigo()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]

class ConstructorMonstruos():
    def __init__(self):
        self.fabrica = FabricaSpritesMonstruo()

    def get_sprites(self):
        return [self.fabrica.crear_derecha(),
                self.fabrica.crear_izquierda(),
                self.fabrica.crear_abajo(),
                self.fabrica.crear_arriba()]