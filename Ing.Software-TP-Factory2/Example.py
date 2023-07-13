from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def draw(self):
        pass

class LineFigure(Figure):
    def draw(self):
        print("Dibujando figura de línea")

    def down_click(self):
        print("Click abajo")

    def drag(self):
        print("Arrastrando")

    def up_click(self):
        print("Click arriba")

class TextFigure(Figure):
    def draw(self):
        print("Dibujando figura de texto")

    def down_click(self):
        print("Click abajo")

    def drag(self):
        print("Arrastrando")

    def up_click(self):
        print("Click arriba")

class Manipulator(ABC):
    @abstractmethod
    def create_figure(self):
        pass

    @abstractmethod
    def down_click(self):
        pass

    @abstractmethod
    def drag(self):
        pass

    @abstractmethod
    def up_click(self):
        pass

class ConcreteLineManipulatorFactory(Manipulator):
    def create_figure(self):
        return LineFigure()

    def down_click(self):
        print("Click abajo")

    def drag(self):
        print("Arrastrando")

    def up_click(self):
        print("Click arriba")

class ConcreteTextManipulatorFactory(Manipulator):
    def create_figure(self):
        return TextFigure()

    def down_click(self):
        print("Click abajo")

    def drag(self):
        print("Arrastrando")

    def up_click(self):
        print("Click arriba")


line_factory = ConcreteLineManipulatorFactory()
line_figure = line_factory.create_figure()
line_figure.draw()
line_figure.down_click()
line_figure.drag()
line_figure.up_click()

text_factory = ConcreteTextManipulatorFactory()
text_figure = text_factory.create_figure()
text_figure.draw()
text_figure.down_click()
text_figure.drag()
text_figure.up_click()
