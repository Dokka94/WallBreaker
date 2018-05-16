from ModelElements import *
from ViewElements import *
from math import sqrt
import time

# a controller between the model and the view
class BallController:
    def __init__(self):
        self.ball = Ball()

        self.stickedTo = None
        self.x_change = 0
        self.y_change = 0
        self.velocity = 10
        self.ballView = BallView(Constants.Border + Constants.Wall_width + Constants.Game_Screen_W/2-6,
                                 Constants.Border + Constants.Wall_width + Constants.Game_Screen_H-50-12,12,12,
                                 self)

    def stickTo(self, bat):
        self.stickedTo = bat

    def release(self):
        self.stickedTo = None
        self.x_change = 0
        self.y_change = -10


    def isOverlapped(self,controller):
        viewElement = controller.getView()
        # TODO: it could be easier with pygame spire collide
        ballcenter = (self.ballView.getx() + self.ballView.width/2, self.ballView.gety() + self.ballView.height/2)
        elementcenter = (viewElement.getx() + viewElement.width/2, viewElement.gety() + viewElement.height/2)

        diffy = elementcenter[1] - ballcenter[1]
        diffx = elementcenter[0] - ballcenter[0]

        if viewElement.getx() <= ballcenter[0] <= viewElement.getx() + viewElement.width:
            if abs(diffy) <= viewElement.height / 2 + self.ballView.height / 2:
                if diffy > 0:
                    return True, True, self.ballView.getx(), viewElement.gety() - self.ballView.height
                else:
                    return True, True, self.ballView.getx(), viewElement.gety() + viewElement.height
        if viewElement.gety() <= ballcenter[1] <= viewElement.gety() + viewElement.height:
            if abs(diffx) <= viewElement.width / 2 + self.ballView.width / 2:
                if diffx > 0:
                    return True, False, viewElement.getx() - self.ballView.width, self.ballView.gety()
                else:
                    return True, False, viewElement.getx() + viewElement.width, self.ballView.gety()
        return False, None, None, None


    # make the ball move
    def move(self, level, walls, bat):
        if self.stickedTo is not None:
            self.ballView.setx(self.stickedTo.batView.getx() + self.stickedTo.batView.width/2 - self.ballView.width / 2)
            self.ballView.sety(self.stickedTo.batView.gety() - self.ballView.height)
        else:
            self.ballView.setx(self.ballView.getx()+self.x_change)
            self.ballView.sety(self.ballView.gety()+self.y_change)

            brickGroup = pygame.sprite.Group()
            bricks = level.getRange(self.ballView.getx(), self.ballView.gety())
            for brick in bricks:
                brickGroup.add(brick.brickView)

            block_hit_list = pygame.sprite.spritecollide(self.ballView, brickGroup, False)
            for block in block_hit_list:
                if self.setBallReflect(self.isOverlapped(block.controller)):
                    block.controller.hit()
                    return

            wallGroup = pygame.sprite.Group()
            for wall in walls.wallViews:
                wallGroup.add(wall)
            block_hit_list = pygame.sprite.spritecollide(self.ballView, wallGroup, False)
            for block in block_hit_list:
                if self.setBallReflect(self.isOverlapped(block)):
                    return

            batGroup = pygame.sprite.Group()
            batGroup.add(bat.getView())
            block_hit_list = pygame.sprite.spritecollide(self.ballView, batGroup, False)
            for block in block_hit_list:
                if self.setBallReflect(self.isOverlapped(block.controller)):
                    ballCenterX = self.ballView.getx() + self.ballView.width / 2
                    batCenterX = block.getx() + block.width / 2
                    diff = batCenterX - ballCenterX
                    self.x_change = - int(diff / block.width * 9)
                    self.y_change = - sqrt(self.velocity**2 - self.x_change**2)
                    return

    def isOnPlayField(self):
        return self.ballView.gety() < Constants.Game_Screen_H

    def setBallReflect(self, params):
        reflect = params[0]
        horizontal = params[1]
        newx = params[2]
        newy = params[3]
        if reflect:
            if horizontal:
                self.x_change = self.x_change
                self.y_change = - self.y_change
            else:
                self.x_change = - self.x_change
                self.y_change = self.y_change
            self.ballView.setx(newx)
            self.ballView.sety(newy)
            return True
        return False


# a controller between the model and the view
class BatController:
    def __init__(self):
        self.bat = Bat()
        self.movementSpeed = 10
        self.batView = BatView(Constants.Border + Constants.Wall_width + Constants.Game_Screen_W/2-35,
                               Constants.Border + Constants.Wall_width + Constants.Game_Screen_H-50, 70, 20,
                               self)

    def changespeed(self, x):
        self.batView.x_change += x

    # make the bat move
    def move(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.changespeed(-self.movementSpeed)
            if event.key == pygame.K_RIGHT:
                self.changespeed(self.movementSpeed)

        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.changespeed(self.movementSpeed)
            if event.key == pygame.K_RIGHT:
                self.changespeed(-self.movementSpeed)

    def setWalls(self, wallController):
        for wallView in wallController.wallViews:
            self.batView.addWall(wallView)

    def getView(self):
        return self.batView

# a controller between the model and the view
class BrickController:
    def __init__(self, x, y, maxX, maxY, brickString):

        if brickString == "simple":
            self.brick = Brick()
        elif brickString == "double":
            self.brick = DoubleBrick()
        elif brickString == "triple":
            self.brick = TripleBrick()
        else:
            raise Exception("Not valid brickstring: " + brickString)
        self.brickView = BrickView(x, y, maxX, maxY, self)


    def hit(self):
        self.brick.hit()

    def getView(self):
        return self.brickView


class WallController:
    def __init__(self):
        self.wallViews = []

    def addWall(self, x, y, width, height):
        self.wallViews.append(WallView(x, y, width, height))
