import pygame

WIDTH, HEIGHT = 600, 600 # Dimensions de la fenêtre
CELL_SIZE = 30 # Taille d'une case de la grille
FPS = 60 # Taux de rafraichissement

# Couleurs
COLOR_BG = (173, 255, 47) # vert clair
COLOR_GRID = (154, 232, 49) # vert plus foncé
COLOR_SNAKE_HEAD = (100, 149, 237) # tête du serpent
COLOR_SNAKE_BODY = (65, 105, 225) # corps du serpent
COLOR_APPLE = (255, 69, 0) # pomme

# Directions
UP = pygame.K_UP
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT
RIGHT = pygame.K_RIGHT