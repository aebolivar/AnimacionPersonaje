import util

class Abajo():
    def get_sprites(self): pass

class AbajoGuerrero(Abajo):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/ABG1.png'),
                util.cargar_imagen('imagenes/ABG2.png'),
                util.cargar_imagen('imagenes/ABG3.png')]

class AbajoEnemigo(Abajo):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/ABE1.png'),
                util.cargar_imagen('imagenes/ABE2.png'),
                util.cargar_imagen('imagenes/ABE3.png')]

class AbajoMonstruo(Abajo):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/ABM1.png'),
                util.cargar_imagen('imagenes/ABM2.png'),
                util.cargar_imagen('imagenes/ABM3.png')]

class Arriba():
    def get_sprites(self): pass

class ArribaGuerrero(Arriba):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/AG1.png'),
                util.cargar_imagen('imagenes/AG2.png'),
                util.cargar_imagen('imagenes/AG3.png')]

class ArribaEnemigo(Arriba):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/AE1.png'),
                util.cargar_imagen('imagenes/AE2.png'),
                util.cargar_imagen('imagenes/AE3.png')]

class ArribaMonstruo(Arriba):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/AM1.png'),
                util.cargar_imagen('imagenes/AM2.png'),
                util.cargar_imagen('imagenes/AM3.png')]

class Derecha():
    def get_sprites(self): pass

class DerechaGuerrero(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/DG1.png'),
                util.cargar_imagen('imagenes/DG2.png'),
                util.cargar_imagen('imagenes/DG3.png')]

class DerechaEnemigo(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/DE1.png'),
                util.cargar_imagen('imagenes/DE2.png'),
                util.cargar_imagen('imagenes/DE3.png')]

class DerechaMonstruo(Derecha):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/DM1.png'),
                util.cargar_imagen('imagenes/DM2.png'),
                util.cargar_imagen('imagenes/DM3.png')]

class Izquierda():
    def get_sprites(self): pass

class IzquierdaGuerrero(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/IG1.png'),
                util.cargar_imagen('imagenes/IG2.png'),
                util.cargar_imagen('imagenes/IG3.png')]

class IzquierdaEnemigo(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/IE1.png'),
                util.cargar_imagen('imagenes/IE2.png'),
                util.cargar_imagen('imagenes/IE3.png')]
                
class IzquierdaMonstruo(Izquierda):
    def get_sprites(self):
        return [util.cargar_imagen('imagenes/IM1.png'),
                util.cargar_imagen('imagenes/IM2.png'),
                util.cargar_imagen('imagenes/IM3.png')]