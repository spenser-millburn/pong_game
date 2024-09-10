import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Ball dimensions
BALL_WIDTH = 20
BALL_HEIGHT = 20

# Paddle dimensions
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100

# Speeds
BALL_SPEED_X = 5
BALL_SPEED_Y = 5
PADDLE_SPEED = 10

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_WIDTH // 2, SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2, BALL_WIDTH, BALL_HEIGHT)
        self.speed_x = BALL_SPEED_X * random.choice((1, -1))
        self.speed_y = BALL_SPEED_Y * random.choice((1, -1))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self):
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1

    def reset(self):
        self.rect.x = SCREEN_WIDTH // 2 - BALL_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2 - BALL_HEIGHT // 2
        self.speed_x *= random.choice((1, -1))
        self.speed_y *= random.choice((1, -1))

# Paddle class
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.speed = 0

    def move(self):
        self.rect.y += self.speed
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

# Create ball and paddles
ball = Ball()
player_paddle = Paddle(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)
opponent_paddle = Paddle(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_paddle.speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                player_paddle.speed = PADDLE_SPEED
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_paddle.speed = 0

    # Move paddles and ball
    player_paddle.move()
    opponent_paddle.move()
    ball.move()

    # Ball collision with paddles
    if ball.rect.colliderect(player_paddle.rect) or ball.rect.colliderect(opponent_paddle.rect):
        ball.speed_x *= -1

    # Ball collision with walls
    ball.bounce()

    # Opponent AI
    if opponent_paddle.rect.centery < ball.rect.centery:
        opponent_paddle.speed = PADDLE_SPEED
    else:
        opponent_paddle.speed = -PADDLE_SPEED

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, player_paddle.rect)
    pygame.draw.rect(screen, WHITE, opponent_paddle.rect)
    pygame.draw.ellipse(screen, WHITE, ball.rect)
    pygame.draw.aaline(screen, WHITE, (SCREEN_WIDTH // 2, 0), (SCREEN_WIDTH // 2, SCREEN_HEIGHT))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
