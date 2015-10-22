from ciu.cih.TelaJogo import TelaJogo
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.Posicao import Posicao
from cln.cgt.AplJogo import AplJogo
import pygame,os

__author__ = 'dell'


class Controlador():

    def __init__(self):
        pygame.init()
        self.apljogo = AplJogo()
        self.telajogo = TelaJogo()
        self.telamenu = TelaMenu()
        self.caminhoimagem = (os.getcwd()).replace("principal",os.path.join("recursos","imagem"))
        self.xtela = 0

    def exibir_tela_jogo(self):
        self.telajogo.exibe_imagem(self.caminhoimagem, "fundo8.png", Posicao(self.xtela,0))
        self.xtela -= 5
        if self.xtela == -500:
            self.xtela = 0

    def exibir_personagem(self, posicao):
        imagem = self.telajogo.exibe_imagem(self.caminhoimagem, "peixa.png", posicao)
        rect = imagem.get_rect().move(posicao.eixox, posicao.eixoy)
        return rect

    def exibir_obstaculo(self, posicao):
        imagem = self.telajogo.exibe_imagem(self.caminhoimagem, "peixeespada.png", posicao)
        rect = imagem.get_rect().move(posicao.eixox, posicao.eixoy)
        return rect

    def exibir_vida(self, x, y):
        self.telajogo.exibe_imagem(self.caminhoimagem, "vida.png", Posicao(x,y))

    def exibir_pontuacao(self, pontos):
        self.telajogo.exibe_texto("Score: "+str(pontos), 40, [10,50])

    def exibir_fim_de_jogo(self):
        self.telajogo.exibe_texto("Game Over", 75, [200,250])
        self.xtela = 0

    def controla_vida(self):
        x = 0
        for auxvida in range(self.apljogo.personagem.vida):
            self.exibir_vida(x, 0)
            x += 40

    def jogo(self):
        self.apljogo.config()
        while True:
            self.apljogo.jogar()

            self.exibir_tela_jogo()
            rect1 = self.exibir_personagem(self.apljogo.personagem.posicao)
            rect2 = self.exibir_obstaculo(self.apljogo.obstaculo.posicao)
            rect3 = self.exibir_obstaculo(self.apljogo.obstaculo2.posicao)
            self.apljogo.verifica_colisao(rect1, rect2)
            self.apljogo.verifica_colisao(rect1, rect3)

            self.exibir_pontuacao(self.apljogo.pontos)
            self.controla_vida()
            if self.apljogo.fimdejogo == True:
                self.exibir_fim_de_jogo()
        pygame.quit()

