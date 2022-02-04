from numpy import disp
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange, choice

pygame.init()
pygame.mixer.init()

mainFile = os.path.dirname(__file__)
imageFile = os.path.join(mainFile,"imagens")
soundFile = os.path.join(mainFile,"sons")

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480

gameSpeed = 10

obsChoice = choice([0,0,0,1])

WHITE = (255,255,255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

points = 0
scoreSound = pygame.mixer.Sound(os.path.join(soundFile,"score_sound.wav"))

def display_message(msg, size, color):
    font = pygame.font.SysFont("comicsansms",size,True,False)
    message = f"{msg}"
    finalText = font.render(message,True,color)
    return finalText

gameOverMessage = display_message("GAME OVER",40,BLACK)
restartMessage = display_message("Press R to start a new game!",30,BLACK)

pygame.display.set_caption('Dino Game')

spriteSheet = pygame.image.load(os.path.join(imageFile,"dinoSpritesheet.png"))

def restart_game():
    global points, obsChoice, gameSpeed, collisionsList
    #collisionsList.clear()
    dino.hasPlayed = False
    points = 0
    obsChoice = choice([0,0,0,1])
    gameSpeed = 10
    dino.rect.y = 385-(32*3)/2
    dino.isJumping = False
    fDino.rect.x = SCREEN_WIDTH
    cactus.rect.x = SCREEN_WIDTH

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dinoList = list()
        self.hasPlayed = False
        self.deathSound = pygame.mixer.Sound(os.path.join(soundFile,"death_sound.wav"))
        self.jumpSound = pygame.mixer.Sound(os.path.join(soundFile,"jump_sound.wav"))
        self.jumpSound.set_volume(1)
        for i in range(3):
            self.img = spriteSheet.subsurface((i*32,0),(32,32))
            self.img = pygame.transform.scale(self.img,(32*3,32*3))
            self.dinoList.append(self.img)
        self.currentIndex = 0
        self.image = self.dinoList[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.initialYpos = 385
        self.rect.topleft = (100,self.initialYpos)
        self.isJumping = False

    def jump(self):
        self.jumpSound.play()
        self.isJumping = True

    def update(self):
        if self.isJumping == True:
            self.rect.y -= 20
            if self.rect.y <= 100:
                self.isJumping = False
        else:
            if self.rect.y < self.initialYpos-(32*3)/2:
                self.rect.y += 20
            else:
                self.rect.y = self.initialYpos-(32*3)/2
        self.currentIndex += 0.2
        if self.currentIndex > 2:
            self.currentIndex = 0
        self.image = self.dinoList[int(self.currentIndex)]

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.choice = obsChoice
        self.image = spriteSheet.subsurface((5*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*2,32*2))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = SCREEN_HEIGTH-128

    def update(self):
        if self.choice == 0:
            if self.rect.x + 32 <= 0:
                self.rect.x = SCREEN_WIDTH
            self.rect.x -= gameSpeed

class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((7*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*3,32*3))
        self.rect = self.image.get_rect()
        self.rect.x = (randrange(SCREEN_WIDTH,SCREEN_WIDTH + (96*3),32*3))

    def update(self):
        if self.rect.x < -40:
            self.rect.x = (randrange(SCREEN_WIDTH,SCREEN_WIDTH + (96*3),32*3))
        self.rect.x -= gameSpeed

class FlyingDino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.flyingDinoFrames = list()
        self.choice = obsChoice
        for i in range(2):
            self.img = spriteSheet.subsurface(((i+3)*32,0),(32,32))
            self.img = pygame.transform.scale(self.img,(32*3,32*3))
            self.flyingDinoFrames.append(self.img)
        self.currentPos = 0
        self.image = self.flyingDinoFrames[self.currentPos]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 200

    def update(self):
        if self.choice == 1:
            self.rect.x -= gameSpeed
            if self.rect.x + 96 < 0:
                self.rect.x = SCREEN_WIDTH
            self.currentPos += 0.25
            if self.currentPos > 1:
                self.currentPos = 0
            self.image = self.flyingDinoFrames[int(self.currentPos)]

class Ground(pygame.sprite.Sprite):
    def __init__(self,xPos):
        pygame.sprite.Sprite.__init__(self)
        self.image = spriteSheet.subsurface((32*6,0),(32,32))
        self.image = pygame.transform.scale(self.image,(32*2,32*2))
        self.rect = self.image.get_rect()
        self.rect.y = SCREEN_HEIGTH-96
        self.rect.x = xPos

    def update(self):
        self.rect.x -= 10
        if self.rect.x + 64 < 0:
            self.rect.x = SCREEN_WIDTH

allSprites = pygame.sprite.Group()
dino = Dino()
for i in range(3):
    cloud = Clouds()
    cloud.rect.y = i*60
    allSprites.add(cloud)
for i in range(20):
    ground = Ground(i*64)
    allSprites.add(ground)
allSprites.add(dino)
cactus = Cactus()
allSprites.add(cactus)
for i in range(2):
    fDino = FlyingDino()
    allSprites.add(fDino)

obstacleGroup = pygame.sprite.Group()
obstacleGroup.add(cactus)
obstacleGroup.add(fDino)

frameRate = pygame.time.Clock()

while True:
    frameRate.tick(30)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE and len(collisionsList) != 1:
                if dino.rect.y != dino.initialYpos-(32*3)/2:
                    pass
                else:
                   dino.jump()
            if event.key == K_r:
                restart_game()

    collisionsList = pygame.sprite.spritecollide(dino,obstacleGroup,False,pygame.sprite.collide_mask)

    allSprites.draw(screen)

    if cactus.rect.x <= 0 or fDino.rect.x <= 0:
        obsChoice = choice([0,0,0,1])
        fDino.choice = obsChoice
        cactus.choice = obsChoice
        cactus.rect.x = SCREEN_WIDTH
        fDino.rect.x = SCREEN_WIDTH

    if len(collisionsList) == 1:
        screen.blit(gameOverMessage,(200,100))
        screen.blit(restartMessage,(200,250))
        if dino.hasPlayed == False:
            dino.deathSound.play()
            dino.hasPlayed = True

    if dino.hasPlayed == True:
        pass
    else:
        points += 1
        updateMessage = display_message(points,40,BLACK)
        if points%100 == 0:
            scoreSound.play()
            if gameSpeed >= 25:
                gameSpeed += 0.1
            else:
                gameSpeed += 1
        allSprites.update()

    screen.blit(updateMessage,(530,30))
    pygame.display.flip()