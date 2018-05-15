from Game import *

# kind of a saved game
class Process:
    
    def __init__(self, screen, name):
        # TODO
        self.level = 0
        if name == "":
            self.name = "None"
        else:
            self.name = name
        self.settings = None
        self.screen = screen

    # start the actual level
    def startGame(self):
        # TODOv
        game = Game(self.level, self.screen)
        if game.start():
            self.levelUp()
            self.saveLevel()
            self.startGame()
            
    # it will be used by class Game, when you beat a level
    def levelUp(self):
        self.level += 1

    def saveLevel(self):
        d = {}
        with open("savedgames.txt") as f:
            for line in f:
                (key, val) = line.split()
                d[str(key)] = val
        d[self.name] = self.level
        with open("savedgames.txt", 'w') as out:
            for key, value in d.items():
                out.write(str(key) + " " + str(value) + "\n")

