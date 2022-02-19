import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint,choice

pygame.init()

# functions
def restart_game():
    global lastDmg, amount
    player.isDead = False
    lastDmg = 0
    amount = 0
    player.speed = 8.5
    player.rect.x = player.initialXpos
    player.rect.y = player.initialYpos
    player.timesCollided = 0
    player.isImune = False
    player.hasCollided = False
    normalLeftArrow.rect.x = SCREEN_WIDTH
    normalRightArrow.rect.x = -spriteSize
    poisonLeftArrow.rect.x = SCREEN_WIDTH
    poisonRightArrow.rect.x = -spriteSize
    flameLeftArrow.rect.x = SCREEN_WIDTH
    flameRightArrow.rect.x = -spriteSize

# dir
mainDir = os.path.dirname(__file__)
imageDir = os.path.join(mainDir,"images")

# spritesheets / sprites loadings
spriteSize = 96
hpSpritesheet = pygame.image.load(os.path.join(imageDir,"HPUI.png"))
arrowsSpritesheet = pygame.image.load(os.path.join(imageDir,"Arrows.png"))
playerSpritesheet = pygame.image.load(os.path.join(imageDir,"Pink Hair SS.png"))
objectsSpritesheet = pygame.image.load(os.path.join(imageDir,"Pink Hair Guy Objects.png"))
sceneSprite = pygame.image.load(os.path.join(imageDir,"Park Image.png"))


# colors
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (200,0,255)

# screen
SCREEN_WIDTH = 640
SCREEN_HEIGTH = 480
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
gameTitle = pygame.display.set_caption("Pink Haired Man")

# FPS
frameRate = pygame.time.Clock()
FPS = 30

# damage
normalDamageConstant = 1
poisonDamageConstant = 2
lastDmg = 0

# texts / messages / fonts
fpsFont = pygame.font.SysFont("arial",20,True,False)
fpsMessage = f"FPS : {FPS}"
fpsText = fpsFont.render(fpsMessage,True,BLACK)

stunnedFont = pygame.font.SysFont("arial",20,True,False)
stunnedMessage = "You've been damaged, you are imune for some time!"
stunnedText = stunnedFont.render(stunnedMessage,True,PURPLE)

gameOverFont1 = pygame.font.SysFont("comicsansms",50,True,True)
gameOverFont2 = pygame.font.SysFont("comicsansms",30,True,True)
gameOverMessage1 = "Game Over!"
gameOverMessage2 = "Press 'R' to restart the game!"
gameOverText1 = gameOverFont1.render(gameOverMessage1,True,RED)
gameOverText2 = gameOverFont2.render(gameOverMessage2,True,BLACK)

# classes
#---------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.isImune = False
        self.hasCollided = False
        self.timesCollided = 0
        self.isDead = False

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
        self.mask = pygame.mask.from_surface(self.image)
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
        self.mask = pygame.mask.from_surface(self.image)
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

class HPstatic(pygame.sprite.Sprite):
    def __init__(self,xPos:float,yPos:float):
        pygame.sprite.Sprite.__init__(self)
        self.image = hpSpritesheet.subsurface((0,0),(spriteSize,spriteSize))
        self.image = pygame.transform.scale(self.image,(spriteSize*1.5,spriteSize*1.5))
        self.rect = self.image.get_rect()
        self.rect.x = xPos
        self.rect.y = yPos

# arrows
#---------------------------------------------------------------------------------------------------------

minY = 30
probLeftList = [0,0,0,1,1,2,2]
probRightList = [0,0,0,1,1,2,2]
leftArrowChoice = choice(probLeftList)
rightArrowChoice = choice(probRightList)
amount = 0

print(leftArrowChoice)

class NormalLeftArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = arrowsSpritesheet.subsurface((0,0),(spriteSize,spriteSize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
    
    def update(self):
        global leftArrowChoice, amount
        if leftArrowChoice == 0:
            if self.rect.x + spriteSize < 0:
                amount += 1
                self.rect.x = SCREEN_WIDTH
                self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
                leftArrowChoice = choice(probLeftList)
            self.rect.x -= self.speed

class NormalRigthArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = arrowsSpritesheet.subsurface((spriteSize,0),(spriteSize,spriteSize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -spriteSize
        self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
    
    def update(self):
        global rightArrowChoice, amount
        if rightArrowChoice == 0:
            if self.rect.x > SCREEN_WIDTH:
                amount += 1
                self.rect.x = -spriteSize
                self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
                rightArrowChoice = choice(probRightList)
            self.rect.x += self.speed

class PoisonLeftArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 12
        self.image = arrowsSpritesheet.subsurface((0,spriteSize),(spriteSize,spriteSize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -spriteSize
        self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
    
    def update(self):
        global leftArrowChoice, amount
        if leftArrowChoice == 1:
            if self.rect.x + spriteSize < 0:
                amount += 1
                self.rect.x = SCREEN_WIDTH
                self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
                leftArrowChoice = choice(probLeftList)
            self.rect.x -= self.speed

class PoisonRightArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 12
        self.image = arrowsSpritesheet.subsurface((spriteSize,spriteSize),(spriteSize,spriteSize))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -spriteSize
        self.rect.y = randint(minY,SCREEN_HEIGTH - 100)

    def update(self):
        global rightArrowChoice, amount
        if rightArrowChoice == 1:
            if self.rect.x > SCREEN_WIDTH:
                amount += 1
                self.rect.x = -spriteSize
                self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
                rightArrowChoice = choice(probRightList)
            self.rect.x += self.speed

class FlameLeftArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        # animation
        self.flameArrowFrames = list()
        for i in range(2):
            self.img = arrowsSpritesheet.subsurface((i*spriteSize,spriteSize*2),(spriteSize,spriteSize))
            self.flameArrowFrames.append(self.img)
        self.currentIndex = 0
        self.image = self.flameArrowFrames[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -spriteSize
        self.rect.y = randint(minY,SCREEN_HEIGTH - 100)

    def update(self):
        global leftArrowChoice, amount
        if leftArrowChoice == 2:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.image = self.flameArrowFrames[int(self.currentIndex)]
            self.currentIndex += 0.5
            if self.rect.x + spriteSize < 0:
                amount += 1
                self.rect.x = SCREEN_WIDTH
                self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
                leftArrowChoice = choice(probLeftList)
            self.rect.x -= self.speed

class FlameRightArrow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        # animation
        self.flameArrowFrames = list()
        for i in range(2):
            self.img = arrowsSpritesheet.subsurface((i*spriteSize,spriteSize*3),(spriteSize,spriteSize))
            self.flameArrowFrames.append(self.img)
        self.currentIndex = 0
        self.image = self.flameArrowFrames[self.currentIndex]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = -spriteSize
        self.rect.y = randint(minY,SCREEN_HEIGTH - 100)

    def update(self):
        global rightArrowChoice, amount
        if rightArrowChoice == 2:
            if self.currentIndex > 1.4:
                self.currentIndex = 0
            self.image = self.flameArrowFrames[int(self.currentIndex)]
            self.currentIndex += 0.5
            if self.rect.x > SCREEN_WIDTH:
                amount += 1
                self.rect.x = -spriteSize
                self.rect.y = randint(minY,SCREEN_HEIGTH - 100)
                rightArrowChoice = choice(probRightList)
            self.rect.x += self.speed

#---------------------------------------------------------------------------------------------------------

spriteGroup = pygame.sprite.Group()
normalDamagingGroup = pygame.sprite.Group()
poisonDamagingGroup = pygame.sprite.Group()
flameDamagingGroup = pygame.sprite.Group()
player = Player()
healthPointsStatic = HPstatic(SCREEN_WIDTH - 160,3)
rock1 = Rock(400,250)
rock2 = Rock(10,120)
plant1 = Plant(400,110)
plant2 = Plant(450,190)
plant3 = Plant(100,3)
plant4 = Plant(100,300)
plant5 = Plant(40,360)
normalLeftArrow = NormalLeftArrow()
normalRightArrow = NormalRigthArrow()
poisonLeftArrow = PoisonLeftArrow()
poisonRightArrow = PoisonRightArrow()
flameLeftArrow = FlameLeftArrow()
flameRightArrow = FlameRightArrow()
spriteGroup.add(rock1)
spriteGroup.add(rock2)
spriteGroup.add(plant1)
spriteGroup.add(plant2)
spriteGroup.add(plant3)
spriteGroup.add(plant4)
spriteGroup.add(plant5)
spriteGroup.add(normalLeftArrow)
spriteGroup.add(normalRightArrow)
spriteGroup.add(poisonLeftArrow)
spriteGroup.add(poisonRightArrow)
spriteGroup.add(flameLeftArrow)
spriteGroup.add(flameRightArrow)
spriteGroup.add(player)
spriteGroup.add(healthPointsStatic)
normalDamagingGroup.add(normalLeftArrow)
normalDamagingGroup.add(normalRightArrow)
poisonDamagingGroup.add(poisonLeftArrow)
poisonDamagingGroup.add(poisonRightArrow)
flameDamagingGroup.add(flameLeftArrow)
flameDamagingGroup.add(flameRightArrow)

#---------------------------------------------------------------------------------------------------------

# main loop
while True:
    frameRate.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_r and player.isDead == True:
                restart_game()

    if player.rect.x + spriteSize < 0:
        player.rect.x = SCREEN_WIDTH
    elif player.rect.x > SCREEN_WIDTH:
        player.rect.x = -spriteSize
    elif player.rect.y + spriteSize < 0:
        player.rect.y = SCREEN_HEIGTH
    elif player.rect.y > SCREEN_HEIGTH:
        player.rect.y = -spriteSize

    if player.isDead == False:
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

    normalCollisionList = pygame.sprite.spritecollide(player,normalDamagingGroup,False,pygame.sprite.collide_mask)
    poisonCollisionList = pygame.sprite.spritecollide(player,poisonDamagingGroup,False,pygame.sprite.collide_mask)
    flameCollisionList = pygame.sprite.spritecollide(player,flameDamagingGroup,False,pygame.sprite.collide_mask)

    screen.blit(sceneSprite,(0,0))

    if amount > 4 and player.isImune == True:
        player.speed = 10
        player.isImune = False
        poisonDamageConstant = 2
        normalDamageConstant = 1

    if player.isImune == True and player.isDead == False:
        screen.blit(stunnedText,(5,5))

    spriteGroup.draw(screen)

    screen.blit(fpsText,(SCREEN_WIDTH - 80,SCREEN_HEIGTH - 23))

    print(player.timesCollided)
    
    if len(normalCollisionList) != lastDmg and player.isImune == False:
        amount = 0
        player.hasCollided = True
        player.isImune = True
        player.speed = 3
        player.timesCollided += normalDamageConstant
        damageConstant = 0

    if len(poisonCollisionList) != lastDmg and player.isImune == False:
        amount = 0
        player.hasCollided = True
        player.isImune = True
        player.speed = 3
        player.timesCollided += poisonDamageConstant
        damageConstant = 0

    if len(flameCollisionList) == 1 and player.isImune == False:
        player.isDead = True

    if player.timesCollided >= 3:
        player.isDead = True
        
    if player.isDead == True:
        gameOverBg1 = pygame.draw.rect(screen,BLACK,(40,40,SCREEN_WIDTH - 80,SCREEN_HEIGTH - 80))
        gameOverBg2 = pygame.draw.rect(screen,WHITE,(50,50,SCREEN_WIDTH - 100,SCREEN_HEIGTH - 100))
        screen.blit(gameOverText1,(175,150))
        screen.blit(gameOverText2,(100,240))
    else:
        spriteGroup.update()

    pygame.display.flip()
