import pygame
from pygame.locals import *
from sys import exit
import os

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
        self.rect.x += self.xSpeed

spriteGroup = pygame.sprite.Group()
car = Car()
spriteGroup.add(car)

while True:
    print(car.rect.x)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d and (car.rect.x != 450):
                car.hasToMoveRight = True
            elif event.key == K_a and (car.rect.x != -10):
                car.hasToMoveLeft = True

    screen.blit(backgroundImage,(0,0))
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()