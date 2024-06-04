import math

class Figure:
    def __init__(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def perimeter(self):
        pass  # Implementar en las clases derivadas

    def area(self):
        pass  # Implementar en las clases derivadas

class Triangle(Figure):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def perimeter(self):
        return 3 * self.base

    def area(self):
        return 0.5 * self.base * self.height

class Circle(Figure):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Figure):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

class Hexagon(Figure):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def perimeter(self):
        return 6 * self.side

    def area(self):
        return (3 * math.sqrt(3) / 2) * self.side ** 2

# Ejemplo de uso
triangulo = Triangle("Rojo", 5, 4)
print(f"Triángulo - Color: {triangulo.getColor()}, Perímetro: {triangulo.perimeter()}, Área: {triangulo.area()}")

circulo = Circle("Azul", 3)
print(f"Círculo - Color: {circulo.getColor()}, Perímetro: {circulo.perimeter()}, Área: {circulo.area()}")

rectangulo = Rectangle("Verde", 6, 8)
print(f"Rectángulo - Color: {rectangulo.getColor()}, Perímetro: {rectangulo.perimeter()}, Área: {rectangulo.area()}")

hexagono = Hexagon("Amarillo", 7)
print(f"Hexágono - Color: {hexagono.getColor()}, Perímetro: {hexagono.perimeter()}, Área: {hexagono.area()}")
