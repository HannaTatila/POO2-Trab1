from cln.cdp.Posicao import Posicao

__author__ = 'dell'


class Personagem:

    def __init__(self, eixox, eixoy):
        self.vida = 3
        self.posicao = Posicao(eixox, eixoy)
        self.velocidadey = 0

    def modifica_posicao(self, eixox, eixoy):
        self.posicao.eixox = eixox
        self.posicao.eixoy = eixoy

    def incrementa_vida(self):
        self.vida += 1

    def decrementa_vida(self):
        self.vida -= 1

    def acabou_vida(self):
        return self.vida <= 0

    def atingiu_limite_da_tela(self):
        chao = 445
        teto = 0
        #if peixe encostar no chao ou no teto, ele nao ultrapassa a tela
        if self.posicao.eixoy > chao:
            self.posicao.eixoy = chao
        elif self.posicao.eixoy < teto:
            self.posicao.eixoy = teto
