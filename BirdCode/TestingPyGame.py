
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
player_size = 60
pipei = []
for i in range(1, 7):
    pipe1i = pygame.image.load(f"pipe_{i}tall.png").convert_alpha()
    pipes1i = pygame.transform.scale(pipe1i, (player_size, player_size))


original_image = pygame.image.load("Flappy_Bird_V3.png").convert_alpha()

player_image = pygame.transform.scale(original_image, (player_size, player_size))


image_2 = pygame.image.load("Flappy_Bird_Flap.png").convert_alpha()

player_image_2 = pygame.transform.scale(image_2, (player_size, player_size))

pipe1 = pygame.Rect(
    WIDTH // 50 // 2,
    HEIGHT // 2 - player_size // 2,
    500,
    50
)

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
jump_power = 2.5
i=1
dt = 0
bird_y = float(player.y) #makes float because player only holds int

image_use = player_image

while running:
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print ("jumping"+str(i))
            i=i+1
            dt = -jump_power
            image_use = player_image_2
    dt += gravity

    if dt >= -1.5:
        image_use = player_image

    if (player.y<0.001):
        dt=0.1
        print ("roof"+str(dt))

    print (str(dt))


    
    bird_y += dt

    player.y = round(bird_y)

    #print ("gravity:"+str(dt))

    # Keep player inside window
    player.clamp_ip(screen.get_rect())

    # Background
    screen.fill((30, 30, 40))

    screen.blit(image_use, player)

    # Draw Pipes



    # Draw player
    

    # Update screen
    pygame.display.flip()

    # 60 FPS
    clock.tick(tick)

pygame.quit()


