import pgzrun
import random

# 🟩 Tamanho da janela
WIDTH = 640
HEIGHT = 480

# 🟩 Tamanho dos blocos
TILE_SIZE = 20

# Estado do jogo
game_state = "menu"
music_on = True
dead = False
paused = False

# 🟩 Cobra
snake = [(10, 10), (9, 10), (8, 10)]
direction = (1, 0)
new_direction = direction
growing = False

# 🟩 Maçã
apple = (15, 10)

# 🟩 Pontuação
score = 0

# 🟩 Botões do menu (visíveis no menu apenas)
menu_buttons = {
    "start": Rect((220, 150), (200, 50)),
    "music": Rect((220, 220), (200, 50)),
    "exit": Rect((220, 290), (200, 50))
}

def draw():
    screen.clear()
    if game_state == "menu":
        draw_menu()
    elif game_state == "playing":
        draw_game()

def draw_menu():
    screen.fill((50, 100, 150))
    screen.draw.text("SNAKE GAME - KODLAND", center=(WIDTH // 2, 80), fontsize=48, color="white")
    for name, rect in menu_buttons.items():
        if name == "music":
            cor = "darkgreen" if music_on else "gray"
        else:
            cor = "darkgreen"
        screen.draw.filled_rect(rect, cor)
        screen.draw.text(name.capitalize(), center=rect.center, fontsize=32, color="white")

def draw_game():
    screen.blit("background", (0, 0))

    # Cabeça
    head = snake[0]
    next_seg = snake[1]
    dx = head[0] - next_seg[0]
    dy = head[1] - next_seg[1]

    if dx == 1:
        head_dir = "right"
    elif dx == -1:
        head_dir = "left"
    elif dy == 1:
        head_dir = "down"
    else:
        head_dir = "up"

    screen.blit(f"snake_head_{head_dir}", (head[0]*TILE_SIZE, head[1]*TILE_SIZE))

    # Corpo
    for segment in snake[1:-1]:
        screen.blit("snake", (segment[0]*TILE_SIZE, segment[1]*TILE_SIZE))

    # Cauda
    if len(snake) > 1:
        tail = snake[-1]
        before_tail = snake[-2]
        dx = tail[0] - before_tail[0]
        dy = tail[1] - before_tail[1]

        if dx == 1:
            tail_dir = "right"
        elif dx == -1:
            tail_dir = "left"
        elif dy == 1:
            tail_dir = "down"
        else:
            tail_dir = "up"

        screen.blit(f"snake_tail_{tail_dir}", (tail[0]*TILE_SIZE, tail[1]*TILE_SIZE))

    # Maçã
    screen.blit("apple", (apple[0]*TILE_SIZE, apple[1]*TILE_SIZE))

    # Pontuação
    screen.draw.text(f"Score: {score}", topleft=(10, 10), fontsize=30, color="white")

    # Pausado
    if paused:
        screen.draw.text("PAUSED", center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color="white")


frame_count = 0
frame_delay = 6  # 60 FPS / 6 = 10 atualizações por segundo

def update():
    global frame_count
    if game_state != "playing" or paused:
        return
    frame_count += 1
    if frame_count >= frame_delay:
        update_snake()
        frame_count = 0

def update_snake():
    global snake, apple, growing, score, game_state, direction

    if new_direction != (-direction[0], -direction[1]):
        direction = new_direction

    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)

    # Colisão com bordas
    if not (0 <= new_head[0] < WIDTH // TILE_SIZE) or not (0 <= new_head[1] < HEIGHT // TILE_SIZE):
        game_over()
        return

    # Colisão com o corpo
    if new_head in snake:
        game_over()
        return

    snake = [new_head] + snake

    if new_head == apple:
        sounds.collect.play()
        growing = True
        score += 1
        place_new_apple()

    if not growing:
        snake.pop()
    else:
        growing = False

def place_new_apple():
    global apple
    while True:
        new_pos = (random.randint(0, (WIDTH // TILE_SIZE) - 1),
                   random.randint(0, (HEIGHT // TILE_SIZE) - 1))
        if new_pos not in snake:
            apple = new_pos
            break

def game_over():
    global game_state, dead
    if not dead:
        sounds.gameover.play()
        game_state = "menu"
        dead = True

def on_key_down(key):
    global new_direction, paused
    if game_state == "playing":
        if key == keys.UP:
            new_direction = (0, -1)
        elif key == keys.DOWN:
            new_direction = (0, 1)
        elif key == keys.LEFT:
            new_direction = (-1, 0)
        elif key == keys.RIGHT:
            new_direction = (1, 0)
        elif key == keys.SPACE:
            paused = not paused  # toggle pausa

def on_mouse_down(pos):
    global game_state, music_on, snake, direction, new_direction, score, dead

    if game_state != "menu":
        return

    if menu_buttons["start"].collidepoint(pos):
        dead = False
        game_state = "playing"
        snake[:] = [(10, 10), (9, 10), (8, 10)]
        direction = (1, 0)
        new_direction = direction
        place_new_apple()
        score = 0
        if music_on:
            music.play("music")
    elif menu_buttons["music"].collidepoint(pos):
        music_on = not music_on
        if music_on:
            music.play("music")
        else:
            music.stop()
    elif menu_buttons["exit"].collidepoint(pos):
        exit()

pgzrun.go()
