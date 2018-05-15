import pygame
from wallbreaker import Wallbreaker
from ViewElements import *
from Constants import *


# the main Controller
class MenuController:
    
    def __init__(self):
        self.newButton = ButtonView(Constants.Screen_Width/2-85, 250, 170, 70, "New Game")
        self.loadButton = ButtonView(Constants.Screen_Width/2-85, 350, 170, 70, "Load Game")
        self.htpButton = ButtonView(Constants.Screen_Width/2-85, 450, 170, 70, "How to play")

        self.Screen = pygame.display.set_mode((Constants.Screen_Width, Constants.Screen_Height))
        self.wallBreaker = Wallbreaker(self.Screen)
        self.givenName = ""

           
    
    def gui(self):
        
        pygame.display.set_caption('Wall-Breaker')
        clock = pygame.time.Clock()
        intro_im = pygame.image.load('wall.png')
        
        all_sprite_list = pygame.sprite.Group()
        all_sprite_list.add(self.newButton)
        all_sprite_list.add(self.loadButton)
        all_sprite_list.add(self.htpButton)

        font = pygame.font.Font(None, 25)
        # text_score = font.render("Score: ", True, self.Black)
        text = font.render("Your name: ", True, Constants.Black)
        text_name = font.render(self.givenName, True, Constants.Black)

        intro = True

        while intro:

            text_name = font.render(self.givenName, True, Constants.Black)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.givenName = self.givenName[0:len(self.givenName)-1]
                    elif len(self.givenName) < 4:
                        self.givenName += pygame.key.name(event.key).upper()

            self.Screen.fill(Constants.White)
            self.Screen.blit(intro_im,(60,10))

            self.Screen.blit(text, [Constants.Screen_Width/2-85, 550])
            displayname = self.givenName
            morecharcount = 4 - len(self.givenName)
            for c in range(0, morecharcount):
                displayname += '_'
            text_name = font.render(displayname, True, Constants.Black)
            self.Screen.blit(text_name, [Constants.Screen_Width/2 + 25, 550])

            all_sprite_list.draw(self.Screen)
            
            all_sprite_list.update()         
            
            if self.newButton.click():
                self.wallBreaker.newProcess(self.givenName)
            if self.loadButton.click():
                self.wallBreaker.loadProcess()
                
            pygame.display.update()
            clock.tick(15)
            
        pygame.quit()
        quit()


pygame.init()
MenuController().gui()
