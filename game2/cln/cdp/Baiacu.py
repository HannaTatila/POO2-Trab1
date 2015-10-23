from cln.cdp.Obstaculo import Obstaculo

__author__ = 'dell'

class Baiacu(Obstaculo):

    def __init__(self, eixox, eixoy):
        self.nome = "baiacu"
        super(Baiacu, self).__init__(eixox, eixoy)

