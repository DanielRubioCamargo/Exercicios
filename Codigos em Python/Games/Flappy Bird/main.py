from matplotlib import animation
import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint

pygame.init()

mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images") 

SCREEN_WIDTH = 540
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Flappy Bird")

clock = pygame.time.Clock()
FPS = 60

backgroundImage = pygame.image.load(os.path.join(imageDir,"Realflappybirdbg.jpg"))
backgroundImage = pygame.transform.scale(backgroundImage,(SCREEN_WIDTH,SCREEN_HEIGTH))

spriteDefaultSize = 96

spritesheet = pygame.image.load(os.path.join(imageDir,"SpritesheetFB.png"))

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.verticalSpeed = 25
        self.jumpSpeed = -10
        self.gravity = 0.5
        self.currentIndex = 0
        self.initialXpos = 200
        self.initialYpos = (SCREEN_HEIGTH/2) - (spriteDefaultSize/2)
        self.animationFrames = list()
        for i in range(3):
            self.img = spritesheet.subsurface((i*spriteDefaultSize,0),(spriteDefaultSize,spriteDefaultSize)).convert_alpha()
            self.img = pygame.transform.scale(self.img,(48,48))
            self.animationFrames.append(self.img)
        self.image = self.animationFrames[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = self.initialXpos
        self.rect.y = self.initialYpos

    def update(self):
        if self.currentIndex > 2.4:
            self.currentIndex = 0
        self.image = self.animationFrames[int(self.currentIndex)]
        self.currentIndex += 0.1

        self.verticalSpeed += self.gravity
        self.rect.y += self.verticalSpeed
        
    def jump(self):
        self.verticalSpeed = self.jumpSpeed
        
class SkyPipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = spriteDefaultSize * 1.5
        self.heigth = spriteDefaultSize*6
        self.image = spritesheet.subsurface((spriteDefaultSize*4,0),(spriteDefaultSize,spriteDefaultSize)).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width,self.heigth))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = -376

    def update(self):
        if self.rect.x + self.width < 0:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = randint(-400,-180)
        self.rect.x -= 5

class GroundPipe(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.width = spriteDefaultSize * 1.5
        self.heigth = spriteDefaultSize*6
        self.image = spritesheet.subsurface((spriteDefaultSize*3,0),(spriteDefaultSize,spriteDefaultSize)).convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.width,self.heigth))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = 270

    def update(self):
        if self.rect.x + self.width < 0:
            self.rect.x = SCREEN_WIDTH
            self.rect.y = skyPipe.rect.y + skyPipe.heigth + 80
        self.rect.x -= 5

spriteGroup = pygame.sprite.Group()
pipeGroup = pygame.sprite.Group()
bird = Bird()
skyPipe = SkyPipe()
groundPipe = GroundPipe()
spriteGroup.add(bird)
spriteGroup.add(skyPipe)
spriteGroup.add(groundPipe)
pipeGroup.add(skyPipe)
pipeGroup.add(groundPipe)

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                bird.jump()

    if pygame.sprite.spritecollide(bird,pipeGroup,False,pygame.sprite.collide_mask) or bird.rect.y > SCREEN_HEIGTH:
        input()
        break
    
    screen.blit(backgroundImage,(0,0))
    spriteGroup.draw(screen)
    spriteGroup.update()
    pygame.display.flip()
