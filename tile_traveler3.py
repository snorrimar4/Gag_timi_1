'''
TODO: Player Class, getur valið nafn
TODO: Board?
TODO: Tile Class
TODO: Lever Class
TODO: Random coins, FASTI SEM HELDUR UTAN UM FJÖLDA PENINGA
TODO: Grid implementation
TODO: Random coin amont
TODO: Stækkanlegt map
TODO: Miðjureitir eru upp,niður,hægri, vinstri
TODO: Vinstri veggir: leyfa ekki að fara til vinstri, sama með hægri veggi og top og bottom veggi. Leyfa ekki að fara í þá átt sem þeir snúa í.
TODO: Player er með update og get current position
TODO: Winning position is always (max,min)
'''
import random
STARTING_POINT = (1,1)
AMOUNT_OF_COINS = random.randint(1,100)

class Tile:
    def __init__(self) -> None:
        pass

class Player:
    def __init__(self, placement, coins = 0) -> None:
        self.name = input('Enter a player name: ')
        self.placement = placement
        self.coins = 0

    def __str__(self) -> str:
        return f"Player: {self.name}, Coins: {self.coins}\nCurrent Position: {self.placement}"

class Lever:
    def __init__(self, coins_dispensed) -> None:
        self.coins_dispensed = coins_dispensed
        self.coins_max = AMOUNT_OF_COINS

class Grid:
    def __init__(self, dimension) -> None:
        self.dimension = int(input("Enter the grid dimensions: "))

p1 = Player(STARTING_POINT)
#p2 = Player(STARTING_POINT)
print(p1)
