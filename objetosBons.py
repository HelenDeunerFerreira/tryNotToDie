# TRY NOT TO DIE
# objetosBons.py

import pygame
import random

class ObjetoBom(pygame.sprite.Sprite):
    def __init__(self, velocidade, alturaTela, posicao):
        super().__init__()   
        imgObjetoBom = ['assets/coisas-boas/agua.png', 
                         'assets/coisas-boas/banana.png', 
                         'assets/coisas-boas/brocolis.png',
                         'assets/coisas-boas/cenoura.png',
                         'assets/coisas-boas/melancia.png']
        self.image = pygame.image.load(random.choice(imgObjetoBom)).convert_alpha()
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