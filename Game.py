from Controllers import *
from ViewElements import *

# the loadGame() calls it
class Game:
    
    Black = (0,0,0)
    White = (255,255,255)
    Yellow = (255,211,25)

    
    def __init__(self, Screen_Width,Screen_Height ,Screen, num_b,row_num_b, b_distance,Game_Screen_W, Game_Screen_H ):
        # TODO
        ''' self.level = self.loadLevel(level)
        self.balls = []
        self.balls.append(BallController())
        self.bat = BatController()'''
        self.Screen = Screen
        self.Screen_Width = Screen_Width
        self.Screen_height = Screen_Height
        self.num_of_bricks = num_b
        self.brick_distance = b_distance
        self.row_num_of_bricks = row_num_b
        self.Game_Screen_W = Game_Screen_W
        self.Game_Screen_H = Game_Screen_H
        
    # load level from file
    def loadLevel(self, level):
        # TODO
        pass

    # the actual game-mechanism
    def nextStep(self):
        # TODO
        
        pygame.display.set_caption('Wall-Breaker')
        clock=pygame.time.Clock()
        
        all_sprite_list = pygame.sprite.Group()
        
        #----TEXTS----
        font = pygame.font.Font(None, 25)
        #text_score = font.render("Score: ", True, self.Black)
        text_level = font.render("Level: ", True, self.Black)
        
        
        #----WALLS----       
        Wall_width = 10
        Border = 15
        wall_list = pygame.sprite.Group()
        
        walls = [[Border, Border, self.Game_Screen_W + 2*Wall_width, Wall_width],
                 [Border, Border, Wall_width, self.Game_Screen_H + 2*Wall_width],
                 [Border, self.Game_Screen_H + Wall_width + Border, self.Game_Screen_W + 2*Wall_width, Wall_width],
                 [self.Game_Screen_W + Wall_width + Border, Border, Wall_width, self.Game_Screen_H + 2*Wall_width]]
 
        for item in walls:
            wall = WallView(item[0], item[1], item[2], item[3])
            all_sprite_list.add(wall)
            wall_list.add(wall)

        
        #----BRICKS----
        row=0
        col=0
        i = 0
        while (i <= self.num_of_bricks \
               or brick.rect.x + brick.width <= (self.Game_Screen_W + Border + Wall_width) ):
                
            brick = BrickView(((self.Game_Screen_W)-(self.brick_distance*(self.row_num_of_bricks)+1))/self.row_num_of_bricks,20)
            
            brick.rect.x = self.brick_distance + col*(brick.width+self.brick_distance) + Border + Wall_width
            brick.rect.y = self.brick_distance + row*(brick.height+self.brick_distance) + Border + Wall_width
            
            col += 1
            
            if brick.rect.x + brick.width >= (self.Game_Screen_W + Border + Wall_width):
                row+=1
                col = 0
            else:
                all_sprite_list.add(brick)
            i+= 1
            
            
        #----BAT----
        bat = BatView(Border + Wall_width + self.Game_Screen_W/2-35,\
                      Border + Wall_width +self.Game_Screen_H-50,70,20)
        bat.walls = wall_list
        all_sprite_list.add(bat)
        
            
        #----BALL----
        ball = BallView(Border + Wall_width + self.Game_Screen_W/2-6,\
                        Border + Wall_width +self.Game_Screen_H-50-12,12,12)      
        all_sprite_list.add(ball)
        
        
        #----WINDOW----
        gameExit=False
        while not gameExit:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                
                
                #----BAT MOVEMENT----
                if event.type==pygame.KEYDOWN:  
                    if event.key == pygame.K_LEFT:
                        bat.changespeed(-5)
                    if event.key == pygame.K_RIGHT:
                        bat.changespeed(5)
                
                if event.type==pygame.KEYUP:  
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        bat.changespeed(0)
                
            all_sprite_list.update()  
            self.Screen.fill(self.White)
            all_sprite_list.draw(self.Screen)
            #self.Screen.blit(text_score, [700,150])
            self.Screen.blit(text_level, [700,150])
            
            pygame.display.update()
            clock.tick(15)
            
        pygame.quit()
        quit()

