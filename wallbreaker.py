#the main Model class
class Wallbreaker:
    def __init__(self):
       self.savedProcesses = self.loadProcesses()
       self.levels = self.loadLevels()

    #make a new process
    def newProcess(self):
        #TODO
        pass

    #load a process, and start a game
    def loadProcess(self, process):
        #TODO
        pass

    #load all saved games from file
    def loadProcesses(self):
        #TODO
        return []

    #load "all" levels from files
    def loadLevels(self):
        #TODO
        return []

#kind of a saved game
class Process:
    def __init__(self,name,settings):
        #TODO
        self.level = 0
        self.name = name
        self.settings = settings

    #start the actual level
    def startGame(self):
        #TODO
        pass

    #it will be used by class Game, when you beat a level
    def levelUp(self):
        self.level += 1

#there will be EASY, NORMAL, HARD and CUSTOM version,
# and if you choose one of them, the settings will be changed.
class Settings:
    def __init__(self, enumSettings):
        #TODO
        if enumSettings == 0:
            self.baseVelocity = 0.0
            self.baseBatWidth = 0
            self.bonusRate = 0
            self.penaltyRate = 0
        else:
            self.baseVelocity = 0.0
            self.baseBatWidth = 0
            self.bonusRate = 0
            self.penaltyRate = 0

#the loadGame() calls it
class Game:
    def __init__(self,level):
        #TODO
        self.level = self.loadLevel(level)
        self.balls = []
        self.balls.append(BallController())
        self.bat = BatController()

    #load level from file
    def loadLevel(self, level):
        #TODO
        pass

    #the actual game-mechanism
    def nextStep(self):
        #TODO
        pass

#the gamefield with bricks
class Level:
    def __init__(self):
        #TODO
        self.levelNumber = 0
        self.bricks = [[Brick()]]

    #check the given coords with the bricks, and returns with that
    def hit(self,x,y):
        #TODO
        pass

#a controller between the model and the view
class BallController:
    def __init__(self):
        #TODO
        self.ball = Ball()
        self.ballView = BallView()

    #make the ball move
    def move(self):
        #TODO
        pass

#a controller between the model and the view
class BatController:
    def __init__(self):
        #TODO
        self.bat = Bat()
        self.batView = BatView()

    #make the bat move
    def move(self):
        #TODO
        pass

#a controller between the model and the view
class BrickController:
    def __init__(self):
        #TODO
        self.brick = Brick()
        self.brickView = BrickView()

#model
class Ball:
    def __init__(self):
        #TODO
        self.textures = [Texture()]
        self.velocity = 0.0
        self.angle = 0.0

#model
class Bat:
    def __init__(self):
        #TODO
        self.textures = [Texture()]
        self.width = 0

#model
class Brick:
    def __init__(self):
        #TODO
        self.textures = [Texture()]
        self.hitRate = 0
        self.hitCount = 0
        self.broken = False

#interface
class ViewElement:
    def __iter__(self):
        #TODO
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
    def draw(self):
        #TODO
        pass

#view
class BallView(ViewElement):
    def __init__(self):
        #TODO
        pass
    def draw(self):
        #TODO
        pass

#view
class BatView(ViewElement):
    def __init__(self):
        #TODO
        pass
    def draw(self):
        #TODO
        pass

#view
class BrickView(ViewElement):
    def __init__(self):
        #TODO
        pass
    def draw(self):
        #TODO
        pass

#view
class ButtonView(ViewElement):
    def __init__(self):
        #TODO
        pass
    def draw(self):
        #TODO
        pass

#the main Controller
class MenuController:
    def __init__(self):
        #TODO
        self.wallBreaker = Wallbreaker()
        self.newButton = ButtonView()
        self.loadButton = ButtonView()