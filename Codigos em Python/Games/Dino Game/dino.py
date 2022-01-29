from locale import currency
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

pygame.init()
pygame.mixer.init()

mainFile = os.path.dirname(__file__)
imageFile = os.path.join(mainFile,"imagens")
soundFile = os.path.join(mainFile,"sons")

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480

WHITE = (255,255,255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

pygame.display.set_caption('Dino Game')

spriteSheet = pygame.image.load(os.path.join(imageFile,"dinoSpritesheet.png"))

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.dinoList = list()
        self.jumpSound = pygame.mixer.Sound(os.path.join(soundFile,"jump_sound.wav"))
        self.jumpSound.set_volume(1)
        for i in range(3):
            self.img = spriteSheet.subsurface((i*32,0),(32,32))
            self.img = pygame.transform.scale(self.img,(32*3,32*3))
            self.dinoList.append(self.img)
        self.currentIndex = 0
        self.image = self.dinoList[self.currentIndex]
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
        self.rect.x -= 10

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

frameRate = pygame.time.Clock()

while True:
    frameRate.tick(30)
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if dino.rect.y != dino.initialYpos-(32*3)/2:
                    pass
                else:
                    dino.jump()

    allSprites.draw(screen)
    allSprites.update()

    pygame.display.flip()