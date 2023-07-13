from abc import ABC, abstractmethod

class Lipstick(ABC):
    @abstractmethod
    def apply(self):
        pass

    @abstractmethod
    def moisturize_lips(self):
        pass

class MatteLipstick(Lipstick):
    def apply(self):
        print("Aplicando labial matte")

    def moisturize_lips(self):
        print("Hidratando labios con labial matte")

class GlossyLipstick(Lipstick):
    def apply(self):
        print("Aplicando gloss")

    def moisturize_lips(self):
        print("Hidratando labios con gloss")

class LipstickFactory(ABC):
    @abstractmethod
    def create_lipstick(self):
        pass

class ConcreteLipstickFactory(LipstickFactory):
    def create_lipstick(self, lipstick_type):
        if lipstick_type == "matte":
            return MatteLipstick()
        elif lipstick_type == "glossy":
            return GlossyLipstick()
        else:
            return None

# Uso de la fábrica de labiales
factory = ConcreteLipstickFactory()

matte_lipstick = factory.create_lipstick("matte")
glossy_lipstick = factory.create_lipstick("glossy")

matte_lipstick.apply()
matte_lipstick.moisturize_lips()

glossy_lipstick.apply()
glossy_lipstick.moisturize_lips()