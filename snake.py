import random
import sys
import pygame
import numpy as np

pygame.init()
screen = pygame.display.set_mode([1000, 1000])
clock = pygame.time.Clock()
fruit=[random.randint(0,50),random.randint(0,50)]
snake = [
    [10, 15],
    [11, 15],
    [12, 15],]
direction=[-1,0]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                direction=[0,-1] 
            if event.key == pygame.K_DOWN:
                direction=[0,1]
            if event.key == pygame.K_RIGHT:
                direction=[1,0]
            if event.key == pygame.K_LEFT:
                direction=[-1,0]    
    color = [255, 255, 255]
    screen.fill(color)
    x = np.arange(0,1000,20)  
    width = 20
    height = 20
    red = 0
    green = 0
    blue = 0
    color = [red, green, blue]
    for n in range(len(x)):
        if n%2==1:
            y = np.arange(20,1000,40)
        else:
            y = np.arange(0,1000,40)
        for val in y: 
            pygame.draw.rect(screen, color, [x[n],val,width,height])
    f=random.randint(0,50)
    if f==0:
        fruit=[random.randint(0,50),random.randint(0,50)]
    pygame.draw.rect(screen, [255,0,0],[fruit[0]*20, fruit[1]*20,20,20])
    fin=snake[-1]
    snake[2]=snake[1]
    snake[1]=snake[0]
    snake[0]=[snake[0][0]+direction[0],snake[0][1]+direction[1]]
    for n in range(len(snake)):
        for m in range(n+1,len(snake)):
            if snake[n]==snake[m]:
                pygame.quit()
                sys.exit()
    if snake[0]==fruit:
        snake.append(fin)
    for pt in snake:
        pygame.draw.rect(screen, [0,255,0], [pt[0]*20,pt[1]*20,20,20])
    pygame.display.update()
    clock.tick(5)