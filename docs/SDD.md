# SDD - Software Design Document - Snake Game - KodLand

![Tela de gameplay](images/gameplay_screen.png)

## 1. Objetivo do documento

Este documento descreve a estrutura técnica do projeto **Snake Game - KodLand**, detalhando organização de arquivos, fluxo de execução, estados do jogo, regras implementadas no código e responsabilidades das principais funções.

O objetivo é facilitar manutenção, reaproveitamento didático e futuras evoluções do jogo.

## 2. Stack técnica

- **Linguagem:** Python
- **Biblioteca principal:** Pygame Zero (PgZero)
- **Módulos utilizados no script:** `pgzrun` e `random`
- **Recursos externos:** imagens PNG, sons WAV e música MP3

## 3. Estrutura do projeto

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

## 4. Arquivo principal

Toda a lógica do jogo está concentrada em `main.py`. Esse arquivo responde por:

- definição do tamanho da janela;
- controle do estado atual do jogo;
- desenho do menu e da gameplay;
- atualização da cobra em tempo controlado;
- detecção de colisões;
- geração da maçã;
- entrada por teclado e mouse;
- acionamento de música e efeitos sonoros.

## 5. Arquitetura geral

A arquitetura do projeto é simples e baseada em **estado global + funções de ciclo do PgZero**.

### 5.1 Estados principais

O jogo utiliza o estado textual `game_state` para alternar entre:

- `menu`
- `playing`

Além disso, há flags auxiliares:

- `music_on`: controla música ligada/desligada;
- `dead`: evita repetição do som de derrota;
- `paused`: indica pausa durante a partida.

### 5.2 Entidades do jogo

As entidades principais são representadas por estruturas simples.

- **Cobra:** lista de tuplas `(x, y)` com segmentos em grade.
- **Maçã:** tupla `(x, y)` em grade.
- **Botões do menu:** dicionário com áreas clicáveis usando `Rect`.

## 6. Configurações base

O jogo define:

- `WIDTH = 640`
- `HEIGHT = 480`
- `TILE_SIZE = 20`

Com isso, a área jogável opera em uma grade lógica de:

- **32 colunas** (`640 / 20`)
- **24 linhas** (`480 / 20`)

## 7. Variáveis globais relevantes

### 7.1 Controle de jogo

- `game_state`
- `music_on`
- `dead`
- `paused`
- `score`

### 7.2 Cobra

- `snake`
- `direction`
- `new_direction`
- `growing`

### 7.3 Item coletável

- `apple`

### 7.4 Controle de atualização

- `frame_count`
- `frame_delay`

A atualização da cobra não ocorre a cada frame desenhado. O script usa `frame_delay = 6`, o que gera aproximadamente **10 atualizações por segundo** quando a aplicação opera a 60 FPS.

## 8. Fluxo de execução

### 8.1 Inicialização

Ao iniciar o script:

- a janela é configurada;
- a cobra recebe tamanho inicial de três segmentos;
- a maçã recebe posição inicial;
- o estado começa em `menu`.

### 8.2 Desenho

A função `draw()` atua como roteadora visual:

- chama `draw_menu()` se o estado for `menu`;
- chama `draw_game()` se o estado for `playing`.

### 8.3 Atualização

A função `update()` só movimenta a cobra quando:

- o estado é `playing`;
- o jogo não está pausado;
- o contador de frames alcança o atraso configurado.

### 8.4 Encerramento de rodada

Quando ocorre colisão, `game_over()`:

- toca o som de derrota;
- altera `game_state` para `menu`;
- marca `dead = True`.

## 9. Responsabilidade das funções

### `draw()`
Decide qual tela deve ser desenhada.

### `draw_menu()`
Renderiza o fundo do menu, o título e os botões. O botão de música muda de cor quando a trilha está desligada.

### `draw_game()`
Renderiza o fundo, a cobra, a maçã, a pontuação e a mensagem de pausa.

### `update()`
Controla a frequência de atualização da cobra com base no contador de frames.

### `update_snake()`
Executa a lógica central da partida:

- valida mudança de direção;
- calcula nova posição da cabeça;
- verifica colisões;
- atualiza a lista da cobra;
- trata coleta de maçã;
- aumenta pontuação;
- controla crescimento.

### `place_new_apple()`
Gera aleatoriamente uma nova posição para a maçã, garantindo que ela não apareça sobre a cobra.

### `game_over()`
Centraliza o comportamento de fim da rodada.

### `on_key_down(key)`
Processa entrada do teclado durante a gameplay:

- mudança de direção;
- pausa com espaço.

### `on_mouse_down(pos)`
Processa cliques no menu:

- iniciar partida;
- alternar música;
- sair da aplicação.

## 10. Lógica da cobra

A cobra é representada por uma lista ordenada de segmentos.

Exemplo inicial:

```python
snake = [(10, 10), (9, 10), (8, 10)]
```

- `snake[0]` representa a cabeça.
- Os demais itens representam corpo e cauda.

A cada atualização:

1. uma nova cabeça é criada na direção atual;
2. essa cabeça é inserida no início da lista;
3. se não houve coleta, o último segmento é removido;
4. se houve coleta, a remoção não acontece e a cobra cresce.

## 11. Controle de direção

A direção atual fica em `direction`, enquanto a próxima intenção do jogador fica em `new_direction`.

Antes de aplicar a mudança, o código verifica se a nova direção não é o oposto exato da direção atual. Isso evita reversão instantânea sobre o próprio eixo.

## 12. Regras de colisão

### 12.1 Bordas

A nova cabeça precisa permanecer dentro dos limites da grade.

Se `new_head` sair do intervalo válido, ocorre derrota.

### 12.2 Corpo

Se a nova cabeça coincidir com qualquer segmento existente da cobra, ocorre derrota.

## 13. Sistema de pontuação

A pontuação é armazenada em `score`.

Sempre que a cabeça coincide com a posição da maçã:

- `score += 1`
- toca `sounds.collect`
- `growing = True`
- uma nova maçã é gerada

## 14. Renderização dos sprites

O desenho da cobra é separado em três partes:

- **cabeça** com sprite direcional;
- **corpo** com sprite neutro repetido;
- **cauda** com sprite direcional.

A orientação é calculada comparando posições entre segmentos vizinhos.

### Sprites utilizados

- `snake_head_up`
- `snake_head_down`
- `snake_head_left`
- `snake_head_right`
- `snake`
- `snake_tail_up`
- `snake_tail_down`
- `snake_tail_left`
- `snake_tail_right`
- `apple`
- `background`

## 15. Áudio

### Música

A música de fundo é controlada pelo objeto `music` do PgZero.

- ao iniciar partida, a música toca se `music_on` estiver verdadeiro;
- no menu, o botão **Music** alterna entre tocar e parar.

### Efeitos

- `sounds.collect.play()` ao coletar maçã;
- `sounds.gameover.play()` ao perder.

## 16. Interface e usabilidade

O menu foi implementado com botões simples baseados em `Rect`, o que torna a navegação direta.

Na gameplay:

- a pontuação fica em posição de destaque no canto superior esquerdo;
- o texto `PAUSED` aparece centralizado quando a partida está pausada.

## 17. Dependências e execução

### Instalação

```bash
pip install pgzero
```

### Execução

```bash
pgzrun main.py
```

## 18. Observações técnicas identificadas na análise

### 18.1 Organização

A organização do projeto está adequada para um jogo pequeno e didático. Os assets estão corretamente separados por tipo.

### 18.2 Acoplamento

A lógica está concentrada em um único arquivo. Isso facilita leitura inicial, mas aumenta o acoplamento entre estado, renderização, entrada e regras de jogo.

### 18.3 Estado de game over

O fluxo atual retorna diretamente ao menu após derrota. Não existe uma tela intermediária de resultado ou reinício.

### 18.4 Identificação visual do título

O repositório e a documentação usam a identidade **KodLand**, enquanto o script pode conter uma string de título no menu que merece padronização conforme a versão final desejada do projeto.

## 19. Melhorias técnicas sugeridas

- separar lógica de jogo, interface e configuração em módulos diferentes;
- criar uma função de reinício dedicada;
- adicionar tela de game over com pontuação final;
- registrar recorde local em arquivo simples;
- substituir parte do estado global por estrutura orientada a objeto ou por camadas de sistema;
- adicionar testes básicos para funções puras, como geração de maçã e validação de colisão.

## 20. Conclusão técnica

O projeto é consistente para fins educacionais, apresenta fluxo funcional completo e utiliza corretamente recursos centrais do PgZero para um jogo arcade simples. A base atual é suficiente para ensino, demonstração e expansão incremental do sistema.

