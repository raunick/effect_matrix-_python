import pygame
import random
import sys

# Inicialização do Pygame
pygame.init()

# Definições de cores e dimensões
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)

# Criar a tela do Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix")

# Definir a fonte e tamanho
font_size = 20
font = pygame.font.SysFont('montserrat', font_size)

# Configurações de letras (números de colunas baseados na largura da tela)
columns = WIDTH // font_size
drops = [0] * columns  # Lista para manter a posição de queda das letras em cada coluna

# Função para desenhar o efeito Matrix com degradê
def draw_matrix():
    # Preencher a tela com preto, mas ligeiramente transparente para criar um efeito de desvanecimento
    screen.fill((0, 0, 0, 25))  # Fundo escurecendo suavemente
    
    # Percorrer cada coluna
    for i in range(len(drops)):
        # Criar o degradê de verde
        for j in range(10):  # 10 níveis de degradê
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            brightness = 255 - j * 25  # Controla o brilho da gota, criando o degradê
            green_color = (0, brightness, 0)
            text = font.render(char, True, green_color)

            # Desenhar a letra na tela
            s 

        # Mover a "gota" para baixo
        drops[i] += 1

        # Resetar a gota para o topo de forma aleatória
        if drops[i] * font_size > HEIGHT or random.random() > 0.95:
            drops[i] = 0

# Função principal para rodar o loop
def matrix():
    clock = pygame.time.Clock()

    # Loop principal
    while True:
        # Checar eventos como o fechamento da janela
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Chamar a função para desenhar o efeito Matrix com degradê
        draw_matrix()

        # Atualizar a tela
        pygame.display.flip()

        # Controlar a taxa de atualização
        clock.tick(10)

# Executar o efeito Matrix
matrix()
