import pygame, os

__author__ = 'dell'


class TelaMenu:

    def __init__(self):
        pygame.init()
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.tela = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("Mar&moto")

    def exibe_imagem(self, caminhoimagem, nomeimagem, posicao):
        imagem = pygame.image.load(os.path.join(caminhoimagem, nomeimagem))
        self.tela.blit(imagem, (posicao.eixox,posicao.eixoy))
        return imagem

    def exibe_texto_menu(self, texto, tam, cor, x, y):
        fonte = pygame.font.SysFont("Agency FB", tam, False, False)
        t = fonte.render(texto, True, cor)
        self.tela.blit(t, (x, (self.tamanhotelay/2)+y))