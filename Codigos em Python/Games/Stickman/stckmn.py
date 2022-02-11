import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint,choice

pygame.init()

def restart_game():
    global points, collisionList
    points = 0
    collisionList = list()
    player.rect.x = player.initialXpos
    player.rect.y = player.initialYpos
    player.isJumping = False
    player.isRunning = False
    player.isIdle = True
    rock.rect.y = randint(150,250)
    rock.rect.x = SCREEN_WIDTH

# files system
mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images")

# colors
BLACK = (0,0,0)
WHITE = (255,255,255)

# screen atributes
SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Stickman Game")

# background image
bgChoiceList = [0,0,0,0,0,0,0,0,0,1]
if choice(bgChoiceList) == 0:
    bgImage = pygame.image.load(os.path.join(imageDir,"background.gif"))
elif choice(bgChoiceList) == 1:
    bgImage = pygame.image.load(os.path.join(imageDir,"riodejaneiro.jfif"))
bgImage = pygame.transform.scale(bgImage,(SCREEN_WIDTH,SCREEN_HEIGTH))

# frames per second
frameRate = pygame.time.Clock()
FPS = 30

# spritesheet
spritesheet = pygame.image.load(os.path.join(imageDir,"Test Pixel Arts.png"))
spriteSize = 32

# points
points = 0

# fonts
pointsFont = pygame.font.SysFont("arial",25,True,False)

# classes
# --------------------------------------------------------------------------------------------------------

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.isIdle = True
        self.isRunning = False
        self.isJumping = False
        self.constant = -10
        self.speed = 10
        self.idleFrames = list()
        self.runFrames = list()
        # jump animation
        self.jumpFrame = spritesheet.subsurface((spriteSize*4,0),(spriteSize,spriteSize))
        self.jumpFrame = pygame.transform.scale(self.jumpFrame,(spriteSize*4,spriteSize*4))
        # idle animation
        for i in range(2):
            self.img = spritesheet.subsurface((i*spriteSize,0),(spriteSize,spriteSize))
            self.img = pygame.transform.scale(self.img,(spriteSize*4,spriteSize*4))
            self.idleFrames.append(self.img)
        # run animation
        for i in range(2,4):
            self.img = spritesheet.subsurface((i*spriteSize,0),(spriteSize,spriteSize))
            self.img = pygame.transform.scale(self.img,(spriteSize*4,spriteSize*4))
            self.runFrames.append(self.img)
        self.currentIndex = 0
        self.image = self.idleFrames[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.initialXpos = 300
        self.initialYpos = 280
        self.rect.x = self.initialXpos
        self.rect.y = self.initialYpos

    def jump(self):
        if self.isJumping == True:
            self.rect.y += self.constant
            if self.rect.y < 50:
                self.constant = 10
            if self.rect.y == self.initialYpos:
                self.constant = -10
                self.isJumping = False
    
    def update(self):
        if self.isJumping == False:
            self.rect.y = self.initialYpos
            if self.isIdle:
                if self.currentIndex > 1.5:
                    self.currentIndex = 0
                self.currentIndex += 0.1
                self.image = self.idleFrames[int(self.currentIndex)]
            elif self.isRunning:
                if self.currentIndex > 1.5:
                    self.currentIndex = 0
                self.currentIndex += 0.1
                self.image = self.runFrames[int(self.currentIndex)]
        else:
            self.image = self.jumpFrame
            self.jump()

class Rock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image = spritesheet.subsurface((5*spriteSize,0),(spriteSize,spriteSize))
        self.image = pygame.transform.scale(self.image,(spriteSize*3,spriteSize*3))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = randint(150,250)

    def update(self):
        global points
        if self.rect.x < 0:
            points += 1
            self.rect.x = SCREEN_WIDTH
            self.rect.y = randint(150,250)  
        self.rect.x -= self.speed

spritesGroup = pygame.sprite.Group()
obstaclesGroup = pygame.sprite.Group()
player = Player()
rock = Rock()
spritesGroup.add(rock)
obstaclesGroup.add(rock)
spritesGroup.add(player)

# --------------------------------------------------------------------------------------------------------

# main loop
while True:
    pointsMessage = f"Points : {points}"
    pointsText = pointsFont.render(pointsMessage,True,BLACK)
    screen.fill(BLACK)
    frameRate.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.isJumping = True

    collisionList = pygame.sprite.spritecollide(player,obstaclesGroup,False,pygame.sprite.collide_mask)

    if len(collisionList) == 1:
        restart_game()

    if player.rect.x + spriteSize < 0:
        player.rect.x = SCREEN_WIDTH
    elif player.rect.x > SCREEN_WIDTH:
        player.rect.x = -spriteSize
    if pygame.key.get_pressed()[K_d]:
        player.isIdle = False
        player.isRunning = True
        player.rect.x += player.speed
    elif pygame.key.get_pressed()[K_a]:
        player.isIdle = False
        player.isRunning = True
        player.rect.x -= player.speed
    else:
        player.isIdle = True
        player.isRunning = False

    screen.blit(bgImage,(0,0))
    screen.blit(pointsText,(490,30))
    spritesGroup.draw(screen)
    spritesGroup.update()
    pygame.display.flip()