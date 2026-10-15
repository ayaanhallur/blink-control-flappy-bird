import pygame
import random

# Start Pygame
pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Game")

tick=120
speed=tick/48

# Clock
clock = pygame.time.Clock()

# Player
player_size = 30
player = pygame.Rect(
    WIDTH // 2 - player_size // 2,
    HEIGHT // 2 - player_size // 2,
    player_size,
    player_size
)
player_speed = speed

player_size = 30
player2 = pygame.Rect(
    WIDTH // 2 - player_size // 2,
    HEIGHT // 2 - player_size // 2,
    player_size,
    player_size
)

# Coin
coin_size = 15
coin = pygame.Rect(
    random.randint(0, WIDTH - coin_size),
    random.randint(0, HEIGHT - coin_size),
    coin_size,
    coin_size
)

# Score
score = 0
score2 = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True

while running:
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Keyboard
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.x -= player_speed

    if keys[pygame.K_RIGHT]:   
        player.x += player_speed

    if keys[pygame.K_UP]:
        player.y -= player_speed

    if keys[pygame.K_DOWN]:
        player.y += player_speed

    if keys[pygame.K_a]:
        player2.x -= player_speed

    if keys[pygame.K_d]:
        player2.x += player_speed

    if keys[pygame.K_w]:
        player2.y -= player_speed

    if keys[pygame.K_s]:
        player2.y += player_speed

    # Keep player inside window
    player.clamp_ip(screen.get_rect())

    player2.clamp_ip(screen.get_rect())

    # Collect coin
    if player.colliderect(coin):
        score += 1

        coin.x = random.randint(0, WIDTH - coin_size)
        coin.y = random.randint(0, HEIGHT - coin_size)

    if player2.colliderect(coin):
        score2 += 1

        coin.x = random.randint(0, WIDTH - coin_size)
        coin.y = random.randint(0, HEIGHT - coin_size)

    # Background
    screen.fill((30, 30, 40))

    # Draw player
    pygame.draw.rect(screen, (50, 150, 255), player)

    pygame.draw.rect(screen, (255, 17, 230), player2)

    # Draw coin
    pygame.draw.rect(screen, (255, 220, 50), coin)

    # Draw score
    score_text = font.render(f"Score: {score2}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (700, 10))

    # Update screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(tick)

pygame.quit()
