__author__ = 'dell'

import unittest
from cln.cgt.AplJogo import AplJogo


class Test(unittest.TestCase):

    def testAumenta_velocidade_personagem(self):
        aplJogo = AplJogo()
        aplJogo.aumenta_velocidade()
        self.assertEqual(10, aplJogo.personagem.velocidadey, "nao igual ao retorno")

    def testAumenta_diminui_personagem(self):
        aplJogo = AplJogo()
        aplJogo.diminui_velocidade()
        self.assertEqual(-15, aplJogo.personagem.velocidadey, "nao igual ao retorno")

    def testMovimenta_personagem(self):
        aplJogo = AplJogo()
        aplJogo.aumenta_velocidade()
        aplJogo.movimenta_personagem()
        self.assertEqual(260, aplJogo.personagem.posicao.eixoy, "nao igual ao retorno")

    def testVerifica_qtd_de_vidas(self):
        aplJogo = AplJogo()
        aplJogo.verifica_qtd_de_vidas()
        self.assertEqual(3, aplJogo.personagem.vida, "nao igual ao retorno")

if __name__ == "__main__":
    unittest.main()
