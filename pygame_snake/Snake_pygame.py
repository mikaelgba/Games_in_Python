import pygame, random
from pygame.locals import *

def on_grid_random():
    
    x = random.randint(0,59)
    y = random.randint(0,59)
    return (x * 10, y * 10)

def colisao(colisao1, colisao2):
    
    return (colisao1[0] == colisao2[0]) and (colisao1[1] == colisao2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

#Iniciando e criando a janela
pygame.init()
janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255))

maca_cor = on_grid_random()
maca = pygame.Surface((10,10))
maca.fill((255,0,0))

direcao = LEFT
clock = pygame.time.Clock()
font = pygame.font.Font('freesansbold.ttf', 18)
score = 0

game_over = False
while(not game_over):
    
    clock.tick(10)
    for event in pygame.event.get():
        
        if(event.type == QUIT):
            pygame.quit()
            exit()

        #Verificando se houve auma tecla clicada
        if(event.type == KEYDOWN):
            
            if(event.key == K_UP and direcao != DOWN): direcao = UP
                
            if(event.key == K_DOWN and direcao != UP): direcao = DOWN
                
            if(event.key == K_LEFT and direcao != RIGHT): direcao = LEFT
                
            if(event.key == K_RIGHT and direcao != LEFT): direcao = RIGHT


    if(colisao(cobra[0], maca_cor)):
        
        maca_cor = on_grid_random()
        cobra.append((0,0))
        score = score + 1
        
    #Verificando se a cobra saiu da janela, caso sim, Game over
    if(cobra[0][0] == 600 or cobra[0][1] == 600 or cobra[0][0] < 0 or cobra[0][1] < 0):
        game_over = True
        break
    
    #Verificando se a cobra colidiu com ela mesma, caso sim, Game over
    for i in range(1, len(cobra) - 1):
        
        if(cobra[0][0] == cobra[i][0] and cobra[0][1] == cobra[i][1]):
            game_over = True
            break

    if(game_over): break

    
    for i in range(len(cobra) - 1, 0, -1): cobra[i] = (cobra[i-1][0], cobra[i-1][1])
    
    #controle de direcao
    if(direcao == UP): cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    
    if(direcao == DOWN): cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    
    if(direcao == RIGHT): cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    
    if(direcao == LEFT): cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    
    janela.fill((0,0,0))
    janela.blit(maca, maca_cor)
    
    for x in range(0, 600, 10): 
        pygame.draw.line(janela, (40, 40, 40), (x, 0), (x, 600))
        
    for y in range(0, 600, 10):
        pygame.draw.line(janela, (40, 40, 40), (0, y), (600, y))

    #Criando o Socre
    font_score = font.render('Score: %s' % (score),
                             True, (255, 255, 255))
    val = font_score.get_rect()
    val.topleft = (600 - 120, 10)
    janela.blit(font_score, val)
    
    for j in cobra: janela.blit(cobra_skin, j)

    pygame.display.update()

while(True):

    #mensagem de Game Over
    font_over = pygame.font.Font('freesansbold.ttf', 75)
    janela_over = font_over.render('Game Over',
                                   True, (255, 255, 255))
    val = janela_over.get_rect()
    val.midtop = (600 / 2, 10)
    
    janela.blit(janela_over, val)
    pygame.display.update()
    pygame.time.wait(500)
    
    while(True):
        
        for evento in pygame.event.get():
            
            if(evento.type == QUIT):
                pygame.quit()
                exit()
