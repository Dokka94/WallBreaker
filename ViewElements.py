import pygame
import pygame.font
from pickle import FALSE
from Constants import *

# interface
class ViewElement(pygame.sprite.Sprite):

    White = (255,255,255)
    Black = (0,0,0)
    Green = (81,164,82)
    Bright_Green = (158,207,141)
    
    def __init__(self):
        super(ViewElement,self).__init__()
        self.xpos = 0
        self.ypos = 0
        self.width = 0
        self.height = 0
        self.text = ""
    
    
    def __iter__(self):
        # TODO
        pass
    
    def draw(self):
        # TODO
        pass

# view
class ButtonView(ViewElement):
    
    def __init__(self, x, y, width, height, text):
       
        super(ButtonView,self).__init__()
        
        self.xpos = x
        self.ypos = y
        self.width = width
        self.height = height
        self.text = text
        
        self.draw()
        
        
    
    def draw(self):
        font = pygame.font.SysFont('tahoma', 15)
        textSurf = font.render(self.text, 1, self.Black)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.White)
        self.image.set_colorkey(self.White)
        W = textSurf.get_width()
        H = textSurf.get_height()
        self.image.blit(textSurf, [self.width/2 - W/2, self.height/2 - H/2])
        pygame.draw.rect(self.image, self.Black, [0, 0, self.width, self.height],2)        
        self.rect = self.image.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

    
    
    def click(self):
        
        click=pygame.mouse.get_pressed()
        mouse=pygame.mouse.get_pos()
        clicked = False
        
        if click[0] \
        and self.xpos+self.width > mouse[0] >self.xpos \
        and self.ypos+self.height > mouse[1] >self.ypos:
        
            clicked = True
            
        return clicked
    

# view
class BallView(ViewElement):

    def __init__(self, x, y, width, height, ballController):
        super(BallView,self).__init__()
        self.xpos = x
        self.ypos = y
        self.width = width
        self.height = height
        self.x_change = 0
        self.y_change = 0
        self.walls = 0
        self.controller = ballController
        self.draw()


    def draw(self):
        self.surface=pygame.Surface([self.width, self.height])
        self.image =pygame.image.load(self.controller.ball.getTexture())

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.surface.blit(self.image,(0,0))

        self.rect = self.surface.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

    def getx(self):
        return self.rect.x

    def gety(self):
        return self.rect.y

    def setx(self,x):
        self.rect.x = x

    def sety(self,y):
        self.rect.y = y
# view
class BatView(ViewElement):

    def __init__(self, x, y, width, height, batController):
        super(BatView,self).__init__()
        self.xpos = x
        self.ypos = y
        self.width = width
        self.height = height
        self.rect = 0
        self.x_change = 0
        self.controller = batController
        self.walls = pygame.sprite.Group()
        self.draw()

    def draw(self):
        self.surface = pygame.Surface([self.width, self.height])
        self.image = pygame.image.load(self.controller.bat.getTexture())

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.surface.blit(self.image, (0, 0))

        self.rect = self.surface.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

    def addWall(self, wallView):
        self.walls.add(wallView)

    def update(self):
        self.rect.x += self.x_change

        block_hit_list = pygame.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            if self.x_change > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
    def getx(self):
        return self.rect.x

    def gety(self):
        return self.rect.y

    def setx(self,x):
        self.rect.x = x

    def sety(self,y):
        self.rect.y = y


# view
class BrickView(ViewElement):

    def __init__(self, x, y, maxX, maxY, brickController):
        super(BrickView,self).__init__()
        self.height = int(Constants.Game_Screen_H / 3 * 2 / maxY)
        self.width = int(Constants.Game_Screen_W / maxX)

        self.xpos = self.width * x + Constants.Wall_width + Constants.Border
        self.ypos = self.height * y + Constants.Wall_width + Constants.Border

        self.controller = brickController

        self.draw()

    def draw(self):

        self.surface = pygame.Surface([self.width, self.height])
        self.image = pygame.image.load(self.controller.brick.getTexture())

        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.surface.blit(self.image,(0,0))

        self.rect = self.surface.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos


    def update(self):
        self.draw()

    def getx(self):
        return self.rect.x

    def gety(self):
        return self.rect.y

    def setx(self,x):
        self.rect.x = x

    def sety(self,y):
        self.rect.y = y

class WallView(ViewElement):

    def __init__(self, x, y, width, height):
        # TODO
        super(WallView, self).__init__()
        self.xpos = x
        self.ypos = y
        self.width = width
        self.height = height
        self.draw()

    def draw(self):
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(self.Black)
        self.rect = self.image.get_rect()
        self.rect.x = self.xpos
        self.rect.y = self.ypos

    def getView(self):
        return self

    def getx(self):
        return self.rect.x

    def gety(self):
        return self.rect.y

    def setx(self,x):
        self.rect.x = x

    def sety(self,y):
        self.rect.y = y
