

# kind of a saved game
class Process:
    def __init__(self, name, settings):
        # TODO
        self.level = 0
        self.name = name
        self.settings = settings

    # start the actual level
    def startGame(self):
        # TODO
        pass

    # it will be used by class Game, when you beat a level
    def levelUp(self):
        self.level += 1