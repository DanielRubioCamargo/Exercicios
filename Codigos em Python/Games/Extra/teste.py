import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()
 
largura = 640
altura = 480
y = altura/2
x = largura/2
 
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('PYGAME')
frame = pygame.time.Clock()
 
while True:
    frame.tick(30) 
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 20
            if event.key == K_d:
                x = x + 20
            if event.key == K_w:
                y = y - 20
            if event.key == K_s:
                y = y + 20
        
    pygame.draw.rect(tela, (255,0,0), (x,y, 40,50))
    pygame.display.update()
