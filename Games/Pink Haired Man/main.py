import pygame
from pygame.locals import *
from sys import exit
import os
from functions import *
from random import randint,randrange,choice

pygame.init()

# dir
mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images")

# spritesheets / sprites
spriteSize = 96
playerSpritesheet = pygame.image.load(os.path.join(imageDir,"Pink Hair SS.png"))
objectsSpritesheet = pygame.image.load(os.path.join(imageDir,"Pink Hair Guy Objects.png"))
sceneSprite = pygame.image.load(os.path.join(imageDir,"Park Image.png"))

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

# screen
SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Pink Haired Man")

# FPS
frameRate = pygame.time.Clock()
FPS = 30

# classes
#---------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.speed = 8.5

        self.lastMove = ""

        self.isIdleDown = True
        self.isWalkingDown = False
        self.isWalkingUp = False
        self.isIdleUp = False
        self.isWalkingRight = False
        self.isIdleRight = False
        self.isWalkingLeft = False
        self.isIdleLeft = False

        # idle down animation
        self.idleDownFrames = list()
        for i in range(2):
            self.img = playerSpritesheet.subsurface((i*spriteSize,0),(spriteSize,spriteSize))
            self.idleDownFrames.append(self.img)
        # walking down animation
        self.wDownFrames = list()
        for i in range(2,4):
            self.img = playerSpritesheet.subsurface((i*spriteSize,0),(spriteSize,spriteSize))
            self.wDownFrames.append(self.img)
        # idle up animation
        self.idleUpFrames = list()
        for i in range(2):
            self.img = playerSpritesheet.subsurface((i*spriteSize,3*spriteSize),(spriteSize,spriteSize))
            self.idleUpFrames.append(self.img)
        # walking up animation
        self.wUpFrames = list()
        for i in range(2,4):
            self.img = playerSpritesheet.subsurface((i*spriteSize,3*spriteSize),(spriteSize,spriteSize))
            self.wUpFrames.append(self.img)
        # walking right animation
        self.wRigthFrames = list()
        for i in range(4):
            self.img = playerSpritesheet.subsurface((i*spriteSize,2*spriteSize),(spriteSize,spriteSize))
            self.wRigthFrames.append(self.img)
        # walking left animation
        self.wLeftFrames = list()
        for i in range(4):
            self.img = playerSpritesheet.subsurface((i*spriteSize,spriteSize),(spriteSize,spriteSize))
            self.wLeftFrames.append(self.img)
        # idle right and left animation
        self.idleRightFrame = playerSpritesheet.subsurface((0,2*spriteSize),(spriteSize,spriteSize))
        self.idleLeftFrame = playerSpritesheet.subsurface((0,spriteSize),(spriteSize,spriteSize))

        self.currentIndex = 0
        self.image = self.idleDownFrames[self.currentIndex]
        self.rect = self.image.get_rect()
        self.initialXpos = 300
        self.initialYpos = 200
        self.rect.x = self.initialXpos
        self.rect.y = self.initialYpos

    def update(self):
        if self.isIdleDown == True:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.currentIndex += 0.05
            self.image = self.idleDownFrames[int(self.currentIndex)]
        elif self.isWalkingDown == True:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.currentIndex += 0.05
            self.image = self.wDownFrames[int(self.currentIndex)]
        elif self.isIdleUp == True:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.currentIndex += 0.05
            self.image = self.idleUpFrames[int(self.currentIndex)]
        elif self.isWalkingUp == True:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.currentIndex += 0.05
            self.image = self.wUpFrames[int(self.currentIndex)]
        elif self.isWalkingRight == True:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.currentIndex += 0.05
            self.image = self.wRigthFrames[int(self.currentIndex)]
        elif self.isIdleRight == True:
            self.image = self.idleRightFrame
        elif self.isWalkingLeft == True:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.currentIndex += 0.05
            self.image = self.wLeftFrames[int(self.currentIndex)]
        elif self.isIdleLeft == True:
            self.image = self.idleLeftFrame

class Rock(pygame.sprite.Sprite):
    def __init__(self,xPos:float,yPos:float):
        pygame.sprite.Sprite.__init__(self)
        self.image = objectsSpritesheet.subsurface((3*spriteSize,0),(spriteSize,spriteSize))
        self.image = pygame.transform.scale(self.image,(spriteSize*2,spriteSize*2))
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos

class Plant(pygame.sprite.Sprite):
    def __init__(self,xPos:float,yPos:float):
        pygame.sprite.Sprite.__init__(self)
        # animation
        self.plantFrames = list()
        for i in range(3):
            self.img = objectsSpritesheet.subsurface((i*spriteSize,0),(spriteSize,spriteSize))
            self.plantFrames.append(self.img)
        self.currentIndex = 0
        self.image = self.plantFrames[self.currentIndex]
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos

    def update(self):
        if self.currentIndex > 2.4:
            self.currentIndex = 0
        self.currentIndex += 0.1
        self.image = self.plantFrames[int(self.currentIndex)]

spriteGroup = pygame.sprite.Group()
player = Player()
rock1 = Rock(400,250)
rock2 = Rock(10,120)
plant1 = Plant(400,110)
plant2 = Plant(450,190)
plant3 = Plant(100,3)
plant4 = Plant(100,300)
plant5 = Plant(40,360)
spriteGroup.add(rock1)
spriteGroup.add(rock2)
spriteGroup.add(plant1)
spriteGroup.add(plant2)
spriteGroup.add(plant3)
spriteGroup.add(plant4)
spriteGroup.add(plant5)
spriteGroup.add(player)


#---------------------------------------------------------------------------------------------------------

# main loop
while True:
    frameRate.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if player.rect.x + spriteSize < 0:
        player.rect.x = SCREEN_WIDTH
    elif player.rect.x > SCREEN_WIDTH:
        player.rect.x = -spriteSize
    elif player.rect.y + spriteSize < 0:
        player.rect.y = SCREEN_HEIGTH
    elif player.rect.y > SCREEN_HEIGTH:
        player.rect.y = -spriteSize

    if pygame.key.get_pressed()[K_d]:
        player.lastMove = "D"
        player.rect.x += player.speed
        player.isIdleDown = False
        player.isWalkingDown = False
        player.isWalkingUp = False
        player.isIdleUp = False
        player.isWalkingRight = True
        player.isIdleRight = False
        player.isWalkingLeft = False
        player.isIdleLeft = False
    elif pygame.key.get_pressed()[K_a]:
        player.lastMove = "A"
        player.rect.x -= player.speed
        player.isIdleDown = False
        player.isWalkingDown = False
        player.isWalkingUp = False
        player.isIdleUp = False
        player.isWalkingRight = False
        player.isIdleRight = False
        player.isWalkingLeft = True
        player.isIdleLeft = False
    elif pygame.key.get_pressed()[K_w]:
        player.lastMove = "W"
        player.rect.y -= player.speed
        player.isIdleDown = False
        player.isWalkingDown = False
        player.isWalkingUp = True
        player.isIdleUp = False
        player.isWalkingRight = False
        player.isIdleRight = False
        player.isWalkingLeft = False
        player.isIdleLeft = False
    elif pygame.key.get_pressed()[K_s]:
        player.lastMove = "S"
        player.rect.y += player.speed
        player.isIdleDown = False
        player.isWalkingDown = True
        player.isWalkingUp = False
        player.isIdleUp = False
        player.isWalkingRight = False
        player.isIdleRight = False
        player.isWalkingLeft = False
        player.isIdleLeft = False
    else:
        if player.lastMove == "S":
            player.isWalkingDown = False
            player.isIdleDown = True
        elif player.lastMove == "W":
            player.isWalkingUp = False
            player.isIdleUp = True
        elif player.lastMove == "D":
            player.isWalkingRight = False
            player.isIdleRight = True
        elif player.lastMove == "A":
            player.isWalkingLeft = False
            player.isIdleLeft = True

    screen.blit(sceneSprite,(0,0))
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()
