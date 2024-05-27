from abc import ABC, abstractmethod
import math

# Clase base abstracta Figure
class Figure(ABC):
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass

# Clase Triangle que hereda de Figure
class Triangle(Figure):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2
        return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

# Clase Circle que hereda de Figure
class Circle(Figure):
    def __init__(self, color, radio):
        super().__init__(color)
        self.radio = radio

    def perimetro(self):
        return 2 * math.pi * self.radio

    def area(self):
        return math.pi * self.radio ** 2

# Clase Rectangle que hereda de Figure
class Rectangle(Figure):
    def __init__(self, color, ancho, alto):
        super().__init__(color)
        self.ancho = ancho
        self.alto = alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)

    def area(self):
        return self.ancho * self.alto

# Clase Hexagon que hereda de Figure
class Hexagon(Figure):
    def __init__(self, color, lado):
        super().__init__(color)
        self.lado = lado

    def perimetro(self):
        return 6 * self.lado

    def area(self):
        return (3 * math.sqrt(3) * self.lado ** 2) / 2

# Demostración del Polimorfismo
def main():
    # Crear instancias de cada clase de figura
    figuras = [
        Triangle("Rojo", 3, 5, 7),
        Circle("Azul", 5),
        Rectangle("Verde", 2, 5),
        Hexagon("Amarillo", 7)
    ]

    # Imprimir detalles de cada figura
    for figura in figuras:
        print(f"Clase: {figura.__class__.__name__}")
        print(f"Color: {figura.getColor()}")
        print(f"Perímetro: {figura.perimetro()}")
        print(f"Área: {figura.area()}")
        print()

# Ejecutar la función principal
if __name__ == "__main__":
    main()
