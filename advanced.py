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

# Score Variables
SCOREFONT = pygame.font.SysFont("Arial", 100)
SCOREY = 25
PLAYERSCOREX = 300
BOTSCOREX = 465

def init_game():
    # Initial position of paddles and ball
    leftPaddleY = 50
    rightPaddleY = 50
    ballX = WINDOW_WIDTH // 2
    ballY = WINDOW_HEIGHT // 2
    ballXMomentum = BALL_SPEED
    ballYMomentum = BALL_SPEED
    player1Score = 0
    player2Score = 0
    return leftPaddleY, rightPaddleY, ballX, ballY, ballXMomentum, ballYMomentum, player1Score, player2Score

def handle_input(leftPaddleY, rightPaddleY):
    pressed = pygame.key.get_pressed()
    if pressed[K_w]:
        leftPaddleY -= 5
    elif pressed[K_s]:
        leftPaddleY += 5
    if pressed[K_UP]:
        rightPaddleY -= 5
    elif pressed[K_DOWN]:
        rightPaddleY += 5
    return leftPaddleY, rightPaddleY

def update_game(ballX, ballY, ballXMomentum, ballYMomentum, leftPaddleY, rightPaddleY, player1Score, player2Score):
    # Check for paddle collisions with walls
    leftPaddleY = max(min(leftPaddleY, WINDOW_HEIGHT - PADDLEHEIGHT), 0)
    rightPaddleY = max(min(rightPaddleY, WINDOW_HEIGHT - PADDLEHEIGHT), 0)

    # Ball collision with walls and scoring
    if ballY <= BALLSIZE or ballY >= WINDOW_HEIGHT - BALLSIZE:
        ballYMomentum *= -1
    if ballX <= BALLSIZE:
        ballX, ballY = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        player2Score += 1
    elif ballX >= WINDOW_WIDTH - BALLSIZE:
        ballX, ballY = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
        player1Score += 1

    # Ball collision with paddles
    if (ballX <= PADDLEINSET + PADDLEWIDTH and leftPaddleY < ballY < leftPaddleY + PADDLEHEIGHT) or \
       (ballX >= WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH and rightPaddleY < ballY < rightPaddleY + PADDLEHEIGHT):
        ballXMomentum *= -1

    # Update ball position
    ballX += ballXMomentum
    ballY += ballYMomentum
    return ballX, ballY, leftPaddleY, rightPaddleY, player1Score, player2Score

def draw_game(ballX, ballY, leftPaddleY, rightPaddleY, player1Score, player2Score):
    WINDOW.fill(BACKGROUND)
    pygame.draw.line(WINDOW, ELEMENTCOLOR, (WINDOW_WIDTH // 2, 0), (WINDOW_WIDTH // 2, WINDOW_HEIGHT), 2)
    pygame.draw.rect(WINDOW, ELEMENTCOLOR, pygame.Rect(PADDLEINSET, leftPaddleY, PADDLEWIDTH, PADDLEHEIGHT))
    pygame.draw.rect(WINDOW, ELEMENTCOLOR, pygame.Rect(WINDOW_WIDTH - PADDLEINSET - PADDLEWIDTH, rightPaddleY, PADDLEWIDTH, PADDLEHEIGHT))
    pygame.draw.circle(WINDOW, ELEMENTCOLOR, (int(ballX), int(ballY)), BALLSIZE)
    player1ScoreText = SCOREFONT.render(str(player1Score), False, ELEMENTCOLOR)
    player2ScoreText = SCOREFONT.render(str(player2Score), False, ELEMENTCOLOR)
    WINDOW.blit(player1ScoreText, (PLAYERSCOREX, SCOREY))
    WINDOW.blit(player2ScoreText, (BOTSCOREX, SCOREY))
    pygame.display.update()

def main():
    leftPaddleY, rightPaddleY, ballX, ballY, ballXMomentum, ballYMomentum, player1Score, player2Score = init_game()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        leftPaddleY, rightPaddleY = handle_input(leftPaddleY, rightPaddleY)
        ballX, ballY, leftPaddleY, rightPaddleY, player1Score, player2Score = update_game(ballX, ballY, ballXMomentum, ballYMomentum, leftPaddleY, rightPaddleY, player1Score, player2Score)
        draw_game(ballX, ballY, leftPaddleY, rightPaddleY, player1Score, player2Score)
        fpsClock.tick(FPS)

if __name__ == "__main__":
    main()
