from wallbreaker import Wallbreaker
from ViewElements import *


# the main Controller
class MenuController:
    def __init__(self):
        # TODO
        self.wallBreaker = Wallbreaker()
        self.newButton = ButtonView()
        self.loadButton = ButtonView()
