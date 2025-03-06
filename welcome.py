import pygame
import time

def display_welcome_message(screen, font):
    # Define colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    text_color = black
    
    # Initialize alpha for fade-in effect
    alpha = 0
    fade_surface = pygame.Surface(screen.get_size())
    fade_surface.fill(white)
    
    welcome_text = font.render("Welcome to Pacman!", True, text_color)
    start_text = font.render("Press ENTER to Start or Q to Quit", True, text_color)
    
    welcome_rect = welcome_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 30))
    start_rect = start_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 30))
    
    screen.fill(white)
    
    # Fade-in effect for the welcome message
    for alpha in range(0, 256, 5):
        fade_surface.set_alpha(alpha)
        screen.blit(fade_surface, (0, 0))
        screen.blit(welcome_text, welcome_rect)
        pygame.display.flip()
        pygame.time.delay(30)
    
    # Blinking effect for "Press ENTER to Start" message
    blink = True
    blink_start = time.time()
    
    while time.time() - blink_start < 3:  # Blink for 3 seconds
        screen.fill(white)
        screen.blit(welcome_text, welcome_rect)
        
        if blink:
            screen.blit(start_text, start_rect)
        blink = not blink
        pygame.display.flip()
        pygame.time.delay(500)
    
    screen.blit(start_text, start_rect)
    pygame.display.flip()

def wait_for_user_input():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
