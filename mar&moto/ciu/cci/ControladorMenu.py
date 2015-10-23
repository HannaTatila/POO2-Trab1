from ciu.cci.Controlador import Controlador
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.Posicao import Posicao
import pygame, os
from pygame import KEYDOWN, KEYUP
from pygame import QUIT, K_DOWN, K_UP, K_RIGHT, K_LEFT, K_RETURN, K_ESCAPE

__author__ = 'dell'


class ControladorMenu():

    def __init__(self):
        pygame.init()
        self.telamenu = TelaMenu()
        self.controlador = Controlador()
        self.caminhoimagem = (os.getcwd()).replace("principal",os.path.join("recursos","imagem"))


    def exibir_tela_menu(self):
        self.telamenu.exibe_imagem(self.caminhoimagem, "fundo2.jpg", Posicao(0,0))
        self.telamenu.exibe_imagem(self.caminhoimagem, "nome2.png", Posicao(150,140))

    def exibe_opcoes_menu(self, id):
        tam1 = 30
        tam2 = 30
        tam3 = 30
        tam4 = 30
        cor1 = (80,80,80)
        cor2 = (80,80,80)
        cor3 = (80,80,80)
        cor4 = (80,80,80)
        if id == 1:
            tam1 = 40
            cor1 = (0,0,0)
        if id == 2:
            tam2 = 40
            cor2 = (0,0,0)
        if id == 3:
            tam3 = 40
            cor3 = (0,0,0)
        if id == 4:
            tam4 = 40
            cor4 = (0,0,0)

        self.telamenu.exibe_texto_menu("INICIAR", tam1, cor1, 302, 30)
        self.telamenu.exibe_texto_menu("CADASTRAR", tam2, cor2, 302, 70)
        self.telamenu.exibe_texto_menu("CONFIGURACOES", tam3, cor3, 302, 110)
        self.telamenu.exibe_texto_menu("SAIR", tam4, cor4, 302, 150)


    #TODO refatorar toda a parte do menu
    def fixo(self, menuselecao):
        if menuselecao == 1:
            self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif", Posicao(245, 260))
        elif menuselecao == 2:
            self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif", Posicao(245, 300))
        elif menuselecao == 3:
            self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif", Posicao(245, 340))
        elif menuselecao == 4:
            self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif", Posicao(245, 380))

    def selecao(self, menuselecao):
        ## TELA 1
        if menuselecao == 1:
            self.exibe_opcoes_menu(menuselecao)
        elif menuselecao == 2:
            self.exibe_opcoes_menu(menuselecao)
        elif menuselecao == 3:
            self.exibe_opcoes_menu(menuselecao)
        elif menuselecao == 4:
            self.exibe_opcoes_menu(menuselecao)

        ## REGRAS DA TELA 1:
        if menuselecao < 1: #nao incrementar estado se apertar p cima de novo
            menuselecao = 1
        elif menuselecao == 5: #nao incrementar estado se apertar p baixo de novo
            menuselecao = 4
        elif menuselecao == 13: # PARA, POR ENQUANTO, NAO FUNCIONAR NADA EM CONFIGURACOES
            menuselecao = 3
        elif menuselecao == 14: # se escolher a opcao 'SAIR'
            exit()
        elif menuselecao == 12: #se der enter na opcao 'CADASTRAR'
            menuselecao = 200
        elif menuselecao == 11:
            self.controlador.jogo()

        ## TELA 2
        elif menuselecao == 200:
            self.telamenu.exibe_texto_menu("NOME: ", 40, (0,0,0), 105, 22)
            pygame.draw.rect(self.telamenu.tela, (255,255,255), (205,270,300,30), 0)
            self.telamenu.exibe_texto_menu("VOLTAR", 30, (80,80,80), 302, 70)
            pygame.display.flip()
            menuselecao = self.cadastrar()
        elif menuselecao == 201:
            self.fixo(2)
            self.telamenu.exibe_texto_menu("Nome cadastrado com sucesso!", 30, (80,80,80), 200, 22)
            self.telamenu.exibe_texto_menu("VOLTAR", 40, (0,0,0), 302, 70)

        ## REGRAS DA TELA 2
        elif (menuselecao == 210) | (menuselecao == 199): # por enquanto, so escreve o nome na tela, mas nao persiste os dados
            menuselecao = 200
        elif menuselecao == 202: #nao incrementar estado se apertar p baixo de novo
            menuselecao = 201
        elif menuselecao == 211: #se clicar em voltar, volta para o menu inical
            menuselecao = 1

        return menuselecao

    def menu(self):
        menuselecao = 1
        while True:
            self.exibir_tela_menu()
            self.fixo(menuselecao)
            menuselecao = self.selecao(menuselecao)
            pygame.display.update()
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
                if e.type == KEYDOWN:
                    if e.key == K_DOWN:
                        menuselecao += 1
                    if e.key == K_UP:
                        menuselecao -= 1
                    if e.key == K_RETURN:
                        menuselecao += 10
                    if e.key == K_ESCAPE:
                        menuselecao -= 10

#---------------------------------------------------- Cadastro

    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key
            else:
              pass


    def imprime_nome(self, nome_corrente, tela):
        nome = ""
        for i in range(len(nome_corrente)):
            nome = nome + nome_corrente[i]

        fonte = pygame.font.SysFont("ARIAL", 24, False, False)
        texto = fonte.render(nome, True, (0,0,0))
        tela.blit(texto, (215,270))
        pygame.display.flip()
        return nome

    def escreve_arquivo(self, nome):
        arq = open("ranking.txt", "a")
        arq.write(nome + " ")

    def cadastrar(self):
        nome_corrente = []
        nome = ""
        while True:
            tecla = self.get_key()
            if tecla == K_RETURN:
                self.escreve_arquivo(nome)
                return 201
            elif tecla <= 127:
                nome_corrente.append(chr(tecla))
                nome = self.imprime_nome(nome_corrente, self.telamenu.tela)




