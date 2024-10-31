import pygame
import random

# Inicializando o pygame
pygame.init()

# Definindo cores
COR_PRETA = (0, 0, 0)
COR_BRANCA = (255, 255, 255)
COR_VERMELHA = (213, 50, 80)
COR_VERDE = (0, 255, 0)
COR_AZUL = (50, 153, 213)

# Dimensões da tela
largura = 800
altura = 600

# Configurações da janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo da Minhoca")

# Configurações da cobra
tamanho_bloco = 20
velocidade = 15

# Fonte para pontuação
fonte_pontuacao = pygame.font.SysFont("comicsansms", 35)

# Função para exibir a pontuação
def mostrar_pontuacao(pontos):
    valor = fonte_pontuacao.render("Pontuação: " + str(pontos), True, COR_BRANCA)
    tela.blit(valor, [0, 0])

# Função principal do jogo
def jogo():
    fim_jogo = False
    fechar_jogo = False

    # Posições iniciais da cobra
    x_cobra = largura / 2
    y_cobra = altura / 2

    # Mudança de posição
    x_mudanca = 0
    y_mudanca = 0

    # Corpo da cobra
    corpo_cobra = []
    comprimento_cobra = 1

    # Posição inicial da comida
    x_comida = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    y_comida = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    # Relógio para controle da velocidade
    relogio = pygame.time.Clock()

    while not fim_jogo:

        while fechar_jogo:
            tela.fill(COR_PRETA)
            mensagem = fonte_pontuacao.render("Fim de Jogo! Pressione C para Continuar ou S para Sair", True, COR_VERMELHA)
            tela.blit(mensagem, [largura / 6, altura / 3])
            mostrar_pontuacao(comprimento_cobra - 1)
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_c:
                        jogo()
                    if evento.key == pygame.K_s:
                        fim_jogo = True
                        fechar_jogo = False

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_mudanca = -tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_RIGHT:
                    x_mudanca = tamanho_bloco
                    y_mudanca = 0
                elif evento.key == pygame.K_UP:
                    y_mudanca = -tamanho_bloco
                    x_mudanca = 0
                elif evento.key == pygame.K_DOWN:
                    y_mudanca = tamanho_bloco
                    x_mudanca = 0

        # Verifica colisão com as bordas
        if x_cobra >= largura or x_cobra < 0 or y_cobra >= altura or y_cobra < 0:
            fechar_jogo = True

        # Atualiza posição da cabeça da cobra
        x_cobra += x_mudanca
        y_cobra += y_mudanca

        tela.fill(COR_PRETA)
        pygame.draw.rect(tela, COR_VERDE, [x_comida, y_comida, tamanho_bloco, tamanho_bloco])

        # Atualiza o corpo da cobra
        cabeca_cobra = [x_cobra, y_cobra]
        corpo_cobra.append(cabeca_cobra)
        if len(corpo_cobra) > comprimento_cobra:
            del corpo_cobra[0]

        # Verifica colisão com o próprio corpo
        for parte in corpo_cobra[:-1]:
            if parte == cabeca_cobra:
                fechar_jogo = True

        # Desenha a cobra
        for parte in corpo_cobra:
            pygame.draw.rect(tela, COR_AZUL, [parte[0], parte[1], tamanho_bloco, tamanho_bloco])

        mostrar_pontuacao(comprimento_cobra - 1)
        pygame.display.update()

        # Verifica se a cobra comeu a comida
        if x_cobra == x_comida and y_cobra == y_comida:
            x_comida = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            y_comida = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 1

        relogio.tick(velocidade)

    pygame.quit()
    quit()

# Inicia o jogo
jogo()
