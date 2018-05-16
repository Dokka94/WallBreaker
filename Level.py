from Controllers import *


# the gamefield with bricks
class Level:
    def __init__(self, level):
        self.levelNumber = level
        self.bricks = []
        self.loadLevel(self.levelNumber)

    # check the given coords with the bricks, and return with that
    def hit(self, x, y):
        # TODO
        pass

    def loadLevel(self, level):
        levelFile = open(str(level) + "level.csv")
        rows = levelFile.readlines()
        for rowIndex in range(0, len(rows)):
            brickRow = []
            brickStrings = rows[rowIndex].split(';')
            for brickIndex in range(0, len(brickStrings)):
                brickRow.append(self.loadBrick(brickStrings[brickIndex].strip(),
                                               brickIndex, rowIndex,  len(brickStrings), len(rows)))
            self.bricks.append(brickRow)
        levelFile.close()

    def loadBrick(self, brickString, x, y, maxX, maxY):
        brickTypes = ["simple", "double", "triple"]
        if brickString in brickTypes:
            return BrickController(x, y, maxX, maxY,brickString)
        else:
            return None

    def getBricks(self):
        result = []
        for brickList in self.bricks:
            for brick in brickList:
                if brick is not None:
                    result.append(brick)
        return result

    def deleteBrokenBricks(self):
        for brickListIndex in range(0,len(self.bricks)):
            for brickIndex in range(0,len(self.bricks[brickListIndex])):
                brickController = self.bricks[brickListIndex][brickIndex]
                if brickController is not None and brickController.brick.broken:
                    self.bricks[brickListIndex][brickIndex] = None

    def isReady(self):
        return len(self.getBricks()) == 0

    def getRange(self, xpos, ypos):
        resultrange = []
        margin = Constants.Border + Constants.Wall_width
        bricksizex = Constants.Game_Screen_W / len(self.bricks[0])
        bricksizey = Constants.Game_Screen_H / 3 * 2 / len(self.bricks)
        xcoord = round((xpos - margin) / bricksizex)
        if xcoord == len(self.bricks[0]):
            xcoord -= 1
        ycoord = round((ypos - margin) / bricksizey)
        if ycoord >= len(self.bricks):
            ycoord = len(self.bricks) - 1
        if xcoord > 0:
            minxcoord = xcoord-1
        else:
            minxcoord = xcoord
        if ycoord > 0:
            minycoord = ycoord-1
        else:
            minycoord = ycoord
        if xcoord < len(self.bricks[0])-1:
            maxxcoord = xcoord + 1
        else:
            maxxcoord = xcoord
        if ycoord < len(self.bricks)-1:
            maxycoord = ycoord + 1
        else:
            maxycoord = ycoord
        for x in range(minxcoord, maxxcoord+1):
            for y in range(minycoord, maxycoord+1):
                brick = self.bricks[y][x]
                if brick is not None:
                    resultrange.append(brick)
        return resultrange
