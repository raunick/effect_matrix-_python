
# Efeito Matrix com Pygame 💻💡

Este projeto implementa um efeito de letras caindo inspirado no filme "Matrix", utilizando a biblioteca Pygame em Python. O efeito simula os icônicos caracteres verdes caindo com um rastro esmaecido.

## Funcionalidades 🌟

- Caracteres caindo, inspirados pelo filme "Matrix".
- Efeito de desvanecimento suave atrás das letras.
- Tamanho da tela, tamanho da fonte e velocidade ajustáveis.

## Pré-requisitos 🛠️

Certifique-se de ter o Python instalado no seu sistema, junto com a biblioteca `pygame`.

Você pode instalar o Pygame usando o seguinte comando:

```bash
pip install pygame
```

## Executando o Programa 🚀

1. Clone o repositório ou faça o download do código fonte.
2. Execute o script Python:

```bash
python matrix_effect.py
```

Isso abrirá uma janela com o efeito de letras caindo.

## Visão Geral do Código 🔍

### Importação de Bibliotecas

```python
import pygame
import random
import sys
```

O script utiliza `pygame` para renderizar os efeitos visuais, `random` para gerar letras aleatórias e `sys` para manipular a saída do programa.

### Configurações da Tela

```python
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
```

As dimensões da tela são configuradas para 800x600 pixels, e a cor de fundo é preta.

### Fonte e Colunas

```python
font_size = 20
font = pygame.font.SysFont('montserrat', font_size)
columns = WIDTH // font_size
drops = [0] * columns
```

O tamanho da fonte é definido como 20, e a tela é dividida em colunas com base na largura e no tamanho da fonte. O array `drops` rastreia a posição vertical das letras caindo em cada coluna.

### Desenhando o Efeito Matrix

A função `draw_matrix()` cria o efeito de letras caindo com um degradê.

```python
def draw_matrix():
    screen.fill((0, 0, 0, 25))  # Fundo ligeiramente transparente para efeito de desvanecimento
    for i in range(len(drops)):
        for j in range(10):
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            brightness = 255 - j * 25  # Controla o degradê
            green_color = (0, brightness, 0)
            text = font.render(char, True, green_color)
            screen.blit(text, (i * font_size, drops[i] * font_size))
        drops[i] += 1
        if drops[i] * font_size > HEIGHT or random.random() > 0.95:
            drops[i] = 0
```

### Loop Principal

A função `matrix()` executa o loop principal do evento, que continuamente atualiza a tela para exibir as letras caindo.

```python
def matrix():
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        draw_matrix()
        pygame.display.flip()
        clock.tick(10)
```

### Como Funciona 🔧

- Cada coluna na matriz tem uma "gota" de caracteres caindo.
- Quando uma gota atinge o fundo ou aleatoriamente, ela é reiniciada no topo da tela.
- A tela é atualizada com um fundo preto ligeiramente transparente para criar o efeito de desvanecimento.

## Customização ✏️

- **Tamanho da Tela**: Ajuste as variáveis `WIDTH` e `HEIGHT` para alterar o tamanho da janela.
- **Tamanho da Fonte**: Modifique a variável `font_size` para fazer os caracteres maiores ou menores.
- **Velocidade**: Modifique o `clock.tick(10)` para controlar a velocidade das letras caindo (número menor = mais rápido).

## Licença 📜

Este projeto está licenciado sob a licença MIT. Você é livre para usar e modificar o código.

## Agradecimentos 🙌

Inspirado pelo efeito visual icônico de caracteres caindo do filme "Matrix".
