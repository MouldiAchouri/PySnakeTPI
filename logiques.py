from variables import *

class Snake:
    # Classe qui gère l'état et les mouvements
    def __init__(self):
        self.reset() # recommence de zéro sans avoir à recréer tout l'objet

    def reset(self):
        # position de départ calcuée pour être alignée sur la grille
        x = (WIDTH // 2 // CELL_SIZE) * CELL_SIZE
        y = (HEIGHT // 2 // CELL_SIZE) * CELL_SIZE

        # position de la tete et du corps du serpent
        self.segments = [[x, y], [x - CELL_SIZE, y]]
        self.direction = RIGHT # direction de départ
        self.score = 0 # score au lancement du jeu

    def move(self):
        head_x, head_y = self.segments[0] # verification de la tete du serpent
        # prédiction du mouvement. Elle vérifie si la prochaine case est sure.
        if self.direction == UP: head_y -= CELL_SIZE
        elif self.direction == DOWN: head_y += CELL_SIZE
        elif self.direction == LEFT: head_x -= CELL_SIZE
        elif self.direction == RIGHT: head_x += CELL_SIZE
        return [head_x, head_y]

    def grow(self, new_head):
        # ajoute une nouvelle tete au serpent
        self.segments.insert(0, new_head)
        self.score += 1

    def crawl(self, new_head):
        # lorsqu'il avance, il ajoute une nouvelle tete puis il supprime un corps
        self.segments.insert(0, new_head)
        self.segments.pop()

    def check_collision(self, head):
        # vérifie la collision (corps, mur)
        x, y = head
        return (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or head in self.segments)