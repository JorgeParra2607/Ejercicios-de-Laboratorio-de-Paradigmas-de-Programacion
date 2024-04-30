# Clase Hexágono Regular
class HexagonoRegular:
    def __init__(self, color, lado):
        self.color = color
        self.lado = lado

    def area(self):
        return (3 * (3 ** 0.5) * self.lado ** 2) / 2

    def perimetro(self):
        return 6 * self.lado

    def __str__(self):
        return (
            f"\nHexágono Regular:\n"
            f"Color: {self.color}\n" 
            f"Lado= {self.lado}\n"
            f"Área= {self.area()}\n"
            f"Perímetro= {self.perimetro()}\n"
        )

# Clase Rombo
class Rombo:
    def __init__(self, color, diagonal_mayor, diagonal_menor):
        self.color = color
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def perimetro(self):
        return 4 * (self.diagonal_mayor ** 2 + self.diagonal_menor ** 2) ** 0.5

    def __str__(self):
        return (
            f"Rombo:\n"
            f"Color: {self.color}\n"
            f"Diagonal Mayor= {self.diagonal_mayor}\n"
            f"Diagonal Menor= {self.diagonal_menor}\n"
            f"Área= {self.area()}\n"
            f"Perímetro= {self.perimetro()}\n"
        )

# Clase Trapecio
class Trapecio:
    def __init__(self, color, base_mayor, base_menor, altura):
        self.color = color
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura

    def area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def perimetro(self):
        return self.base_mayor + self.base_menor + 2 * (self.altura ** 2 + ((self.base_mayor - self.base_menor) / 2) ** 2) ** 0.5

    def __str__(self):
        return (
            f"Trapecio:\n" 
            f"Color: {self.color}\n"
            f"Base Mayor= {self.base_mayor}\n"
            f"Base Menor= {self.base_menor}\n"
            f"Altura= {self.altura}\n"
            f"Área= {self.area()}\n"
            f"Perímetro= {self.perimetro()}\n"
        )


hexagono = HexagonoRegular("Azul", 5)
print(hexagono)

rombo = Rombo("Rojo", 4, 6)
print(rombo)

trapecio = Trapecio("Verde", 5, 3, 4)
print(trapecio)
