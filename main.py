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
        # Inicialização Jogador
        self.velocidadeJogador = 5
        sprite_jogador = Jogador((larguraTela / 2, alturaTela), larguraTela, self.velocidadeJogador)
        self.jogador = pygame.sprite.GroupSingle(sprite_jogador)
        
        # Inicialização Vidas
        self.vidas = 4
        self.mostrarVida = pygame.image.load('assets/vida.png').convert_alpha()
        self.vida_x_pos_inicial = larguraTela - (self.mostrarVida.get_size()[0] * 3 + 25)

        # Inicialização Placar
        self.placar = 0
        self.fonte = pygame.font.Font('assets/coffee-extra.ttf', 20)

        # Inicialização Objetos Ruins
        self.objetosRuins = pygame.sprite.Group()

        # Inicialização Objetos Bons
        self.objetosBons = pygame.sprite.Group()

        # Inicialização Poderes
        self.poderes = pygame.sprite.Group()

        # Inicialização Música
        musica = pygame.mixer.Sound('assets/musica/trynottodie.mp3')
        musica.set_volume(0.1)
        musica.play(loops = -1)
      
        # Inicialização Efeitos
        self.tosse = pygame.mixer.Sound('assets/musica/ruim.mp3')
        self.tosse.set_volume(0.3)
        self.mordida = pygame.mixer.Sound('assets/musica/bom.mp3')
        self.mordida.set_volume(0.3)
        self.som = pygame.mixer.Sound('assets/musica/poder.mp3')
        self.som.set_volume(0.3)
    
    # Métodos
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
        self.poderes.add(sprite_poder)

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
                    
                    if self.vidas == 0:
                        fimDeJogo()

    def colisoesObjetosBons(self):
        if self.objetosBons:
            for objetoBom in self.objetosBons:
                if pygame.sprite.spritecollide(objetoBom, self.jogador, False):                         
                    objetoBom.kill()
                    self.mordida.play() 
                    self.placar += 10
    
    def colisoesPoder(self):
        if self.poderes:
            for poder in self.poderes:
                if pygame.sprite.spritecollide(poder, self.jogador, False):                                          
                    poder.kill()
                    self.som.play() 
                    self.placar += 15 
                    self.pegouPoder()

    def pegouPoder(self):
            habilidade = random.randrange(0, 1)          
            # Vida Extra
            if habilidade == 0:
                if self.vidas < 4:
                    self.vidas += 1
            # Incremento de Velocidade ao Jogador              
            elif habilidade == 1: 
                if self.velocidadeJogador < 20:
                    self.velocidadeJogador += 1
            else:
                pass

    def mostrarVidas(self):
        for vida in range(self.vidas -1):
            x = self.vida_x_pos_inicial + (vida * (self.mostrarVida.get_size()[0] + 10))
            tela.blit(self.mostrarVida, (x, 10))  

    def mostrarPlacar(self):
        mostraPlacar = self.fonte.render(f'Points: {self.placar}', False, 'black')
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

        self.poderes.update()
        self.colisoesPoder()
        self.poderes.draw(tela)

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
    fonte = pygame.font.Font('assets/coffee-extra.ttf', 20)
    relogio = pygame.time.Clock()
    jogo = Jogo()

    # Eventos
    quedaObjetoRuim = pygame.USEREVENT 
    pygame.time.set_timer(quedaObjetoRuim, 5000)
    quedaObjetoBom = pygame.USEREVENT + 3
    pygame.time.set_timer(quedaObjetoBom, 1500)
    quedaPoder = pygame.USEREVENT + 2
    pygame.time.set_timer(quedaPoder, 30000)

    def jogar():
        # Loop de Jogo
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
    
    def menuPrincipal():
        while True:
            tela.fill((30,30,30))
            tela.blit(fundo, (0, 0))
            tela.blit(icone, (135, 100))
            mostraTecla = fonte.render('Press the Space Key to Play', False, 'black')
            rectTecla = mostraTecla.get_rect(center = (larguraTela /2 , 560))
            tela.blit(mostraTecla, rectTecla)
            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_SPACE]:
                jogar() 

            if teclas[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()  

    def fimDeJogo():
        while True:
            tela.fill((30,30,30))
            tela.blit(fundo, (0, 0))
            tela.blit(icone, (135, 100))
            mostraMensagem = fonte.render('You tried, but succumbed to the Bad Things in the world!', False, 'black')
            rectMensagem = mostraMensagem.get_rect(center = (larguraTela /2 , 560))
            tela.blit(mostraMensagem, rectMensagem)
            mostraTecla = fonte.render('Press the Escape Key to exit', False, 'black')
            rectTecla = mostraTecla.get_rect(center = (larguraTela /2 , 580)) 
            tela.blit(mostraTecla, rectTecla)

            pygame.display.flip()

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            teclas = pygame.key.get_pressed()
 
            if teclas[pygame.K_ESCAPE]:
                pygame.quit()
                sys.exit()   

    menuPrincipal()

# Carlos Eduardo dos Santos, Helen Deuner Ferreira e Karoline Z. Soares