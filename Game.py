from Controllers import *
from ViewElements import *
from Constants import *
from Level import *
# the loadGame() calls it
class Game:
    


    #def __init__(self, screen, num_b, row_num_b, b_distance):
        #         # TODO
    def __init__(self, level, screen):
        self.level = Level(level)
        self.walls = WallController()
        self.balls = []
        self.balls.append(BallController())
        self.bat = BatController()

        self.balls[0].stickTo(self.bat)

        self.screen = screen


        self.allSpriteList = None
        self.refreshAllSpriteList()
        self.initWalls()
        self.bat.setWalls(self.walls)
        self.lives = 3
        self.won = False

    # load level from file
    def loadLevel(self, level):
        # TODO
        pass

    def refreshAllSpriteList(self):
        self.allSpriteList = pygame.sprite.Group()
        for brickController in self.level.getBricks():
            if brickController is not None:
                self.allSpriteList.add(brickController.brickView)
        for ballController in self.balls:
            self.allSpriteList.add(ballController.ballView)
        for wallView in self.walls.wallViews:
            self.allSpriteList.add(wallView)
        self.allSpriteList.add(self.bat.batView)

    def looseLife(self):
        self.lives -= 1

    def initWalls(self):
        walls = [[Constants.Border, Constants.Border, Constants.Game_Screen_W + 2 * Constants.Wall_width,
                  Constants.Wall_width],
                 [Constants.Border, Constants.Border, Constants.Wall_width,
                  Constants.Game_Screen_H + 2 * Constants.Wall_width],
                 [Constants.Border, Constants.Game_Screen_H + Constants.Wall_width + Constants.Border,
                  Constants.Game_Screen_W + 2 * Constants.Wall_width,
                  Constants.Wall_width],
                 [Constants.Game_Screen_W + Constants.Wall_width + Constants.Border, Constants.Border,
                  Constants.Wall_width,
                  Constants.Game_Screen_H + 2 * Constants.Wall_width]]

        for item in walls:
            self.walls.addWall(item[0], item[1], item[2], item[3])

    # the actual game-mechanism
    def start(self):
        # TODO
        
        pygame.display.set_caption('Wall-Breaker')
        clock=pygame.time.Clock()
        
        #----TEXTS----
        font = pygame.font.Font(None, 25)
        #text_score = font.render("Score: ", True, self.Black)
        text_level = font.render("Level: " + str(self.level.levelNumber), True, Constants.Black)
        text_lives = font.render("Lives: ", True, Constants.Black)
        
        
        #----WINDOW----
        gameExit=False
        while not gameExit and self.lives > 0 and not self.won:
            start = time.time()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                
                self.bat.move(event)
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    for ball in self.balls:
                        ball.release()
            for ball in self.balls:
                ball.move(self.level, self.walls, self.bat)
                self.level.deleteBrokenBricks()
                self.won = self.level.isReady()
                if not ball.isOnPlayField():
                    ball.stickTo(self.bat)
                    self.looseLife()
            end = time.time()
            #print("Counting time: " + str(end - start))
            start = time.time()
            self.refreshAllSpriteList()
            end = time.time()
            #print("Refresh time: " + str(end - start))
            start = time.time()
            self.allSpriteList.update()
            end = time.time()
            #print("Update time: " + str(end - start))
            start = time.time()
            self.screen.fill(Constants.White)

            self.allSpriteList.draw(self.screen)

            #self.Screen.blit(text_score, [700,150])
            self.screen.blit(text_level, [700, 150])

            text_lives = font.render("Lives: " + str(self.lives), True, Constants.Black)
            self.screen.blit(text_lives, [700, 250])
            end = time.time()
            #print("Draw time: " + str(end - start))
            pygame.display.update()

            clock.tick(15)
        if gameExit:
            pygame.quit()
            quit()
        else:
            return self.won

