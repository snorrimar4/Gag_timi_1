class Grid:
    def __init__(self) -> None:
        self.x = int(input("Enter the grid's X value: "))
        self.y = int(input("Enter the grid's Y value: "))
        self.dimension = self.x, self.y

    def __str__(self):
        return f"Grid's dimension: {self.x}x{self.y}"


g1 = Grid()
print(g1)