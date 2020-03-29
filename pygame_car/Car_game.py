import pygame
pygame.init()
x = 400
y = 300
velo = 9

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Car Game Test")

aberta = True
while(aberta):

    pygame.time.delay(50)

    for abert in pygame.event.get():
        if(abert.type == pygame.QUIT): aberta = False

    acao = pygame.key.get_pressed()
    if(acao[pygame.K_UP]): y-= velo
        
    if(acao[pygame.K_DOWN]): y+= velo
        
    if(acao[pygame.K_RIGHT]): x+= velo
        
    if(acao[pygame.K_LEFT]): x-= velo
           
    janela.fill((0,0,0))     
    pygame.draw.circle(janela,(255,255,0),(x,y),50)
    pygame.display.update()

pygame.quit()
