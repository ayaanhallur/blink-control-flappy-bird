
import pygame

# Start Pygame
pygame.init()

# Window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My First Pygame Game")

tick=180
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


# Game loop
running = True


#stats
gravity = 0.035
jump_power = 2
i=1
dt = 0
bird_y = float(player.y) #makes float because player only holds int

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print ("jumping"+str(i))
            i=i+1
            dt = -jump_power
    #print ("Height:" +str(player.y))

    if (dt<3 and player.y<HEIGHT-player_size):
        dt += gravity
        #print ("falling"+str(dt))


    if (player.y>=HEIGHT-player_size):
        dt=0
        print ("grounded"+str(dt))

    #print ("falling"+str(dt))

    bird_y += dt

    player.y = round(bird_y)

    #print ("gravity:"+str(dt))

    # Keep player inside window
    player.clamp_ip(screen.get_rect())

    # Background
    screen.fill((30, 30, 40))

    # Draw player
    pygame.draw.rect(screen, (50, 150, 255), player)

    # Update screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(tick)

pygame.quit()




