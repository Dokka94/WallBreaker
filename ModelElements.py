

# model
class Ball:
    def __init__(self):
        # TODO
        self.textures = []
        self.velocity = 0.0
        self.angle = 0.0


# model
class Bat:
    def __init__(self):
        # TODO
        self.textures = []
        self.width = 0


# model
class Brick:
    def __init__(self):
        # TODO
        self.textures = ['simple_white.png']
        self.hitRate = 0
        self.hitCount = 0
        self.broken = False

    def getTexture(self):
        return self.textures[self.hitCount]

    def hit(self):
        self.hitCount+=1
        if self.hitCount == self.hitRate:
            self.broken = True
