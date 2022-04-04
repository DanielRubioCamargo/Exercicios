import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((640,480))

FPS = 30
clock = pygame.time.Clock()

inputFont = pygame.font.Font(None,30)
inputMessage = ""

activeColor = (50,50,50)
passiveColor = (10,10,10)
color = passiveColor
active = False

inputRect = pygame.Rect(100,100,100,30)

while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if inputRect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if event.type == KEYDOWN:
            if active:
                if event.key == K_BACKSPACE:
                    inputMessage = inputMessage[:-1]
                elif(len(inputMessage) < 10):
                    inputMessage += event.unicode

    if active:
        color = activeColor
    else:
        color = passiveColor

    pygame.draw.rect(screen,color,inputRect,2)

    inputText = inputFont.render(inputMessage,True,(255,255,255))

    inputRect.w = inputText.get_width() + 10

    screen.blit(inputText,((inputRect.x + 5),(inputRect.y + 5)))

    print(inputMessage)

    pygame.display.flip()