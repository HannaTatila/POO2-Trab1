from random import randint
from cln.cdp.PeixeEspada import PeixeEspada
from cln.cdp.Baiacu import Baiacu

__author__ = 'dell'

class FabricaObstaculo(object):

    @staticmethod
    def criarObstaculo(tipo):
        if tipo == 1:
            obstaculo = PeixeEspada(700, randint(0,445))
        elif tipo == 2:
            obstaculo = Baiacu(700, randint(0,445))

        return obstaculo