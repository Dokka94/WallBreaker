from ModelElements import *
from ViewElements import *

# a controller between the model and the view
class BallController:
    def __init__(self):
        # TODO
        self.ball = Ball()
        self.ballView = BallView(Constants.Border + Constants.Wall_width + Constants.Game_Screen_W/2-6,
                                 Constants.Border + Constants.Wall_width + Constants.Game_Screen_H-50-12,12,12)
        self.stickedTo = None
        self.x_change = 0
        self.y_change = 0

    def stickTo(self, bat):
        self.stickedTo = bat

    def release(self):
        self.stickedTo = None
        self.x_change = -7
        self.y_change = -5


    def isOverlapped(self, controller):
        viewElement = controller.getView()
        #TODO: it could be easier with pygame spire collide
        ballcenter = (self.ballView.rect.x + self.ballView.width/2, self.ballView.rect.y + self.ballView.height/2)
        elementcenter = (viewElement.rect.x + viewElement.width/2, viewElement.rect.y + viewElement.height/2)

        diffy = elementcenter[1] - ballcenter[1]
        diffx = elementcenter[0] - ballcenter[0]

        if viewElement.rect.x <= ballcenter[0] <= viewElement.rect.x + viewElement.width:
            if abs(diffy) <= viewElement.height / 2 + self.ballView.height / 2:
                if diffy > 0:
                    return True, True, self.ballView.rect.x, viewElement.rect.y - self.ballView.height
                else:
                    return True, True, self.ballView.rect.x, viewElement.rect.y + viewElement.height
        if viewElement.rect.y <= ballcenter[1] <= viewElement.rect.y + viewElement.height:
            if abs(diffx) <= viewElement.width / 2 + self.ballView.width / 2:
                if diffx > 0:
                    return True, False, viewElement.rect.x - self.ballView.width, self.ballView.rect.y
                else:
                    return True, False, viewElement.rect.x + viewElement.width, self.ballView.rect.y
        return False, None, None, None

    # make the ball move
    def move(self, bricks, walls, bat):
        if self.stickedTo is not None:
            self.ballView.rect.x = self.stickedTo.batView.rect.x + self.stickedTo.batView.width/2 - self.ballView.width / 2
            self.ballView.rect.y = self.stickedTo.batView.rect.y - self.ballView.height
        else:
            self.ballView.rect.x += self.x_change
            self.ballView.rect.y += self.y_change

            for brick in bricks:
                if self.setBallReflect(self.isOverlapped(brick)):
                    return

            for wall in walls.wallViews:
                if self.setBallReflect(self.isOverlapped(wall)):
                    return

            if self.setBallReflect(self.isOverlapped(bat)):
                return

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
            self.ballView.rect.x = newx
            self.ballView.rect.y = newy
            return True
        return False


# a controller between the model and the view
class BatController:
    def __init__(self):
        # TODO
        self.bat = Bat()
        self.batView = BatView(Constants.Border + Constants.Wall_width + Constants.Game_Screen_W/2-35,
                               Constants.Border + Constants.Wall_width + Constants.Game_Screen_H-50, 70, 20)

    def changespeed(self,x):
        self.batView.x_change+= x

    # make the bat move
    def move(self, event):
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.changespeed(-5)
            if event.key == pygame.K_RIGHT:
                self.changespeed(5)

        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.changespeed(5)
            if event.key == pygame.K_RIGHT:
                self.changespeed(-5)

    def setWalls(self, wallController):
        for wallView in wallController.wallViews:
            self.batView.addWall(wallView)

    def getView(self):
        return self.batView

# a controller between the model and the view
class BrickController:
    def __init__(self, x, y, maxX, maxY):
        # TODO
        self.brick = Brick()
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