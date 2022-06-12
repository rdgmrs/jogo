#jogo estudo de pygame
#bibliotecas 
import sys
import pygame
import random

#start

pygame.init()
velocidade = 1

#posição inicial do jogador1
x_player1 = 500
y_player1 = 300
x_fruta = random.randint(20,980)
y_fruta = random.randint(20,580)

#dimensoes da tela
largura = 1000
altura = 600
#tela 
while True:
    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption('primeiro code pygame')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            print(event)
        
#joystick controles do player1
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            y_player1-= velocidade
        if comandos[pygame.K_DOWN]:
                y_player1+= velocidade
        if comandos[pygame.K_RIGHT]:
                x_player1+= velocidade
        if comandos[pygame.K_LEFT]:
                x_player1-= velocidade            
        
        tela.fill((0,0,0))

#quadrado verde = jogador1 
        jogador1 = pygame.draw.rect(tela,(0,255,0),(x_player1,y_player1,10,10))
        fruta1 = pygame.draw.rect(tela,(255,0,0),(x_fruta,y_fruta,10,10))
        #colisao com a fruta
        if jogador1.colliderect(fruta1):
                x_fruta = random.randint(20,980)
                y_fruta = random.randint(20,580)    
        #bordas da tela     
        if x_player1 > 1000:
                x_player1 = 985
        if x_player1 < 0:
                x_player1 = 0
        if y_player1 > 600:
                y_player1 = 585
        if y_player1 <  0:
                y_player1 = 0

        pygame.display.update()


