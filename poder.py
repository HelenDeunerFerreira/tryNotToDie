# TRY NOT TO DIE
# poder.py

import pygame

class Poder(pygame.sprite.Sprite):
    def __init__(self, velocidade, alturaTela, posicao):
        super().__init__()   
        self.image = pygame.image.load('assets/mudanca-misteriosa.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = velocidade
        self.alturaMaxima = alturaTela
        self.rect.x = posicao  
    
    def destruir(self):
        if self.rect.y <= 0:
            self.kill()

    def cair(self):
        self.rect.y += self.speed

    def update(self):
        self.cair()
        self.destruir()

# Carlos Eduardo dos Santos, Helen Deuner Ferreira e Karoline Z. Soares