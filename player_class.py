class Player:
    def __init__(self, placement, coins = 0) -> None:
        self.name = input('Enter a player name: ')
        self.placement = placement
        self.coins = 0

    def __str__(self) -> str:
        return f"Player: {self.name}, Coins: {self.coins}\nCurrent Position: {self.placement}"