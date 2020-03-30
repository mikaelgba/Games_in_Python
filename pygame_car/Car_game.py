import pygame
from random import randint
pygame.init()

x = 380     # max 530 min min 230 era 380
y = 100       #era 100
pos_x = 526
pos_y = 800
pos_y_a = 800
pos_y_c = 2500
time = 0
contador = 0
velo = 9

car = pygame.image.load("imagens/car.png")
fundo = pygame.image.load('imagens/fundo.PNG')

font = pygame.font.SysFont('arial black',30)
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

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

    #verifica a colisao
    if ((x + 80 > pos_x and y + 180 > pos_y) ): y = 1200

    if ((x - 80 < pos_x - 300 and y + 180 > pos_y_a)): y = 1200

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c))and((x - 80 < pos_x - 136 and y + 180 > pos_y_c)):
        y = 1200

    if (pos_y <= -80): pos_y = randint(800,1000)

    if (pos_y_a <= -80): pos_y_a = randint(1200, 2000)

    if (pos_y_c <= -80): pos_y_c = randint(2200, 3000)

    if (time <20): time +=1
    
    else:
        contador +=1
        texto = font.render("Tempo: " + str(contador),
                            True, (255, 255, 255), (0, 0, 0))
        time = 0

    pos_y  -= velo
    pos_y_a -= velo + 2 
    pos_y_c -= velo + 10
           
    #janela.fill((0,0,0))
    #janela.blit(car(x,y))
    janela.blit(fundo, (0,0))
    pygame.display.update()   
    #janela.fill((0,0,0)) 
    #pygame.display.update()

pygame.quit()
