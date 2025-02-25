import pygame, sys, random
from pygame.locals import *
pygame.init()

# Colours
BACKGROUND = (255, 255, 255)
ELEMENTCOLOUR = (100, 100, 100)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Pong')

# Game Element Variables
PADDLEINSET = 20
PADDLEWIDTH = 10
PADDLEHEIGHT = 60
BALLSIZE = 10
BALL_SPEED = 2  # Constant for ball speed

# The main function that controls the game
def main():
    looping = True

    # Initial positions and momentum
    leftPaddleY = 50
    rightPaddleY = 50
    ballX = WINDOW_WIDTH // 2
    ballY = WINDOW_HEIGHT // 2
    ballXMomentum = BALL_SPEED
    ballYMomentum = BALL_SPEED

    # The main game loop
    while looping:
        # Get inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pressed = pygame.key.get_pressed()
        if pressed[K_w]:
            leftPaddleY -= 5
        elif pressed[K_s]:
            leftPaddleY += 5
        if pressed[K_UP]:
            rightPaddleY -= 5
        elif pressed[K_DOWN]:
            rightPaddleY += 5

        # Check for paddle collisions with walls
        if leftPaddleY < 0:
            leftPaddleY = 0
        if leftPaddleY > WINDOW_HEIGHT - PADDLEHEIGHT:
            leftPaddleY = WINDOW_HEIGHT - PADDLEHEIGHT
        if rightPaddleY < 0:
            rightPaddleY = 0
        if rightPaddleY > WINDOW_HEIGHT - PADDLEHEIGHT:
            rightPaddleY = WINDOW_HEIGHT - PADDLEHEIGHT

        # Ball collision with top and bottom walls
        if ballY < BALLSIZE:
            ballYMomentum = BALL_SPEED
        if ballY > WINDOW_HEIGHT - BALLSIZE:
            ballYMomentum = -BALL_SPEED

        # Ball collision with left and right walls (scoring)
        if ballX <= BALLSIZE:
            ballX = WINDOW_WIDTH // 2
            ballY = WINDOW_HEIGHT // 2
            ballYMomentum = BALL_SPEED
            ballXMomentum = BALL_SPEED
        if ballX >= WINDOW_WIDTH - BALLSIZE:
            ballX = WINDOW_WIDTH // 2
            ballY = WINDOW_HEIGHT // 2
            ballYMomentum = BALL_SPEED
            ballXMomentum = -BALL_SPEED

        # Ball collision with paddles
        if ballX <= PADDLEINSET + PADDLEWIDTH and ballX > PADDLEINSET:
            if leftPaddleY < ballY and leftPaddleY + PADDLEHEIGHT > ballY:
                ballXMomentum = BALL_SPEED
        if ballX >= WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH and ballX < WINDOW_WIDTH - PADDLEINSET:
            if rightPaddleY < ballY and rightPaddleY + PADDLEHEIGHT > ballY:
                ballXMomentum = -BALL_SPEED

        # Update the paddles
        leftPaddleRect = pygame.Rect(PADDLEINSET, leftPaddleY, PADDLEWIDTH, PADDLEHEIGHT)
        rightPaddleRect = pygame.Rect(WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH, rightPaddleY, PADDLEWIDTH, PADDLEHEIGHT)

        # Update the ball
        ballX = ballX + ballXMomentum
        ballY = ballY + ballYMomentum

        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        # Draw line down the middle
        pygame.draw.line(WINDOW, ELEMENTCOLOUR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)

        # Draw paddles and ball
        pygame.draw.rect(WINDOW, ELEMENTCOLOUR, leftPaddleRect)
        pygame.draw.rect(WINDOW, ELEMENTCOLOUR, rightPaddleRect)
        pygame.draw.circle(WINDOW, ELEMENTCOLOUR, (int(ballX), int(ballY)), BALLSIZE)

        # Update the display
        pygame.display.update()
        fpsClock.tick(FPS)

# Run the main game function
main()