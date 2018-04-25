from ModelElements import *
from ViewElements import *

# a controller between the model and the view
class BallController:
    def __init__(self):
        # TODO
        self.ball = Ball()
        self.ballView = BallView()

    # make the ball move
    def move(self):
        # TODO
        pass


# a controller between the model and the view
class BatController:
    def __init__(self):
        # TODO
        self.bat = Bat()
        self.batView = BatView()

    # make the bat move
    def move(self):
        # TODO
        pass


# a controller between the model and the view
class BrickController:
    def __init__(self):
        # TODO
        self.brick = Brick()
        self.brickView = BrickView()