import pygame
from pygame.locals import *
import sys
import os

pygame.init()

mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images")

spritesheet = pygame.image.load(os.path.join(imageDir,"spritesheet.png"))

SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))

clock = pygame.time.Clock()
FPS = 30

class Warrior(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.isAnimating = False
        self.combatList = list()
        self.currentIndex = 0
        for i in range(6):
            self.img = spritesheet.subsurface((i*96,0),(96,96)).convert_alpha()
            self.combatList.append(self.img)
        self.image = self.combatList[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 350
        self.rect.y = 250

    def animate(self):
        if self.currentIndex > 5:
            self.currentIndex = 0
            self.isAnimating = False
        self.image = self.combatList[int(self.currentIndex)]
        self.mask = pygame.mask.from_surface(self.image)
        self.currentIndex += 0.5

    def update(self):
        if self.isAnimating:
            self.animate()

class Wizard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.isAnimating = False
        self.canThrowPower = False
        self.combatList = list()
        self.currentIndex = 0
        for i in range(3):
            self.img = spritesheet.subsurface((i*96,96),(96,96)).convert_alpha()
            self.combatList.append(self.img)
        self.image = self.combatList[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 250

    def animate(self):
        if self.currentIndex > 2.4:
            self.canThrowPower = True
            self.currentIndex = 0
            self.isAnimating = False
        self.image = self.combatList[int(self.currentIndex)]
        self.currentIndex += 0.1

    def update(self):
        if self.isAnimating:
            self.animate()

class Spell(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.spellFrames = list()
        self.isAnimating = False
        self.currentIndex = 0
        for i in range(3,5):
            self.img = spritesheet.subsurface((i*96,96),(96,96)).convert_alpha()
            self.spellFrames.append(self.img)
        self.image = self.spellFrames[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = wizard.rect.x + 100
        self.rect.y = wizard.rect.y

    def animate(self):
        if self.currentIndex > 1.4:
            self.currentIndex = 0
            self.isAnimating = False
        self.image = self.spellFrames[int(self.currentIndex)]
        self.currentIndex += 0.1

    def update(self):
        if wizard.canThrowPower:
            self.animate()
            self.rect.x += 10

spriteGroup = pygame.sprite.Group()
warrior = Warrior()
wizard = Wizard()
spriteGroup.add(warrior)
spriteGroup.add(wizard)

spellGroup = pygame.sprite.Group()
spell = Spell()
spellGroup.add(spell)

while True:
    screen.fill((255,255,255))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                wizard.isAnimating = True
            if event.key == K_d:
                wizard.rect.x += 10

    if pygame.sprite.collide_mask(warrior,wizard) and warrior.isAnimating:
        spriteGroup.remove(wizard)
    
    if spell.rect.x > SCREEN_WIDTH or pygame.sprite.collide_mask(spell, warrior):
        spriteGroup.remove(warrior)
        wizard.canThrowPower = False
        spell.rect.x = wizard.rect.x + 100
        spell.rect.y = wizard.rect.y

    spriteGroup.draw(screen)
    spriteGroup.update()
    if wizard.canThrowPower:
        spellGroup.draw(screen)
        spellGroup.update()
    pygame.display.flip()