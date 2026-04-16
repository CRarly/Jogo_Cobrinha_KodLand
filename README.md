# Snake Game - KodLand

![Thumbnail do jogo](docs/images/gameplay_screen1.png)

Projeto de um jogo no estilo **Snake**, desenvolvido em **Python** com **Pygame Zero (PgZero)**. O jogador controla a cobra em uma grade, coleta maçãs para aumentar a pontuação e precisa evitar colisões com as bordas da tela e com o próprio corpo.

## Documentação do projeto

- [GDD - Game Design Document](docs/GDD.md)
- [SDD - Sound Design Document](docs/SDD.md)

## Visão geral

Este projeto apresenta uma versão educacional do clássico jogo da cobrinha, com foco em simplicidade de implementação, organização de assets e documentação. A proposta é servir tanto como jogo casual quanto como material de estudo introdutório para desenvolvimento de jogos 2D com Python.

## Principais funcionalidades

- menu inicial com botões de **Start**, **Music** e **Exit**;
- movimentação da cobra em grade;
- sistema de pontuação em tempo real;
- crescimento da cobra ao coletar maçãs;
- colisão com paredes e com o próprio corpo;
- pausa com tecla de espaço;
- música de fundo com alternância no menu;
- efeitos sonoros para coleta e game over.

## Tecnologias utilizadas

- **Python 3**
- **Pygame Zero (PgZero)**
- módulo padrão **random**

## Como executar

1. Instale o **Python 3**.
2. Instale o **PgZero**:

```bash
pip install pgzero
```

3. Execute o projeto na pasta raiz:

```bash
pgzrun main.py
```

## Controles

- **Setas direcionais**: movimentam a cobra.
- **Barra de espaço**: pausa ou retoma a partida.
- **Mouse**: interage com os botões do menu.

## Regras do jogo

- O objetivo é alcançar a maior pontuação possível.
- Cada maçã coletada soma **1 ponto**.
- Ao coletar uma maçã, a cobra cresce.
- O jogo termina quando a cobra colide com:
  - as bordas da tela;
  - o próprio corpo.

## Estrutura do projeto

```text
Jogo_Cobrinha_KodLand-main/
├── main.py
├── README.md
├── docs/
│   ├── GDD.md
│   ├── SDD.md
│   └── images/
│       ├── gameplay_screen.png
│       └── menu_screen.png
├── images/
│   ├── apple.png
│   ├── background.png
│   ├── snake.png
│   ├── snake_head_down.png
│   ├── snake_head_left.png
│   ├── snake_head_right.png
│   ├── snake_head_up.png
│   ├── snake_tail_down.png
│   ├── snake_tail_left.png
│   ├── snake_tail_right.png
│   ├── snake_tail_up.png
│   └── thumbnail.png
├── music/
│   └── music.mp3
└── sounds/
    ├── collect.wav
    └── gameover.wav
```

## Organização dos assets

- `images/`: sprites da cobra, maçã e plano de fundo;
- `music/`: trilha principal do jogo;
- `sounds/`: efeitos sonoros de feedback;
- `docs/`: documentação de design do jogo e design sonoro.

## Observações

- A lógica principal está concentrada em `main.py`, o que torna o projeto mais simples para fins didáticos.
- O jogo possui dois estados principais: **menu** e **playing**.
- O botão **Music** controla a trilha de fundo.
- Após a derrota, o jogo retorna ao menu inicial.

## Créditos

Projeto utilizado em contexto educacional para estudo de lógica de jogos, organização de assets e documentação de projeto.
