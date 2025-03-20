import pygame, sys, random
from pygame.locals import *
pygame.init()

# Colors
BACKGROUND = (255, 255, 255)
ELEMENTCOLOR = (100, 100, 100)

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
BALL_SPEED = 3

# Initial position of paddles
leftPaddleY = 50
rightPaddleY = 50
# Initial position of ball
ballX = WINDOW_WIDTH // 2
ballY = WINDOW_HEIGHT // 2
ballXMomentum = BALL_SPEED
ballYMomentum = BALL_SPEED

# Score Variables
SCOREFONT = pygame.font.SysFont("Ariel", 100)
SCOREY = 25
PLAYER1SCOREX = 300
PLAYER2SCOREX = 465
player1Score = 0
player2Score = 0

# The main game loop
looping = True
while looping:
    # Handle user clicking X to close window
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # get_pressed returns the keys on the keyboard
    pressed = pygame.key.get_pressed()
    # Update the paddle positions based on keyboard input
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
        player2Score += 1
    if ballX >= WINDOW_WIDTH - BALLSIZE:
        ballX = WINDOW_WIDTH // 2
        ballY = WINDOW_HEIGHT // 2
        ballYMomentum = BALL_SPEED
        ballXMomentum = -BALL_SPEED
        player1Score += 1

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
    pygame.draw.line(WINDOW, ELEMENTCOLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)

    # Draw paddles and ball
    pygame.draw.rect(WINDOW, ELEMENTCOLOR, leftPaddleRect)
    pygame.draw.rect(WINDOW, ELEMENTCOLOR, rightPaddleRect)
    pygame.draw.circle(WINDOW, ELEMENTCOLOR, (int(ballX), int(ballY)), BALLSIZE)

    # Show Score
    player1ScoreText = SCOREFONT.render(str(player1Score), False, ELEMENTCOLOR)
    player2ScoreText = SCOREFONT.render(str(player2Score), False, ELEMENTCOLOR)
    WINDOW.blit(player1ScoreText, (PLAYER1SCOREX, SCOREY))
    WINDOW.blit(player2ScoreText, (PLAYER2SCOREX, SCOREY))

    # Update the display
    pygame.display.update()
    fpsClock.tick(FPS)