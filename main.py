import pygame
import random

pygame.init()
screenSize= (500,540)
win = pygame.display.set_mode((screenSize))
pygame.display.set_caption("GAME")
playerPos = [250,250]
playerSize= [20,20]
krok = 10
GREEN = (0, 255, 0)
BLUE = (255,0,0)
run = True
# definiuję itemsy
itemSize = 10

edible =[]

def makeItem():
    itemPosX = random.randint(0,screenSize[0])
    itemPosY = random.randint(0,screenSize[1])
    print (itemPosY, itemPosX)
    edible[0]=[BLUE, itemPosX,itemPosY, itemSize,itemSize]
    print(edible[0])

def drawItem(x):
    print('X', x)
    pygame.draw.rect(win, x)

while run:
    # opóźnienie w grze
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # obsługa zdarzeń
    keys = pygame.key.get_pressed()
    # warunki do zmiany pozycji obiektu
    if keys[pygame.K_LEFT]:
        playerPos[0] -= krok
    if keys[pygame.K_RIGHT]:
        playerPos[0]+= krok
    if keys[pygame.K_UP]:
        playerPos[1]-= krok
    if keys[pygame.K_DOWN] :
        playerPos[1]+= krok
     #"czyszczenie" ekranu
    win.fill((0, 0, 0))
    # rysowanie prostokąta
    pygame.draw.rect(win, GREEN, (playerPos, playerSize))
    makeItem()
    for a in edible:
        drawItem(a)
    # odświeżenie ekranu
    pygame.display.update()
