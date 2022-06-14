#jogo estudo de pygame
#bibliotecas 
import sys
import pygame
import random

#start

pygame.init()
velocidade = 1
pontos_jogador1 = 0
pontos_jogador2 = 0
#posição inicial dos objetos na tela
x_player1 = 250
y_player1 = 150
x_player2 = 750
y_player2 = 150
x_fruta = random.randint(20,980)
y_fruta = random.randint(20,580)

#dimensoes da tela
largura = 1000
altura = 600

#função para mesnsagens
def exibir_mensagem(msg, tamanho, cor):
        fonte = pygame.font.SysFont('comicsansms', tamanho, True, False)
        mensagem = f'{msg}'
        texto_formatado = fonte.render(mensagem, True, cor)
        return texto_formatado

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
        
#joystick controles do player1 ##
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            y_player1-= velocidade
        if comandos[pygame.K_DOWN]:
                y_player1+= velocidade
        if comandos[pygame.K_RIGHT]:
                x_player1+= velocidade
        if comandos[pygame.K_LEFT]:
                x_player1-= velocidade            


        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_w]:
            y_player2-= velocidade
        if comandos[pygame.K_s]:
                y_player2+= velocidade
        if comandos[pygame.K_d]:
                x_player2+= velocidade
        if comandos[pygame.K_a]:
                x_player2-= velocidade            


        tela.fill((0,0,0))

#desenhar na tela (jogadores, frutas, etc) 
        jogador1 = pygame.draw.rect(tela,(0,255,0),(x_player1,y_player1,10,10))
        fruta1 = pygame.draw.rect(tela,(255,0,0),(x_fruta,y_fruta,10,10))
        jogador2 = pygame.draw.rect(tela,(0,0,255),(x_player2,y_player2,10,10))


        #colisao com a fruta
        if jogador1.colliderect(fruta1):
                x_fruta = random.randint(20,980)
                y_fruta = random.randint(20,580)
        if jogador2.colliderect(fruta1):
                x_fruta = random.randint(20,980)
                y_fruta = random.randint(20,580)
                
        #pontuacao                    
        if jogador1.colliderect(fruta1):
                pontos_jogador1 += 1
        if jogador2.colliderect(fruta1):
                pontos_jogador2 += 1

        #pontuação na tela
        texto_pontos_jogador1 = exibir_mensagem(pontos_jogador1, 50, (00,255,0))
        tela.blit(texto_pontos_jogador1, (50,20))
        texto_pontos_jogador2 = exibir_mensagem(pontos_jogador2, 50, (0,0,255))
        tela.blit(texto_pontos_jogador2, (950,20))



        #bordas da tela  
        if x_player1 > 990:
                x_player1 = 990
        if x_player1  < 0:
                x_player1 = 0
        if y_player1  > 590:
                y_player1 = 590
        if y_player1 <  0:
                y_player1 = 0
        #bordas da tela player2
        if x_player2 > 990:
                x_player2 = 990
        if x_player2  < 0:
                x_player2 = 0
        if y_player2  > 590:
                y_player2 = 590
        if y_player2 <  0:
                y_player2 = 0

        pygame.display.update()

# varios codigos repetidos que necessitam refatoramento
