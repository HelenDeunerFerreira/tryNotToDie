# TRY NOT TO DIE
# jogador.py

import pygame

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao, limiteTela, velocidade):
        super().__init__()
        self.image = pygame.image.load("assets/personagem-andando-direita.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom = posicao)
        self.speed = velocidade
        self.larguraMaxima = limiteTela

    def get_input(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.image = pygame.image.load("assets/personagem-andando-direita.png").convert_alpha()
            self.rect.x += self.speed
        elif teclas[pygame.K_LEFT]:  
            self.image = pygame.image.load("assets/personagem-andando-esquerda.png").convert_alpha()
            self.rect.x -= self.speed

    def limiteTela(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.larguraMaxima:
            self.rect.right = self.larguraMaxima
    
    def update(self):
        self.get_input()
        self.limiteTela()

# Carlos Eduardo dos Santos, Helen Deuner Ferreira e Karoline Z. Soares

            


