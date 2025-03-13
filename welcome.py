import pygame
import time

def display_welcome_message(screen, font):
    # Define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    text_color = WHITE  # Change text color to white
    
    # Initialize alpha for fade-in effect
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill(WHITE)
    
    # Create text surfaces
    welcome_text = font.render("Welcome to Pacman!", True, text_color)
    start_text = font.render("Press ENTER to Start or Q to Quit", True, text_color)
    
    # Define rectangles for centering the text
    welcome_rect = welcome_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 100))
    start_rect = start_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 100))
    
    # Load and position the logo image
    try:
        logo_image = pygame.image.load('bg_images/bg.jpg')  # Replace with your image path
        logo_rect = logo_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 3))
    except pygame.error:
        logo_image = None
        print("Image could not be loaded. Please check the file path.")
    
    # Fill screen with black background
    screen.fill(BLACK)
    
    # Fade-in effect for the welcome message
    for alpha in range(0, 256, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        
        if logo_image:
            screen.blit(logo_image, logo_rect)
        screen.blit(welcome_text, welcome_rect)
        
        pygame.display.flip()
        pygame.time.delay(30)
    
    # Blinking effect for the "Press ENTER to Start" message
    blink = True
    blink_start = time.time()
    
    while time.time() - blink_start < 3:  # Blink for 3 seconds
        screen.fill(BLACK)  # Background color is black
        
        if logo_image:
            screen.blit(logo_image, logo_rect)
        screen.blit(welcome_text, welcome_rect)
        
        if blink:
            screen.blit(start_text, start_rect)
        
        blink = not blink
        pygame.display.flip()
        pygame.time.delay(500)
    
    # Ensure the start message stays visible
    screen.blit(start_text, start_rect)
    pygame.display.flip()


def wait_for_user_input():
    """Wait for the user to press Enter to start or Q to quit."""
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True  # User pressed Enter to start
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()  # User pressed Q to quit


def select_difficulty(screen, font):
    """Display difficulty selection options."""
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    
    # Create text surfaces for difficulty options
    easy_text = font.render("Press 1 for Easy", True, WHITE)
    medium_text = font.render("Press 2 for Medium", True, WHITE)
    hard_text = font.render("Press 3 for Hard", True, WHITE)
    
    # Define rectangles for centering the text
    easy_rect = easy_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 50))
    medium_rect = medium_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    hard_rect = hard_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 50))
    
    # Display difficulty options
    screen.fill(BLACK)
    screen.blit(easy_text, easy_rect)
    screen.blit(medium_text, medium_rect)
    screen.blit(hard_text, hard_rect)
    pygame.display.flip()
    
    # Wait for user to select difficulty
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return "Easy"
                elif event.key == pygame.K_2:
                    return "Medium"
                elif event.key == pygame.K_3:
                    return "Hard"


def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pacman Game")
    
    # Set up the font
    font = pygame.font.Font(None, 48)  # You can change the font size as needed
    
    # Display the welcome message
    display_welcome_message(screen, font)
    
    # Wait for user input to start
    if wait_for_user_input():
        # Select difficulty level
        difficulty = select_difficulty(screen, font)
        print(f"Selected difficulty: {difficulty}")  # Placeholder for starting the game logic with selected difficulty
    
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()
