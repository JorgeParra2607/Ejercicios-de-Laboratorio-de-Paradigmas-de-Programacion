class Robot:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.path = []

    def is_safe(self, x, y):
        return 0 <= x < self.rows and 0 <= y < self.cols and self.grid[x][y] == 0

    def find_path(self, x=0, y=0):
        if not self.is_safe(x, y):
            return False

        self.path.append((x, y))

        if x == self.rows - 1 and y == self.cols - 1:
            return True

        if self.find_path(x + 1, y) or self.find_path(x, y + 1):
            return True

        self.path.pop()
        return False

    def get_path(self):
        if self.find_path():
            return f"La ruta es: {self.path}"
        else:
            return "No se encontró una ruta."

# Ejemplo de uso
grid = [
    [0, 0, 1],
    [0, 0, 0],
    [0, 0, 0]
]

robot = Robot(grid)
print('\n')
print(robot.get_path())

