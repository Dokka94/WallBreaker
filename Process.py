from Game import *

# kind of a saved game
class Process:
    
    def __init__(self, screen):
        # TODO
        self.level = 0
        self.name = "Example"
        self.settings = None
        self.screen = screen

    # start the actual level
    def startGame(self, numofBricks, rowNumOfBricks, brickDistance):
        # TODOv
        game = Game(self.level, self.screen)
        game.start()
            
    # it will be used by class Game, when you beat a level
    def levelUp(self):
        self.level += 1
