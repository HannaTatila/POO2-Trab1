from cln.cdp.Posicao import Posicao

__author__ = 'dell'


class Obstaculo:

    def __init__(self, eixox, eixoy):
        self.posicao = Posicao(eixox, eixoy)
        self.velocidadex = 9

    def modifica_posicao(self, eixox, eixoy):
        self.posicao.eixox = eixox
        self.posicao.eixoy = eixoy

    def desce(self):
        self.posicao.eixoy += 7

    def sobe(self):
        self.posicao.eixoy -= 7