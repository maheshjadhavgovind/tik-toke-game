import pygame
import random
import time

# Initialize pygame
pygame.init()

# Game settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("TikTok Reaction Game")

# Fonts
font = pygame.font.SysFont(None, 75)

# Timer variables
start_time = 0
reaction_time = 0
game_started = False
prompt_appeared = False

# Function to display text on screen
def display_text(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Start the game when spacebar is pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not game_started:
        game_started = True
        prompt_appeared = False
        start_time = time.time() + random.uniform(2, 5)  # Random delay

    # Display waiting message
    if game_started and not prompt_appeared:
        display_text("Wait for it...", font, BLACK, 200, 250)

    # Show the prompt after the delay
    if game_started and not prompt_appeared and time.time() >= start_time:
        prompt_appeared = True
        reaction_time = time.time()  # Record when prompt appears

    # Display prompt
    if prompt_appeared:
        display_text("PRESS NOW!", font, RED, 200, 250)
        if keys[pygame.K_SPACE]:
            reaction_time = time.time() - reaction_time
            display_text(f"Reaction Time: {reaction_time:.3f} sec", font, GREEN, 50, 400)
            pygame.display.update()
            time.sleep(3)
            game_started = False  # Reset game

    pygame.display.update()

# Quit pygame
pygame.quit()
