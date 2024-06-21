#This file was mad for the SPJ-Game-Dev YouTube channel
#Simple 2D window with a movable rectangle along the x axis
#Published June 21, 2024
import pygame

pygame.init()

#Screen Variables
WIDTH = 800
HEIGHT = 600
caption = "Simple Example"
fps = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(caption)

#Player Variables
dx = 0
dy = 0
p_width = 20
p_height = 40
prect = pygame.Rect(50, 50, p_width, p_height)

#Game Loop Variables
run = True
timer = pygame.time.Clock()

#Main Game Loop
while run:
    timer.tick(fps)
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, 'Red', prect)
    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dx = -1
            if event.key == pygame.K_d:
                dx = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                dx = 0
            if event.key == pygame.K_d:
                dx = 0
    prect.x += dx
    prect.y += dy
    pygame.display.update()
pygame.quit()
