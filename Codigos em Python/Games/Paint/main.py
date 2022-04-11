import pygame
from pygame.locals import *
from sys import exit

pygame.init()

def draw(xPos,yPos):
    global screen, BLACK, pixelList
    rect = pygame.Rect(xPos,yPos,10,10)
    pixel = pygame.draw.rect(screen,BLACK,rect)
    pixelList.append(pixel)

pixelList = list()

SCREEN_WIDTH = 850
SCREEN_HEIGTH = 650
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
screenTitle = pygame.display.set_caption("Paint")

clock = pygame.time.Clock()
FPS = 240

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
LIGHT_BLUE = (0,0,200)

isDrawing = False

screen.fill(WHITE)

toolBack = pygame.draw.rect(screen, LIGHT_BLUE,(0,0,SCREEN_WIDTH,70))
toolBackTape = pygame.draw.rect(screen, BLACK,(0,65,SCREEN_WIDTH,5))
eraseButtonColor = RED
eraseButtonBG = pygame.draw.rect(screen,BLACK,(18,18,104,44))

eraseFont = pygame.font.SysFont("arial",20,True,False)
eraseMessage = "Erase All"
eraseText = eraseFont.render(eraseMessage,True,BLACK)

while True:
    clock.tick(FPS)
    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 :
                isDrawing = True
            if eraseButton.collidepoint(mousePos):
                screen.fill(WHITE,(0,70,SCREEN_WIDTH,SCREEN_HEIGTH-70))
                eraseButtonColor = GREEN

        if event.type == MOUSEBUTTONUP:
            if event.button == 1:
                isDrawing = False
                eraseButtonColor = RED
        
    if isDrawing and not toolBack.collidepoint(mousePos):
        draw(mousePos[0],mousePos[1])

    eraseButton = pygame.draw.rect(screen,eraseButtonColor,(20,20,100,40))
    screen.blit(eraseText,(25,25))

    pygame.display.flip()