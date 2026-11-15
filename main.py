import pygame
pygame.init()
screen=pygame.display.set_mode((400,300))
screen.fill((255,255,255))
lb=pygame.Color("lightblue")
pygame.draw.circle(screen,lb,(300,200),50)#solid circle
pygame.draw.circle(screen,lb,(100,100),50,5)#hollow circle
done=False
while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.display.flip()