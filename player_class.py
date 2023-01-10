class Player:
    def __init__(self, placement, coins = 0) -> None:
        self.name = input('Enter a player name: ')
        self.placement = placement
        self.coins = 0


    def __str__(self) -> str:
        return f"Player: {self.name}, Coins: {self.coins}\nCurrent Position: {self.placement}"


    def get_move(self, valid_move:list)->str:
        '''Gets the from the player'''
        print("You can move ", end ="")
        for direction in valid_move:
            print(direction,end=", ")
        movement = input("Enter a direction")
        while not self.check_move(movement, valid_move):
            print("Please pick a valid direction.")
            movement = input("Enter a direction")
    

    def check_move(self,movement, valid_moves):
        '''Checks if a movement is valid'''
        if movement in valid_moves:
            return True
        return False


    def move(self, movement):
        '''updates the current placement depending on the direction moved'''
        if movement == "n":
            pass
        elif movement == "s":
            pass
        elif movement == "e":
            pass
        elif movement == "w":
            pass