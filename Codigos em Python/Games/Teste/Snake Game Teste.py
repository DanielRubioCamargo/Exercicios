import pygame
from pygame.locals import *
from sys import exit
from random import randint

def set_snake_size(lst:list):
    for i in lst:
        pygame.draw.rect(screen,(snakeColor),(i[0],i[1],snakeWidth,snakeHeigth))

def reset_snake():
    global points,snakeSpeed,snakeLength,snakeList,appleX,appleY,isDead
    points = 0
    snakeSpeed = 5
    snakeLength = 5
    snakeList = []
    appleX = randint(appleWidth,screenWidth-appleWidth)
    appleY = randint(appleHeigth,screenHeigth-appleHeigth)
    isDead = False

pygame.init()

#Screen
screenWidth = 640
screenHeigth = 480
screen = pygame.display.set_mode((screenWidth,screenHeigth))
gameTitle = pygame.display.set_caption("Snake Game")

#FPS
frameRate = pygame.time.Clock()

#Player Atributes
snakeX = screenWidth/2
snakeY = screenHeigth/2
snakeWidth = 20
snakeHeigth = 20
snakeSpeed = 5
snakeColor = (0,255,0)
snakeControlX = 5
snakeControlY = 0
snakeLength = 5
isDead = False

#Apple Atributes
appleWidth = 20
appleHeigth = 20
appleX = randint(appleWidth,screenWidth-appleWidth)
appleY = randint(appleHeigth,screenHeigth-appleHeigth)
appleColor = (255,0,0)

#List
snakeList = list()

#Text
font = pygame.font.SysFont("Arial",20,True,False)
points = 0

#language
ptLang = "Points"
lang = str(input("Idiom : English/Ingles or/ou Portuguese/Portugues : ")).upper().strip()
if lang == "ENGLISH" or lang == "INGLES" or lang == "ENG" or lang == "ING":
    ptLang = "Points"
    print("You can open the game window now!")
elif lang == "PORTUGUESE" or lang == "PORTUGUES" or lang == "PT" or lang == "PT-BR" or lang == "BR":
    ptLang = "Pontos"
    print("Você pode abrir o jogo agora!")
else:
    print("You can open the game window now!")

#Main Loop
while True:
    screen.fill((0,0,0))
    frameRate.tick(30)
    pointsMessage = "{} : {}".format(ptLang,points)
    text = font.render(pointsMessage,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                if snakeControlX == 0:
                    snakeControlX = snakeSpeed
                    snakeControlY = 0
            if event.key == K_a:
                if snakeControlX == 0:
                    snakeControlX = -snakeSpeed
                    snakeControlY = 0
            if event.key == K_s:
                if snakeControlY == 0:
                    snakeControlX = 0
                    snakeControlY = snakeSpeed
            if event.key == K_w:
                if snakeControlY == 0:
                    snakeControlX = 0
                    snakeControlY = -snakeSpeed

    snakeX += snakeControlX
    snakeY += snakeControlY

    if snakeX > screenWidth:
        snakeX = 0
    if snakeX < 0:
        snakeX = screenWidth
    if snakeY > screenHeigth:
        snakeY = 0
    if snakeY < 0:
        snakeY = screenHeigth

    headList = list()
    headList.append(snakeX)
    headList.append(snakeY)
    snakeList.append(headList)
    
    if len(snakeList) > snakeLength:
        snakeList.pop(0)

    if snakeList.count(headList) > 1:
        isDead = True
        deathFont = pygame.font.SysFont("Arial",25,True,True)
        deathMessage = "Você morreu! Pressione R para jogar novamente!"
        deathText = deathFont.render(deathMessage,True,(255,0,0))
        while isDead:
            for deadEvent in pygame.event.get():
                if deadEvent.type == QUIT:
                    pygame.quit()
                    exit()
                if deadEvent.type == KEYDOWN:
                    if deadEvent.key == K_r:
                        reset_snake()
            screen.blit(deathText,((screenWidth/2)-285,screenHeigth/2))
            pygame.display.update()

    set_snake_size(snakeList)

    snake = pygame.draw.rect(screen,snakeColor,(snakeX,snakeY,snakeWidth,snakeHeigth))     
    apple = pygame.draw.rect(screen,appleColor,(appleX,appleY,appleWidth,appleHeigth))  
        
    if snake.colliderect(apple):
        points += 1
        snakeLength += 1
        appleX = randint(appleWidth,screenWidth-appleWidth)
        appleY = randint(appleHeigth,screenHeigth-appleHeigth)
        #snakeSpeed += 0.25

    screen.blit(text,(screenWidth-150,30))
    pygame.display.update()