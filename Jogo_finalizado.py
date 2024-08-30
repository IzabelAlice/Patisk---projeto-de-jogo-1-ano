import pygame
from pygame.locals import *
from sys import exit
from random import randint
import os

def abrir_tela_de_entrada(tela):
    imagem = pygame.image.load('sprites/telainicial.png').convert()

    tela.blit(imagem, (0,0))
    pygame.display.flip()
    sair_tela_entrada = False
    while not sair_tela_entrada:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            sair_tela_entrada = event.key == pygame.K_j
            

def abrir_tela_de_saida(tela):
    imagem_final = pygame.image.load('sprites/teladefim.png').convert()

    tela.blit(imagem_final, (0,0))
    pygame.display.flip()
    sair_tela_saida = False
    while not sair_tela_saida:
        event = pygame.event.poll()
        if pygame.key.get_pressed()[K_c]:
            jogo()
        if pygame.key.get_pressed()[K_s]:
            pygame.quit()


            

def jogo():

    #cores
    branco = (255,255,255)
    preto = (0,0,0)
    vermelho = (255,0,0)
    verde = (0,255,0)
    azul = (0,0,255)
    cinza = (139, 123, 139)

    direcao = 0

    pygame. init()

    largura = 600
    altura = 420
    tamanho = 5

    pato_x = largura/2
    pato_y = altura/2

    contador_ovos = 0
    contador_de_vidas = 5

    ovo1_x =  randint(1, 590)
    ovo1_y = randint(20, 380)

    pedra1_x =  randint(1, 579)
    pedra1_y = randint(20, 380)

    pedra2_x =  randint(1, 579)
    pedra2_y = randint(20, 380)

    fonte = pygame.font.SysFont('Pixeled Regular', 25, True, False)

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Patisk")
        
    fundo = pygame.image.load('sprites/fundo_maior.png')

    class Pedra1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('sprites/pedra_final.png'))
            self.image = self.sprites[0]
            self.rect = self.image.get_rect()
            self.pedra_x = randint(1, 579)
            self.pedra_y = randint(20, 380)
            self.rect.center = self.pedra_x, self.pedra_y
            self.image = pygame.transform.scale(self.image, (21*1.7, 9*1.7))
        def redefinir_posicao(self):
            self.pedra_x = randint(1, 579)
            self.pedra_y = randint(20, 380)
        def update(self):
            self.image = self.sprites[0]
            self.rect.x = self.pedra_x
            self.rect.y = self.pedra_y
            self.image = pygame.transform.scale(self.image, (21*1.7, 9*1.7))

    class Pedra2(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('sprites/pedra_final.png'))
            self.image = self.sprites[0]
            self.rect = self.image.get_rect()
            self.rect.center = pedra2_x, pedra2_y
            self.image = pygame.transform.scale(self.image, (21*1.5, 9*1.5))

    class Ovo1(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('sprites/ovo_final.png'))
            self.image = self.sprites[0]
            self.rect = self.image.get_rect()
            self.ovo_x = randint(1, 579)
            self.ovo_y = randint(20, 380)
            self.rect.center = self.ovo_x, self.ovo_y
            self.image = pygame.transform.scale(self.image, (11*1.7, 11*1.7))
        def redefinir_posicao_ovo(self):
            self.ovo_x = randint(1, 579)
            self.ovo_y = randint(20, 380)
        def update(self):
            self.image = self.sprites[0]
            self.rect.x = self.ovo_x
            self.rect.y = self.ovo_y
            self.image = pygame.transform.scale(self.image, (11*1.7, 11*1.7))

    class Pato(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.sprites = []
            self.sprites.append(pygame.image.load('sprites/pato0.png'))
            self.sprites.append(pygame.image.load('sprites/pato1.png'))
            self.sprites.append(pygame.image.load('sprites/pato2.png'))
            self.sprites.append(pygame.image.load('sprites/pato3.png'))
            self.sprites.append(pygame.image.load('sprites/pato4.png'))
            self.sprites.append(pygame.image.load('sprites/pato5.png'))
            self.sprites.append(pygame.image.load('sprites/pato6.png'))
            
            self.sprites.append(pygame.image.load('sprites/pato-0.png'))
            self.sprites.append(pygame.image.load('sprites/pato-1.png'))
            self.sprites.append(pygame.image.load('sprites/pato-2.png'))
            self.sprites.append(pygame.image.load('sprites/pato-3.png'))
            self.sprites.append(pygame.image.load('sprites/pato-4.png'))
            self.sprites.append(pygame.image.load('sprites/pato-5.png'))
            self.sprites.append(pygame.image.load('sprites/pato-6.png'))
            
            self.atual = 0
            self.image = self.sprites[self.atual]
            self.rect = self.image.get_rect()
            self.image = pygame.transform.scale(self.image, (22*3.4, 18*3.4))
            
            self.rect = self.image.get_rect()
            self.rect.topleft = pato_x, pato_y

            self.animar = False
            self.animar2 = False

        def andar_esquerda(self):
            self.animar = True
        def andar_direita(self):
            self.animar2 = True
            
        def update(self):
            if self.animar == True:
                self.atual = self.atual + 0.25
                if self.atual >= 7:
                    self.atual = 0
                if direcao == 0:
                    self.animar = False
                    self.atual == 0
                
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (22*3.4, 18*3.4))
                self.rect.topleft = pato_x, pato_y

            if self.animar2 == True:
                self.atual = self.atual + 0.25
                if self.atual > 7 and self.atual >= 14:
                    self.atual = 7
                if direcao == 0:
                    self.animar2 = False
                    self.atual == 0
                    
                self.image = self.sprites[int(self.atual)]
                self.image = pygame.transform.scale(self.image, (22*3.4, 18*3.4))
                self.rect.topleft = pato_x, pato_y




    todas_as_sprites = pygame.sprite.Group()
    patisk = Pato()
    pedra1 = Pedra1()
    pedra2 = Pedra1()
    pedra3 = Pedra1()
    ovo = Ovo1()
    todas_as_sprites.add(patisk)
    todas_as_sprites.add(pedra1)
    todas_as_sprites.add(pedra2)
    todas_as_sprites.add(pedra3)
    todas_as_sprites.add(ovo)

    grupo_pedra1 = pygame.sprite.Group()
    grupo_pedra1.add(pedra1)

    grupo_pedra2 =  pygame.sprite.Group()
    grupo_pedra2.add(pedra2)

    grupo_pedra3 =  pygame.sprite.Group()
    grupo_pedra3.add(pedra3)

    grupo_ovo = pygame.sprite.Group()
    grupo_ovo.add(ovo)

    relogio = pygame.time. Clock()


    abrir_tela_de_entrada(tela)

        
    sair = True
    while sair:
        relogio.tick(30)
        tela.blit(fundo,(0,0))

        colisoes = pygame.sprite.spritecollide(patisk,grupo_pedra1,False)
        colisoes2 = pygame.sprite.spritecollide(patisk,grupo_pedra2,False)
        colisoes3 = pygame.sprite.spritecollide(patisk,grupo_pedra3,False)
        colisoes4 = pygame.sprite.spritecollide(patisk,grupo_ovo,False)

        mensagem = f'Ovos:{contador_ovos}   Vidas:{contador_de_vidas}'
        texto_formatado =  fonte.render(mensagem, False, branco)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
                    
            if pygame.key.get_pressed()[K_a]:
                direcao = 1
                pato_x = pato_x - 5
                patisk.andar_esquerda()
            if pygame.key.get_pressed()[K_d]:
                pato_x = pato_x + 5
                direcao = 2
                patisk.andar_direita()
            if pygame.key.get_pressed()[K_w]:
                pato_y = pato_y - 5
                direcao = 1
                patisk.andar_esquerda()
            if pygame.key.get_pressed()[K_s]:
                pato_y = pato_y + 5
                direcao = 2
                patisk.andar_direita()
            else:
                direcao = 0

        if colisoes:
            pedra1.redefinir_posicao()
            contador_de_vidas = contador_de_vidas - 1


        if colisoes2:
            pedra2.redefinir_posicao()
            contador_de_vidas = contador_de_vidas - 1

        if colisoes3:
            pedra3.redefinir_posicao()
            contador_de_vidas = contador_de_vidas - 1

        if colisoes4:
            ovo.redefinir_posicao_ovo()
            contador_ovos = contador_ovos + 1

        if contador_de_vidas == 0:
            if event.type == QUIT:
                pygame.quit()
                exit()
            sair = False
            abrir_tela_de_saida(tela)

                    
        if pato_x > largura:
            pato_x = 0
        if pato_x < 0:
            pato_x = largura - tamanho
        if pato_y > altura:
            pato_y = 20
        if pato_y < 20:
            pato_y = altura - tamanho

        todas_as_sprites.draw(tela)
        todas_as_sprites.update()
        tela.blit(texto_formatado, (2, 3))
        pygame.display.flip()
jogo()