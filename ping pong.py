import pygame

pygame.init()

screen_width = 900
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ping Pong")

paddle_width = 10
paddle_height = 100
paddle_speed = 5

player1_paddle = pygame.Rect(50, (screen_height - paddle_height) / 2, paddle_width, paddle_height)
player2_paddle = pygame.Rect(screen_width - 50 - paddle_width, (screen_height - paddle_height) / 2, paddle_width, paddle_height)

ball_size = 10
ball_speed = 1

ball = pygame.Rect((screen_width - ball_size) / 2, (screen_height - ball_size) / 2, ball_size, ball_size)
ball_direction = [1, 1]

player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_paddle.top > 0:
        player1_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_s] and player1_paddle.bottom < screen_height:
        player1_paddle.move_ip(0, paddle_speed)
    if keys[pygame.K_UP] and player2_paddle.top > 0:
        player2_paddle.move_ip(0, -paddle_speed)
    if keys[pygame.K_DOWN] and player2_paddle.bottom < screen_height:
        player2_paddle.move_ip(0, paddle_speed)
    
    ball.move_ip(ball_speed * ball_direction[0], ball_speed * ball_direction[1])

    if ball.left < 0:
        player2_score += 1
        ball_direction[0] = 1
        ball.center = (screen_width / 2, screen_height / 2)
    if ball.right > screen_width:
        player1_score += 1
        ball_direction[0] = -1
        ball.center = (screen_width / 2, screen_height / 2)
    if ball.top < 0 or ball.bottom > screen_height:
        ball_direction[1] = -ball_direction[1]

    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_direction[0] = -ball_direction[0]

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), player1_paddle)
    pygame.draw.rect(screen, (255, 255, 255), player2_paddle)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    score_text = font.render(f"{player1_score} - {player2_score}", True, (255, 255, 255))
    screen.blit(score_text, ((screen_width - score_text.get_width()) / 2, 10))
    pygame.display.flip()

pygame.quit()
