# the main Model class
from Game import *
from Process import *
from ViewElements import *
from Constants import *

class Wallbreaker:

    def __init__(self, Screen):
        ''' self.savedProcesses = self.loadProcesses()
        self.levels = self.loadLevels()'''
        self.screen = Screen

        
    # make a new process
    def newProcess(self, name):
        Process(self.screen, name).startGame()

    # load a process, and start a game
    def loadProcess(self):
        pygame.display.set_caption('Wall-Breaker')
        clock=pygame.time.Clock()
        all_sprite_list = pygame.sprite.Group()
        
        #---TEXTS----
        font = pygame.font.Font(None, 35)
        text_title = font.render(" Load Game ", True, (0,0,0))
        font = pygame.font.Font(None, 20)
        text_click = font.render(" Click on your name ", True, (0,0,0))
        
        
        #----WALLS----
        Wall_width = 10
        Border_H = 15

        walls = [[Constants.Screen_Width/2-Constants.Game_Screen_W/2, Border_H, Constants.Game_Screen_W + 2*Wall_width, Wall_width],
                 [Constants.Screen_Width/2-Constants.Game_Screen_W/2, Border_H, Wall_width, Constants.Game_Screen_H + 2*Wall_width],
                 [Constants.Screen_Width/2-Constants.Game_Screen_W/2, Constants.Game_Screen_H + Wall_width + Border_H, Constants.Game_Screen_W + 2*Wall_width, Wall_width],
                 [Constants.Screen_Width/2+Wall_width+Constants.Game_Screen_W/2, Border_H, Wall_width, Constants.Game_Screen_H + 2*Wall_width]]
 
        for item in walls:
            wall = WallView(item[0], item[1], item[2], item[3])
            all_sprite_list.add(wall)
        
    
        #---BUTTONS---
        i = 0
        List = self.loadProcesses()
        buttonDict = {}
        for key, value in List.items():
            button = ButtonView(Constants.Screen_Width/2-250, 100 + i*60 ,500, 50, str(key))
            i+=1
            all_sprite_list.add(button)
            buttonDict[key] = button
        
        #----WINDOW----
        gameExit=False
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                
            
            all_sprite_list.update()  
            self.screen.fill((255,255,255))
            all_sprite_list.draw(self.screen)

            for key, value in List.items():
                if buttonDict[key].click():
                    Process(self.screen, key, value).startGame()

            self.screen.blit(text_title, [Constants.Screen_Width/2-70, 40])
            self.screen.blit(text_click, [Constants.Screen_Width/2-60, 70])
            
            pygame.display.update()
            clock.tick(15)
            
        pygame.quit()
        quit()

    # load all saved games from file
    def loadProcesses(self):
        #
        d = {}
        with open("savedgames.txt") as f:
            for line in f:
               (key, val) = line.split()
               d[str(key)] = val
        return d
        
        #a kulcs a nev az ertek a szint

    # load "all" levels from files
    def loadLevels(self):
        # TODO
        return []
