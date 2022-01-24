
from pydoc import ispackage
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

class Frog(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = list()
        self.isPressed = False
        for i in range(1,11):
            self.sprites.append(pygame.image.load(f"Codigos em Python\\Games\\Teste\\animation-master\\attack_{str(i)}.png"))
        self.currentPos = 0
        self.image = self.sprites[self.currentPos]
        self.image = pygame.transform.scale(self.image,(128*3,64*3))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,255

    def animate(self):
        self.isPressed = True

    def update(self):
        if self.isPressed == True:
            self.currentPos += 0.3
            if self.currentPos >= len(self.sprites):
                self.currentPos = 0
                self.isPressed = False
            self.image = self.sprites[int(self.currentPos)]
            self.image = pygame.transform.scale(self.image,(128*3,64*3))

spritesGroup = pygame.sprite.Group()
frog = Frog()
spritesGroup.add(frog)

screenWidth = 640
screenHeigth = 480

screen = pygame.display.set_mode((screenWidth,screenHeigth))
gameTitle = pygame.display.set_caption("Sprites")

swampBG = pygame.image.load("Codigos em Python\\Games\\Teste\\bg-swamp\\swampPA.jfif").convert()
swampBG = pygame.transform.scale(swampBG,(screenWidth,screenHeigth))

frameRate = pygame.time.Clock()

while True:
    print(frog.currentPos)
    screen.fill((0,0,0))
    frameRate.tick(30)
    screen.blit(swampBG,(0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                frog.animate()
    spritesGroup.draw(screen)
    spritesGroup.update()
    pygame.display.flip()