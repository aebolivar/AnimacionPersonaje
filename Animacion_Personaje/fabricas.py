from productos import *

class FabricaAbstracta():
    def crear_izquierda(self): pass
    def crear_derecha(self): pass
    def crear_arriba(self): pass
    def crear_abajo(self): pass

class FabricaSpritesGuerrero(FabricaAbstracta):

    def crear_izquierda(self):
        izquierda = IzquierdaGuerrero()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaGuerrero()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaGuerrero()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoGuerrero()
        return abajo.get_sprites()

class FabricaSpritesEnemigo(FabricaAbstracta):
    def crear_izquierda(self):
        izquierda = IzquierdaEnemigo()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaEnemigo()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaEnemigo()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoEnemigo()
        return abajo.get_sprites()

class FabricaSpritesMonstruo(FabricaAbstracta):

    def crear_izquierda(self):
        izquierda = IzquierdaMonstruo()
        return izquierda.get_sprites()

    def crear_derecha(self):
        derecha = DerechaMonstruo()
        return derecha.get_sprites()

    def crear_arriba(self):
        arriba = ArribaMonstruo()
        return arriba.get_sprites()

    def crear_abajo(self):
        abajo = AbajoMonstruo()
        return abajo.get_sprites()