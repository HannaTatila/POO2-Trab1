from cln.cdp.Obstaculo import Obstaculo

__author__ = 'dell'

class PeixeEspada(Obstaculo):

    def __init__(self, eixox, eixoy):
        self.nome = "peixeespada"
        super(PeixeEspada, self).__init__(eixox, eixoy)

