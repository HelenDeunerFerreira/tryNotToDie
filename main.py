# repo do marcão do jogo do ironman em pygame: https://github.com/profmarcossantos/IronMan2021.2

from operator import index, indexOf
import pygame
import random
import time

pygame.init()

icone = pygame.image.load("assets/logo.png")
pygame.display.set_caption("try not to die")
pygame.display.set_icon(icone)

largura = 700
altura = 700
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/cenario.png")

# coisas boas
agua = pygame.image.load("assets/coisas-boas/agua.png")
banana = pygame.image.load("assets/coisas-boas/banana.png")
brocolis = pygame.image.load("assets/coisas-boas/brocolis.png")
cenoura = pygame.image.load("assets/coisas-boas/cenoura.png")
melancia = pygame.image.load("assets/coisas-boas/melancia.png")

coisasBoas = [agua, banana, brocolis, cenoura, melancia]


def randomCoisasBoas():
    randomico = int(random.choice([0, 1, 2, 3, 4]))
    caindo = pygame.image.load(f"assets/coisas-boas/{coisasBoas[randomico]}")
    return caindo


# coisas ruins
cerveja = pygame.image.load("assets/coisas-ruins/cerveja.png")
cigarro = pygame.image.load("assets/coisas-ruins/cigarro.png")
drogas = pygame.image.load("assets/coisas-ruins/drogas.png")
veneno = pygame.image.load("assets/coisas-ruins/veneno.png")

coisasRuins = [cerveja, cigarro, drogas, veneno]


def caindoCoisasRuins():
    for coisa in coisasRuins:
        print(coisa)

# def randomCoisasRuins():
#     randomico = random.choice([0, 1, 2, 3])

#     for coisa in coisasRuins:
#         objeto = index(coisa)
#         if objeto == randomico:
#             return coisa

#     caindo = coisa
#     return caindo


# mudança misteriosa e personagem
mudancaMisterio = pygame.image.load("assets/mudanca-misteriosa.png")
persoEsquerda = pygame.image.load("assets/personagem-andando-esquerda.png")
persoDireita = pygame.image.load("assets/personagem-andando-direita.png")

# lista de cores em RGB
preto = (0, 0, 0)
branco = (255, 255, 255)


# def text_objetcs(texto, fonte):
#     textSurface = fonte.render(texto, True, preto)
#     return textSurface, textSurface.get_react()


# def message(text):
#     fonte = pygame.font.Font("freesansbold.ttf", 50)
#     TextSurf, TextRect = text_objetcs(text, fonte)
#     TextRect.center = ((largura/2), (altura/2))
#     display.blit(TextSurf, TextRect)
#     pygame.display.update()
#     time.sleep(3)
#     jogo()


# def dead(desvios):
# pygame.mixer.Sound.play(explosaoSom)
# pygame.mixer.music.stop()
# message(
#     f"Ah, não! Você até tentou, mas não conseguiu evitar: sucumbiu aos prazeres momentâneos e morreu. Você morreu por causa de {desvios} coisas ruins")


# def placar(desvios):
#     font = pygame.font.SysFont(None, 25)
#     texto = font.render("Desvios: " + str(desvios), True, branco)
# display.blit(0, 0)


def jogo():
    # pygame.mixer.music.load("assets/ironsound.mp3")
    # pygame.mixer.music.play(-1)  # -1 significa tocar em looping infinito
    personagem = persoEsquerda
    persoPosicaoX = largura * 0.55
    persoPosicaoY = altura * 0.40
    movimentoX = 0
    persoLargura = 360

    missel = caindoCoisasRuins()
    misselPosicaoX = largura * 0.45
    misselPosicaoY = -220
    misselLargura = 50
    misselAltura = 250
    misselVelocidade = 5

    desvios = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -5
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 5
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        persoPosicaoX = persoPosicaoX + movimentoX

        if persoPosicaoX < 0:
            persoPosicaoX = 0
        elif persoPosicaoX > 720:
            # a largura do personagem é 360 (1080 - 360)
            persoPosicaoX = 720 - 360

        display.fill(branco)
        display.blit(fundo, (0, 0))  # insere imagem na tela (imagem , posição)
        # primeiro o fundo, depois o ironman
        display.blit(personagem, (persoPosicaoX, persoPosicaoY))

        display.blit(missel, (misselPosicaoX, misselPosicaoY))
        misselPosicaoY = misselPosicaoY + misselVelocidade

        # quando ultrapassa a barreira começa em um lugar novo aleatório
        if misselPosicaoY > altura:
            # pygame.mixer.Sound.play(misselSom)
            misselPosicaoY = -220
            misselVelocidade += 1
            misselPosicaoX = random.randrange(0, largura)
            desvios += 1

        # análise de colisão
        if persoPosicaoY < misselPosicaoY + misselAltura:
            if persoPosicaoX < misselPosicaoX and persoPosicaoX + persoLargura > misselPosicaoX or misselPosicaoX + misselLargura > persoPosicaoX and misselPosicaoX + misselLargura < persoPosicaoX + persoLargura:
                print('morreu')
                # dead(desvios)

        # placar(desvios)
        pygame.display.update()  # dá update no display
        fps.tick(60)  # 60 frames por segundo


jogo()
