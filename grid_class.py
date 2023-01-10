class Grid:
    def __init__(self, dimension) -> None:
        self.dimension = tuple(input("Enter the grid's dimension: "))

    def __str__(self):
        return f"{self.dimension}"