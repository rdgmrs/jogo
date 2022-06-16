import pygame
#import pygame.examples.aliens
#import inspect


class jogador:
        x = 500
        y = 300
        velocidade = 1

def bordas_tela(x,y):
        #bordas da tela  
        if x > 990:
                x = 990
        if x  < 0:
                x = 0
        if y  > 590:
                y = 590
        if y <  0:
                y = 0
        return x,y

def mov_jogador(comandos,x,y,velocidade):
        if comandos[pygame.K_UP]:
                y-= velocidade
        if comandos[pygame.K_DOWN]:
                y+= velocidade
        if comandos[pygame.K_RIGHT]:
                x+= velocidade
        if comandos[pygame.K_LEFT]:
                x-= velocidade           
        
        x,y = bordas_tela(x,y)

        return x,y

def main():
        #dimensoes da tela
        largura = 1000
        altura = 600
        tela = pygame.display.set_mode((largura,altura))
        pygame.display.set_caption('primeiro code pygame')
        #jogador
        Player_1 = jogador()



        while True:
                comandos = pygame.key.get_pressed()
                Player_1.x,Player_1.y = mov_jogador(comandos,Player_1.x,Player_1.y,Player_1.velocidade)
                #Player_1.x,Player_1.y = bordas_tela(Player_1.x,Player_1.y)
                pygame.draw.rect(tela,(0,255,0),(Player_1.x,Player_1.y,10,10))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                pygame.quit()  
                pygame.display.update()
                tela.fill((0,0,0))
        return 0

main()

#pygame.examples.cursors.main()


#try:
#    print(inspect.getsource(pygame.examples.aliens))
#except OSError:
#    print("Source not available, possibly a C module.")
