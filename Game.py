from Controllers import *


# the loadGame() calls it
class Game:
    def __init__(self, level):
        # TODO
        self.level = self.loadLevel(level)
        self.balls = []
        self.balls.append(BallController())
        self.bat = BatController()

    # load level from file
    def loadLevel(self, level):
        # TODO
        pass

    # the actual game-mechanism
    def nextStep(self):
        # TODO
        pass