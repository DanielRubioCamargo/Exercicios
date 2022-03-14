import pygame
from pygame.locals import *
from sys import exit
import os
from random import choice

pygame.init()

mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images")

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Road Game")

SPRITE_SIZE = 96
spritesheet = pygame.image.load(os.path.join(imageDir,"spritesheet.png"))

backgroundImage = spritesheet.subsurface((SPRITE_SIZE*2,0),(SPRITE_SIZE,SPRITE_SIZE))
backgroundImage = pygame.transform.scale(backgroundImage,(SCREEN_WIDTH,SCREEN_HEIGTH))
bgCount1 = 0
backgroundImage2 = spritesheet.subsurface((SPRITE_SIZE*2,0),(SPRITE_SIZE,SPRITE_SIZE))
backgroundImage2 = pygame.transform.scale(backgroundImage,(SCREEN_WIDTH,SCREEN_HEIGTH))
bgCount2 = -600

clock = pygame.time.Clock()
FPS = 30

class Car(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.xSpeed = 0
        self.hasToMoveRight = False
        self.hasToMoveLeft = False
        self.moveConstant = 0
        self.initialXpos = (SCREEN_WIDTH/2) - 100
        self.initialYpos = (SCREEN_HEIGTH/2) + 100
        self.image = spritesheet.subsurface((0,0),(SPRITE_SIZE,SPRITE_SIZE))
        self.image = pygame.transform.scale(self.image,(SPRITE_SIZE*2,SPRITE_SIZE*2))
        self.rect = self.image.get_rect()
        self.rect.x = self.initialXpos
        self.rect.y = self.initialYpos

    def update(self):
        if self.hasToMoveRight:
            self.move_right()
        elif self.hasToMoveLeft:
            self.move_left()

    def move_right(self):
        self.xSpeed = 10
        self.moveConstant = 225
        if self.rect.x >= self.initialXpos + self.moveConstant:
            self.xSpeed = 0
            self.hasToMoveRight = False
            self.initialXpos = self.rect.x
        else:
            self.rect.x += self.xSpeed

    def move_left(self):
        self.xSpeed = -10
        self.moveConstant = -225
        if self.rect.x <= self.initialXpos + self.moveConstant:
            self.xSpeed = 0
            self.hasToMoveLeft = False
            self.initialXpos = self.rect.x
        else:
            self.rect.x += self.xSpeed

class GreenCar(pygame.sprite.Sprite):
    def __init__(self, yPos : float):
        pygame.sprite.Sprite.__init__(self)
        self.ySpeed = 10
        self.xList = [-10,220,450]
        self.image = spritesheet.subsurface((SPRITE_SIZE,0),(SPRITE_SIZE,SPRITE_SIZE))
        self.image = pygame.transform.scale(self.image,(SPRITE_SIZE*2,SPRITE_SIZE*2))
        self.rect = self.image.get_rect()
        self.rect.x = choice(self.xList)
        self.rect.y = yPos

    def update(self):
        if self.rect.y >= SCREEN_HEIGTH:
            self.rect.y = -SPRITE_SIZE*2
            self.rect.x = choice(self.xList)
        self.rect.y += self.ySpeed

spriteGroup = pygame.sprite.Group()
car = Car()
greenCar1 = GreenCar(-SPRITE_SIZE*2)
greenCar2 = GreenCar(-SPRITE_SIZE*5)
spriteGroup.add(car)
spriteGroup.add(greenCar1)
spriteGroup.add(greenCar2)

while True:
    screen.fill((0,0,0))
    print(car.rect.x)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and (car.rect.x != 450) and car.hasToMoveLeft == False:
                car.hasToMoveRight = True
            elif event.key == K_a and (car.rect.x != -10) and car.hasToMoveRight == False:
                car.hasToMoveLeft = True

    bgCount1 += 10
    bgCount2 += 10

    if bgCount1 == 600:
        bgCount1 = -600
    if bgCount2 == 600:
        bgCount2 = -600

    screen.blit(backgroundImage,(0,bgCount1))
    screen.blit(backgroundImage2,(0,bgCount2))
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()