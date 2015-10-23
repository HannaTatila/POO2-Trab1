from random import randint
import pygame
from cln.cdp.EntradaUsuario import EntradaUsuario
from cln.cdp.Personagem import Personagem
from cln.cgt.FabricaObstaculo import FabricaObstaculo

__author__ = 'dell'


class AplJogo:

    def __init__(self):
        self.personagem = Personagem(350, 250)
        self.pontos = 0
        self.pontosatual = 0
        self.fimdejogo = False
        self.desceu = True
        self.obstaculos = list()
        self.novo = 44


    def config(self):
        self.clock = pygame.time.Clock()
        self.entradas = EntradaUsuario()

    def player_input(self):
        for event in pygame.event.get():
            self.entradas.reset()
            if event.type == pygame.QUIT:
                self.entradas.quit_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.entradas.quit_pressed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.diminui_velocidade()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.aumenta_velocidade()
            pygame.key.set_repeat(1)

    def aumenta_velocidade(self):
        self.personagem.velocidadey = 10

    def diminui_velocidade(self):
        self.personagem.velocidadey = -15

    def movimenta_personagem(self):
        self.personagem.modifica_posicao(self.personagem.posicao.eixox, self.personagem.posicao.eixoy + self.personagem.velocidadey)

    def cria_obstaculos(self):
        if self.novo == 45:
            self.novo = 0
            if len(self.obstaculos) < 3:
                self.obstaculos.append(FabricaObstaculo.criarObstaculo(randint(1,2)))

    def movimenta_obstaculo_horizontalmente(self):
        for obs in self.obstaculos:
            obs.modifica_posicao(obs.posicao.eixox - obs.velocidadex, obs.posicao.eixoy)

    def movimenta_obstaculo_verticalmente(self):
        for obs in self.obstaculos:
            if obs.posicao.eixoy <= 0:
                self.desceu = True
            elif obs.posicao.eixoy >= 450:
                self.desceu = False

            if self.desceu == True:
                obs.desce()
            elif self.desceu == False:
                obs.sobe()

    def verifica_limite_da_tela(self):
        self.personagem.atingiu_limite_da_tela()

    def incrementa_pontuacao(self):
        for obs in self.obstaculos:
            if self.personagem.posicao.eixox > obs.posicao.eixox and self.personagem.posicao.eixox < obs.posicao.eixox+10:
                self.pontos += 1

    def remove_obstaculo(self):
        if self.obstaculos[0].posicao.eixox < -80:
            del self.obstaculos[0]

    def verifica_colisao(self, rect1, rect2):
        if rect1.colliderect(rect2) and self.pontos != self.pontosatual:
            self.personagem.vida -= 1
            self.pontosatual = self.pontos

    def verifica_qtd_de_vidas(self):
        if self.personagem.acabou_vida():
            self.fimdejogo = True
            self.personagem.velocidadey = 0
            for obs in self.obstaculos:
                obs.velocidadex = 0

    def jogar(self):
        self.player_input()
        self.movimenta_personagem()
        self.cria_obstaculos()
        self.movimenta_obstaculo_horizontalmente()
        self.movimenta_obstaculo_verticalmente()
        self.remove_obstaculo()
        self.verifica_limite_da_tela()
        self.verifica_qtd_de_vidas()
        self.incrementa_pontuacao()
        if self.entradas.quit_pressed:
            exit(0)
        pygame.display.flip()
        self.clock.tick(60)

