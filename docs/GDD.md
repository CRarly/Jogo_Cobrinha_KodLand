# GDD - Game Design Document

![Tela de menu](images/menu_screen.png)

## 1. Visão geral

**Snake Game - KodLand** é um jogo 2D inspirado no clássico Snake. O jogador controla uma cobra em uma área fechada, coleta maçãs e busca sobreviver o maior tempo possível sem colidir com as bordas ou com o próprio corpo.

A proposta do projeto é combinar uma mecânica clássica, fácil de compreender, com uma estrutura enxuta e didática para estudo de desenvolvimento de jogos com Python.

## 2. Conceito do jogo

O jogo segue um loop simples e direto:

1. o jogador entra no menu inicial;
2. inicia a partida;
3. movimenta a cobra pela tela;
4. coleta maçãs;
5. aumenta a pontuação e o tamanho da cobra;
6. enfrenta dificuldade crescente;
7. perde ao colidir com a parede ou com o próprio corpo.

## 3. Objetivo do jogador

O objetivo é alcançar a maior pontuação possível, mantendo a cobra viva por mais tempo e coletando o máximo de maçãs.

## 4. Público-alvo

- estudantes iniciantes em programação de jogos;
- pessoas aprendendo Python e Pygame Zero;
- jogadores casuais familiarizados com o gênero arcade.

## 5. Gênero e plataforma

- **Gênero:** Arcade / Casual
- **Formato:** 2D em grade
- **Plataforma:** Desktop
- **Biblioteca:** Pygame Zero

## 6. Mecânicas principais

### 6.1 Movimentação

A cobra se move continuamente em uma grade, com controle por setas direcionais.

### 6.2 Coleta

Ao tocar a maçã, o item é coletado, a pontuação aumenta e uma nova maçã é posicionada em local válido.

### 6.3 Crescimento

Cada maçã coletada faz a cobra crescer, elevando a complexidade da movimentação.

### 6.4 Colisão

A partida termina quando a cobra colide com:

- as bordas da tela;
- o próprio corpo.

### 6.5 Pausa

A tecla de espaço permite pausar e retomar a partida.

## 7. Controles

- **Seta para cima:** mover para cima
- **Seta para baixo:** mover para baixo
- **Seta para esquerda:** mover para a esquerda
- **Seta para direita:** mover para a direita
- **Espaço:** pausar ou continuar
- **Mouse:** clicar nos botões do menu

## 8. Interface

### 8.1 Menu principal

O menu apresenta:

- título do jogo;
- botão **Start**;
- botão **Music**;
- botão **Exit**.

### 8.2 Gameplay

Durante a partida, a interface mostra:

- fundo do cenário;
- cobra com cabeça, corpo e cauda;
- maçã como item coletável;
- pontuação no canto superior esquerdo;
- indicação textual de pausa.

## 9. Progressão e desafio

A dificuldade cresce de forma natural. No início, a cobra possui poucos segmentos e há maior liberdade de movimentação. Conforme o jogador coleta maçãs, o tamanho da cobra aumenta e o espaço seguro diminui, tornando mais difícil evitar colisões.

## 10. Condições de derrota e vitória

### Derrota

A derrota ocorre quando a cabeça da cobra toca a borda da tela ou qualquer parte do próprio corpo.

### Vitória

Não há uma condição final de vitória. O jogo é baseado em **superação de pontuação**.

## 11. Estilo visual

O projeto utiliza uma apresentação visual simples e funcional:

- plano de fundo texturizado;
- sprites próprios para cabeça, corpo e cauda;
- maçã destacada visualmente;
- HUD minimalista.

## 12. Áudio no design do jogo

O áudio atua como reforço da experiência:

- trilha de fundo para ambientação;
- som de coleta como recompensa imediata;
- som de game over como sinalização de fim da rodada.

## 13. Escopo atual

### Implementado

- menu jogável;
- sistema de música;
- gameplay funcional;
- pontuação;
- pausa;
- colisões;
- efeitos sonoros.

### Não implementado

- tela exclusiva de game over;
- sistema de recordes;
- níveis de dificuldade;
- efeitos visuais avançados;
- suporte mobile.

## 14. Melhorias futuras

- adicionar tela de game over com opção de reinício;
- criar sistema de recorde local;
- aumentar a velocidade ao longo da partida;
- incluir feedback visual para botões;
- adicionar variações de cenário e trilha.

## 15. Captura de gameplay

![Tela de gameplay](images/gameplay_screen.png)

## 16. Resumo

O projeto é compacto, funcional e adequado para uso didático. Seu valor está na clareza das mecânicas, na facilidade de compreensão do fluxo de jogo e na possibilidade de expansão futura.
