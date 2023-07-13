from abc import ABC, abstractmethod

#Producto abstracto
class Lipstick(ABC):
    @abstractmethod
    def apply(self):
        pass

#Productos concretos
class MatteLipstick(Lipstick):
    def apply(self):
        print("Aplicando labial matte")

class GlossyLipstick(Lipstick):
    def apply(self):
        print("Aplicando gloss")


#Creador abstracto.
class LipstickFactory(ABC):
    @abstractmethod
    def create_lipstick(self):
        pass

#Creador concreto
#implementa método create_lipstick() de la clase Lipstick
class ConcreteLipstickFactory(LipstickFactory):
    def create_lipstick(self, lipstick_type):
        if lipstick_type == "matte":
            return MatteLipstick()
        elif lipstick_type == "glossy":
            return GlossyLipstick()
        else:
            return None

# Creación de la factoría y los labiales
factory = ConcreteLipstickFactory()

matte_lipstick = factory.create_lipstick("matte")
glossy_lipstick = factory.create_lipstick("glossy")

# Aplicación de los labiales
matte_lipstick.apply()  
glossy_lipstick.apply()  
