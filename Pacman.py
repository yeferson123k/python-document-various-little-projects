import pygame

pygame.init()

screen_width = 700
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Pacman")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont(None, 25)

clock = pygame.time.Clock()

pacman_x = 50
pacman_y = 50
pacman_size = 20

speed = 5

pallet_list = []
pallet_size = 5

# Create the pallets
for i in range(0, screen_width, 20):
    for j in range(0, screen_height, 20):
        pallet_list.append(pygame.Rect(i, j, pallet_size, pallet_size))

score = 0

# Defining the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= speed
    if keys[pygame.K_RIGHT]:
        pacman_x += speed
    if keys[pygame.K_UP]:
        pacman_y -= speed
    if keys[pygame.K_DOWN]:
        pacman_y += speed

    # Keeping the pacman on the screen
    if pacman_x < 0:
        pacman_x = 0
    elif pacman_x > screen_width - pacman_size:
        pacman_x = screen_width - pacman_size
    if pacman_y < 0:
        pacman_y = 0
    elif pacman_y > screen_height - pacman_size:
        pacman_y = screen_height - pacman_size

    # Check for pallet collisions
    for pallet in pallet_list:
        if pallet.colliderect(pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)):
            pallet_list.remove(pallet)
            score += 1

    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (pacman_x + pacman_size // 2, pacman_y + pacman_size // 2), pacman_size // 2)
    for pallet in pallet_list:
        pygame.draw.rect(screen, WHITE, pallet)
    score_text = font.render("Score: " + str(score), True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()