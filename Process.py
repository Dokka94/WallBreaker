from Game import *

# kind of a saved game
class Process:
    
    def __init__(self, Screen_Width, Screen_Height, Screen, Game_Screen_W, Game_Screen_H):
        # TODO
        '''self.level = 0
        self.name = name
        self.settings = settings'''
        self.Screen_Width = Screen_Width
        self.Screen_Height = Screen_Height
        self.Screen = Screen
        self.Game_Screen_W = Game_Screen_W
        self.Game_Screen_H = Game_Screen_H

    # start the actual level
    def startGame(self, numofBricks, rowNumOfBricks, brickDistance):
        # TODOv
        Game(self.Screen_Width, self.Screen_Height,\
             self.Screen,numofBricks,rowNumOfBricks,brickDistance,\
              self.Game_Screen_W, self.Game_Screen_W).nextStep()
            
    # it will be used by class Game, when you beat a level
    def levelUp(self):
        self.level += 1
