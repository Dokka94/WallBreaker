# the main Model class
from Game import *
from Process import *
from ViewElements import *

class Wallbreaker:
    
    Game_Screen_W = 600
    Game_Screen_H = 600
    
    def __init__(self, Screen_Width, Screen_Height, Screen):
        ''' self.savedProcesses = self.loadProcesses()
        self.levels = self.loadLevels()'''
        self.Screen_Width = Screen_Width
        self.Screen_Height = Screen_Height
        self.Screen = Screen

        
    # make a new process
    def newProcess(self, numofBricks, rowNumOfBricks, brickDistance):
        # TODO        
        Process(self.Screen_Width, self.Screen_Height,
                self.Screen, self.Game_Screen_W, self.Game_Screen_H)\
                .startGame(numofBricks, rowNumOfBricks, brickDistance)

    # load a process, and start a game
    def loadProcess(self):
        # TODO
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

        walls = [[self.Screen_Width/2-self.Game_Screen_W/2, Border_H, self.Game_Screen_W + 2*Wall_width, Wall_width],
                 [self.Screen_Width/2-self.Game_Screen_W/2, Border_H, Wall_width, self.Game_Screen_H + 2*Wall_width],
                 [self.Screen_Width/2-self.Game_Screen_W/2, self.Game_Screen_H + Wall_width + Border_H, self.Game_Screen_W + 2*Wall_width, Wall_width],
                 [self.Screen_Width/2+Wall_width+self.Game_Screen_W/2, Border_H, Wall_width, self.Game_Screen_H + 2*Wall_width]]
 
        for item in walls:
            wall = WallView(item[0], item[1], item[2], item[3])
            all_sprite_list.add(wall)
        
    
        #---BUTTONS---
        i=0
        List = self.loadProcesses()
        for key, value in List.items():
            self.loadButton = ButtonView(self.Screen_Width/2-250, 100 + i*60 ,500, 50, str(key))
            i+=1
            all_sprite_list.add(self.loadButton)
            
        
        #----WINDOW----        
        gameExit=False
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                
            
            all_sprite_list.update()  
            self.Screen.fill((255,255,255))
            all_sprite_list.draw(self.Screen)
            
            #if self.loadButton.click() and ...
            
            
            self.Screen.blit(text_title, [self.Screen_Width/2-70,40])
            self.Screen.blit(text_click, [self.Screen_Width/2-60,70])
            
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
