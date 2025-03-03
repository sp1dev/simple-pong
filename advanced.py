import pygame

# Initialize Pygame
pygame.init()

# Font that is used to render the text
font20 = pygame.font.Font('freesansbold.ttf', 20)

# RGB values of standard colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Basic parameters of the screen
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up the clock for managing the frame rate
clock = pygame.time.Clock()
FPS = 30

# Paddle parameters
paddle_width, paddle_height = 10, 100
paddle_speed = 10

# Ball parameters
ball_radius = 7
ball_speed = 7

# Initial positions of paddles and ball
paddle1_pos = [20, HEIGHT // 2 - paddle_height // 2]
paddle2_pos = [WIDTH - 30, HEIGHT // 2 - paddle_height // 2]
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_dir = [1, -1]

# Scores for both players
score1, score2 = 0, 0

# Function to draw a paddle
def draw_paddle(pos, color):
    pygame.draw.rect(screen, color, (*pos, paddle_width, paddle_height))

# Function to draw the ball
def draw_ball(pos, color):
    pygame.draw.circle(screen, color, pos, ball_radius)

# Function to display the scores in the middle of the screen
def display_scores(score1, score2, color):
    score_text = font20.render(f"{score1}   {score2}", True, color)
    text_rect = score_text.get_rect(center=(WIDTH // 2, 20))
    screen.blit(score_text, text_rect)

# Main game function
def main():
    global paddle1_pos, paddle2_pos, ball_pos, ball_dir, score1, score2
    running = True
    paddle1_y_change, paddle2_y_change = 0, 0

    while running:
        # Fill the screen with black color
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    paddle2_y_change = -paddle_speed
                if event.key == pygame.K_DOWN:
                    paddle2_y_change = paddle_speed
                if event.key == pygame.K_w:
                    paddle1_y_change = -paddle_speed
                if event.key == pygame.K_s:
                    paddle1_y_change = paddle_speed
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    paddle2_y_change = 0
                if event.key in (pygame.K_w, pygame.K_s):
                    paddle1_y_change = 0

        # Update paddle positions
        paddle1_pos[1] += paddle1_y_change
        paddle2_pos[1] += paddle2_y_change

        # Ensure paddles stay within the screen bounds
        paddle1_pos[1] = max(0, min(paddle1_pos[1], HEIGHT - paddle_height))
        paddle2_pos[1] = max(0, min(paddle2_pos[1], HEIGHT - paddle_height))

        # Update ball position
        ball_pos[0] += ball_speed * ball_dir[0]
        ball_pos[1] += ball_speed * ball_dir[1]

        # Ball collision with top and bottom walls
        if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT:
            ball_dir[1] *= -1

        # Ball collision with left and right walls (scoring)
        if ball_pos[0] <= 0:
            score2 += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_dir[0] *= -1
        elif ball_pos[0] >= WIDTH:
            score1 += 1
            ball_pos = [WIDTH // 2, HEIGHT // 2]
            ball_dir[0] *= -1

        # Create rectangles for collision detection
        paddle1_rect = pygame.Rect(*paddle1_pos, paddle_width, paddle_height)
        paddle2_rect = pygame.Rect(*paddle2_pos, paddle_width, paddle_height)
        ball_rect = pygame.Rect(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius, ball_radius * 2, ball_radius * 2)

        # Ball collision with paddles
        if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
            ball_dir[0] *= -1

        # Draw paddles and ball
        draw_paddle(paddle1_pos, GREEN)
        draw_paddle(paddle2_pos, GREEN)
        draw_ball(ball_pos, WHITE)

        # Display scores
        display_scores(score1, score2, WHITE)

        # Update the display
        pygame.display.update()
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

# Run the main game function
if __name__ == "__main__":
    main()
