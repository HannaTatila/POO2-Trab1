import pygame, os

__author__ = 'dell'


class TelaJogo:

    def __init__(self):
        self.branco = (255,255,255)
        self.preto = (0,0,0)
        self.ceu = (192,217,217)
        pygame.init()
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.tela = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("Mar&moto")


    def exibe_imagem(self, caminhoimagem, nomeimagem, posicao):
        imagem = pygame.image.load(os.path.join(caminhoimagem, nomeimagem))
        self.tela.blit(imagem, (posicao.eixox,posicao.eixoy))
        return imagem

    def exibe_texto(self, texto, tamanhofonte, posicao):
        font = pygame.font.SysFont(None, tamanhofonte)
        text = font.render(texto, True, self.branco)
        self.tela.blit(text, posicao)





