# Snake Game - Kodland Edition

Este projeto é uma implementação do clássico jogo da cobrinha (Snake) desenvolvido em Python, utilizando a biblioteca PgZero. O jogo foi desenvolvido como parte de um desafio educacional, com restrições específicas sobre bibliotecas permitidas e funcionalidades obrigatórias.

## Descrição

O jogador controla uma cobra que cresce ao comer maçãs espalhadas pela tela. O objetivo é obter a maior pontuação possível sem colidir com as paredes ou com o próprio corpo da cobra.

## Funcionalidades

- Menu inicial com três botões funcionais: Iniciar, Música (ligar/desligar) e Sair.
- Execução de música de fundo durante o jogo.
- Efeitos sonoros distintos para a coleta de maçã e para o Game Over.
- Sprite personalizada para cabeça, corpo e cauda da cobra.
- Sprite de maçã com imagem.
- Tela de fundo com imagem customizada.
- Sistema de pausa acionado pela tecla espaço.
- Contador de pontuação exibido em tempo real.

## Controles

- Setas do teclado (↑, ↓, ←, →): controlam o movimento da cobra.
- Tecla Espaço: pausa e retoma o jogo.
- Mouse: usado para interagir com os botões do menu.

## Como executar

1. Certifique-se de ter o Python 3.13+ instalado.
2. Instale a biblioteca PgZero:
   ```bash
   pip install pgzero
   ```
3. Execute o jogo com o comando:
   ```bash
   pgzrun main.py
   ```

## Estrutura de diretórios esperada

O jogo espera a seguinte estrutura de diretórios:

```
project/
│
├── main.py
├── images/
│   ├── background.png
│   ├── apple.png
│   ├── snake.png
│   ├── snake_head_up.png
│   ├── snake_head_down.png
│   ├── snake_head_left.png
│   ├── snake_head_right.png
│   ├── snake_tail_up.png
│   ├── snake_tail_down.png
│   ├── snake_tail_left.png
│   ├── snake_tail_right.png
│
├── sounds/
│   ├── collect.wav
│   ├── gameover.wav
│
├── music/
│   ├── music.mp3
```

## Requisitos do Desafio

- Utilização apenas de `pgzrun`, `random` e `Rect` (do pygame).
- Implementação de interface gráfica simples e funcional.
- Sem utilização de bibliotecas gráficas adicionais como Pygame completo.
- Sprites e sons devidamente organizados nas pastas padrão do PgZero.

## Autor

Arly Alves  
Desenvolvido como parte do desafio Kodland para ensino de lógica e programação com Python.
