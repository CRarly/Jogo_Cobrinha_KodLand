# SDD - Sound Design Document

![Tela de gameplay](images/gameplay_screen.png)

## 1. Objetivo do documento

Este documento descreve o **design sonoro** do projeto **Snake Game - KodLand**, detalhando a função da música e dos efeitos sonoros, os pontos de disparo no jogo, o papel de cada asset de áudio e diretrizes para evolução futura da camada sonora.

## 2. Visão geral da proposta sonora

O jogo possui uma proposta sonora simples e funcional, coerente com sua natureza arcade e didática. O áudio foi pensado para cumprir três papéis principais:

- reforçar a ambientação da partida;
- oferecer feedback imediato às ações do jogador;
- sinalizar claramente eventos importantes do jogo.

Como o projeto tem escopo enxuto, a trilha sonora e os efeitos são poucos, mas cumprem bem a função de apoiar a experiência sem poluir a partida.

## 3. Objetivos do áudio

O design sonoro busca:

- criar uma base de ambientação contínua durante a gameplay;
- reforçar a sensação de recompensa ao coletar a maçã;
- comunicar o encerramento da rodada de forma clara;
- manter uma implementação simples para fins educacionais.

## 4. Inventário de assets sonoros

## 4.1 Música

| Arquivo | Tipo | Função |
|---|---|---|
| `music/music.mp3` | Trilha de fundo | Ambientação principal da partida |

## 4.2 Efeitos sonoros

| Arquivo | Tipo | Função |
|---|---|---|
| `sounds/collect.wav` | SFX | Feedback de coleta da maçã |
| `sounds/gameover.wav` | SFX | Feedback de derrota / fim da rodada |

## 5. Papel de cada elemento sonoro

### 5.1 Música de fundo

A música principal acompanha a partida quando o jogador inicia o jogo e a opção de música está ativa. Sua função é sustentar a ambientação e evitar sensação de vazio durante a gameplay.

Além disso, o botão **Music** no menu permite alternar entre música ligada e desligada, oferecendo ao jogador um controle simples sobre a trilha.

### 5.2 Som de coleta

O som `collect.wav` é disparado quando a cabeça da cobra toca a maçã. Ele atua como um feedback positivo e imediato, reforçando a ação de sucesso do jogador.

Esse tipo de resposta sonora é importante porque confirma a coleta sem exigir que o jogador desvie o olhar da movimentação principal.

### 5.3 Som de game over

O som `gameover.wav` é reproduzido no momento em que ocorre colisão fatal. Sua função é marcar a transição brusca entre o estado de jogo e o retorno ao menu, deixando evidente que a rodada foi encerrada.

## 6. Eventos de disparo no código

Com base no script `main.py`, os eventos sonoros estão organizados da seguinte forma:

| Evento | Ação sonora |
|---|---|
| Clique em **Start** com música ativada | `music.play("music")` |
| Clique no botão **Music** para ativar | `music.play("music")` |
| Clique no botão **Music** para desativar | `music.stop()` |
| Cobra coleta a maçã | `sounds.collect.play()` |
| Cobra perde a partida | `sounds.gameover.play()` |

## 7. Fluxo sonoro da experiência

O fluxo sonoro do jogo pode ser resumido assim:

1. o jogador entra no menu em silêncio ou com música já ativada;
2. ao iniciar a partida, a trilha de fundo pode começar;
3. durante o jogo, cada coleta gera um efeito sonoro curto;
4. ao perder, o som de game over marca o fim da rodada;
5. o jogo retorna ao menu.

Esse fluxo é simples, mas suficiente para apoiar a leitura do estado atual da partida.

## 8. Função do som na jogabilidade

Mesmo com poucos elementos, o áudio contribui diretamente para a usabilidade:

- ajuda a confirmar ações do jogador;
- melhora a percepção de resposta do sistema;
- diferencia momentos positivos e negativos;
- torna a experiência menos seca e mais envolvente.

## 9. Diretrizes de mixagem

Como o projeto utiliza poucos sons simultâneos, a mixagem é naturalmente simples. Ainda assim, algumas diretrizes são recomendadas:

- a trilha de fundo deve permanecer abaixo do volume dos efeitos de feedback;
- `collect.wav` deve ser curto e perceptível;
- `gameover.wav` deve se destacar da trilha, marcando claramente o fim da rodada;
- evitar sons excessivamente longos para não sobrepor ações rápidas da gameplay.

## 10. Coerência estética sonora

O jogo possui proposta visual simples e arcade. Por isso, o áudio ideal segue a mesma direção:

- sons diretos;
- respostas rápidas;
- trilha contínua e discreta;
- baixo número de camadas sonoras.

Essa coerência favorece a clareza da experiência e se alinha ao escopo do projeto.

## 11. Limitações atuais

No estado atual, o projeto ainda não possui:

- variação de trilha por estado do jogo;
- efeitos para navegação no menu;
- som específico de pausa;
- camadas adicionais de ambientação;
- sistema de ajuste fino de volume por categoria.

## 12. Melhorias futuras sugeridas

- adicionar efeito sonoro para clique de botão;
- incluir som específico de pausa e retomada;
- separar volume de música e efeitos;
- criar uma trilha exclusiva para menu;
- adicionar variação sonora conforme aumento da dificuldade;
- trabalhar transições mais suaves entre menu e gameplay.

## 13. Resumo

O design sonoro de **Snake Game - KodLand** é pequeno em escopo, mas bem alinhado ao projeto. A trilha sustenta a ambientação, o som de coleta reforça recompensa e o som de game over comunica falha com clareza. Para um jogo didático e introdutório, a camada sonora atual é suficiente, organizada e facilmente expansível.
