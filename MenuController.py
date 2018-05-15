import pygame
from wallbreaker import Wallbreaker
from ViewElements import *
from Constants import *


# the main Controller
class MenuController():
    
    def __init__(self):
        # TODO       
        self.newButton = ButtonView(Constants.Screen_Width/2-85, 250, 170, 70, "New Game")
        self.loadButton = ButtonView(Constants.Screen_Width/2-85, 350 ,170, 70, "Load Game")
        self.htpButton = ButtonView(Constants.Screen_Width/2-85, 450, 170, 70, "How to play")

        self.Screen = pygame.display.set_mode((Constants.Screen_Width, Constants.Screen_Height))
        self.wallBreaker = Wallbreaker(self.Screen)
        
           
    
    def gui(self):
        
        pygame.display.set_caption('Wall-Breaker')
        clock=pygame.time.Clock()
        intro_im=pygame.image.load('wall.png')
        
        all_sprite_list = pygame.sprite.Group()
        all_sprite_list.add(self.newButton)
        all_sprite_list.add(self.loadButton)
        all_sprite_list.add(self.htpButton)
        
        intro=True
        
        while intro:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                
            self.Screen.fill(Constants.White)
            self.Screen.blit(intro_im,(60,10))
            
            all_sprite_list.draw(self.Screen)
            
            all_sprite_list.update()         
            
            if self.newButton.click():
                self.wallBreaker.newProcess(50,11,3)
            if self.loadButton.click():
                self.wallBreaker.loadProcess()
                
            pygame.display.update()
            clock.tick(15)
            
        pygame.quit()
        quit()


pygame.init()
MenuController().gui()
