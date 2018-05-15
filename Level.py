from Controllers import *


# the gamefield with bricks
class Level:
    def __init__(self, level):
        # TODO
        self.levelNumber = level
        self.bricks = []
        self.loadLevel(self.levelNumber)

    # check the given coords with the bricks, and return with that
    def hit(self, x, y):
        # TODO
        pass

    def loadLevel(self, level):
        levelFile = open(str(level) + "level.txt")
        rows = levelFile.readlines()
        for rowIndex in range(0, len(rows)):
            brickRow = []
            brickStrings = rows[rowIndex].split(',')
            for brickIndex in range(0, len(brickStrings)):
                brickRow.append(self.loadBrick(brickStrings[brickIndex].strip(),
                                               brickIndex, rowIndex,  len(brickStrings), len(rows)))
            self.bricks.append(brickRow)
        levelFile.close()

    def loadBrick(self, brickString, x, y, maxX, maxY):
        brickTypes = ["simple", "double"]
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
