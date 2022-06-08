# TRY NOT TO DIE
# Main.py

import pygame, sys
from jogador import Jogador
from objetosRuins import ObjetoRuim
from objetosBons import ObjetoBom
from poder import Poder
import random

class Jogo:

    def __init__(self):     
        self.velocidadeJogador = 5
        sprite_jogador = Jogador((larguraTela / 2, alturaTela), larguraTela, self.velocidadeJogador)
        self.jogador = pygame.sprite.GroupSingle(sprite_jogador)

        self.vidas = 4
        self.mostrarVida = pygame.image.load('assets/vida.png').convert_alpha()
        self.vida_x_pos_inicial = larguraTela - (self.mostrarVida.get_size()[0] * 3 + 25)

        self.placar = 0
        self.fonte = pygame.font.Font('assets/coffee-extra.ttf', 20)

        self.objetosRuins = pygame.sprite.Group()

        self.objetosBons = pygame.sprite.Group()

        self.poder = pygame.sprite.Group()

        musica = pygame.mixer.Sound('assets/musica/trynottodie.mp3')
        musica.set_volume(0.1)
        musica.play(loops = -1)
        
        self.tosse = pygame.mixer.Sound('assets/musica/ruim.mp3')
        self.tosse.set_volume(0.3)
        self.mordida = pygame.mixer.Sound('assets/musica/bom.mp3')
        self.mordida.set_volume(0.3)
        self.som = pygame.mixer.Sound('assets/musica/poder.mp3')
        self.som.set_volume(0.3)
    
    def cairObjetoRuim(self):
        posicao = random.randrange(0, 630)
        sprite_objetosRuins = ObjetoRuim(3, alturaTela, posicao)
        self.objetosRuins.add(sprite_objetosRuins)

    def cairObjetoBom(self):
        posicao = random.randrange(0, 630)
        sprite_objetosBons = ObjetoBom(3, alturaTela, posicao)
        self.objetosBons.add(sprite_objetosBons)

    def cairPoder(self):
        posicao = random.randrange(0, 630)
        sprite_poder = Poder(3, alturaTela, posicao)
        self.poder.add(sprite_poder)

    def colisoesObjetosRuins(self):
        if self.objetosRuins:
            for objetoRuim in self.objetosRuins:
                if pygame.sprite.spritecollide(objetoRuim, self.jogador, False):
                    objetoRuim.kill()
                    self.vidas -= 1
                    self.tosse.play()
                    if self.placar <= 0:
                        pass
                    else:
                        self.placar -= 10
                    
                    if self.vidas <= 0:
                        pygame.quit()
                        sys.exit()
                    #('Ah, não! Você até tentou, mas não conseguiu evitar. Sucumbiu aos prazeres momentâneos e morreu.')

    def colisoesObjetosBons(self):
        if self.objetosBons:
            for objetoBom in self.objetosBons:
                if pygame.sprite.spritecollide(objetoBom, self.jogador, False):                         
                    objetoBom.kill()
                    self.mordida.play() 
                    self.placar += 10
    
    def colisoesPoder(self):
        if self.poder:
            for habilidade in self.poder:
                if pygame.sprite.spritecollide(habilidade, self.jogador, False):                         
                    habilidade.kill()
                    self.som.play() 
                    self.placar += 15
                    if self.vidas < 4:
                        self.vidas += 1

    def mostrarVidas(self):
        for vida in range(self.vidas -1):
            x = self.vida_x_pos_inicial + (vida * (self.mostrarVida.get_size()[0] + 10))
            tela.blit(self.mostrarVida, (x, 10))  

    def mostrarPlacar(self):
        mostraPlacar = self.fonte.render(f'Pontos: {self.placar}', False, 'black')
        rectPlacar = mostraPlacar.get_rect(topleft = (10, 10))
        tela.blit(mostraPlacar, rectPlacar)

    def run(self):
        self.jogador.update()
        self.jogador.draw(tela)
        
        self.objetosRuins.update()
        self.colisoesObjetosRuins()
        self.objetosRuins.draw(tela)

        self.objetosBons.update()
        self.colisoesObjetosBons()
        self.objetosBons.draw(tela)

        self.poder.update()
        self.colisoesPoder()
        self.poder.draw(tela)

        self.mostrarVidas()
        self.mostrarPlacar()
     
if __name__ == '__main__':
    pygame.init()

    icone = pygame.image.load("assets/logo.png")
    pygame.display.set_caption("TRY NOT TO DIE")
    pygame.display.set_icon(icone)

    larguraTela = 700
    alturaTela = 700
    tela = pygame.display.set_mode((larguraTela, alturaTela))
    fundo = pygame.image.load("assets/cenario.png")
    relogio = pygame.time.Clock()
    jogo = Jogo()

    quedaObjetoRuim = pygame.USEREVENT 
    pygame.time.set_timer(quedaObjetoRuim, 5000)
    quedaObjetoBom = pygame.USEREVENT + 3
    pygame.time.set_timer(quedaObjetoBom, 1500)
    quedaPoder = pygame.USEREVENT
    pygame.time.set_timer(quedaPoder, 1500)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == quedaObjetoRuim:
                jogo.cairObjetoRuim()

            if evento.type == quedaObjetoBom:
                jogo.cairObjetoBom()
            
            if evento.type == quedaPoder:
                jogo.cairPoder()

        tela.fill((30,30,30))
        tela.blit(fundo, (0, 0))

        jogo.run()

        pygame.display.flip()
        relogio.tick(60)

# Carlos Eduardo dos Santos, Helen Deuner Ferreira e Karoline Z. Soares