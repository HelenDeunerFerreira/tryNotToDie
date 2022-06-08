# TRY NOT TO DIE
# objetosRuins.py

import pygame
import random

class ObjetoRuim(pygame.sprite.Sprite):
    def __init__(self, velocidade, alturaTela, posicao):
        super().__init__()   
        imgObjetoRuim = ['assets/coisas-ruins/cerveja.png', 
                         'assets/coisas-ruins/cigarro.png', 
                         'assets/coisas-ruins/drogas.png',
                         'assets/coisas-ruins/veneno.png']
        self.image = pygame.image.load(random.choice(imgObjetoRuim)).convert_alpha()
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