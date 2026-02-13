import pygame
import sys
import random
from variables import *
from snake import Snake

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('PySnake Pro')
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.apple = self.spawn_apple()

    def spawn_apple(self):
        while True:
            pos = [random.randint(0, (WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
                   random.randint(0, (HEIGHT // GRID_SIZE) - 1) * GRID_SIZE]
            if pos not in self.snake.positions:
                return pos

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snake.direction != pygame.K_DOWN:
                    self.snake.direction = event.key
                elif event.key == pygame.K_DOWN and self.snake.direction != pygame.K_UP:
                    self.snake.direction = event.key
                elif event.key == pygame.K_LEFT and self.snake.direction != pygame.K_RIGHT:
                    self.snake.direction = event.key
                elif event.key == pygame.K_RIGHT and self.snake.direction != pygame.K_LEFT:
                    self.snake.direction = event.key

    def run(self):
        while True:
            self.handle_events()
            if not self.snake.update():
                self.snake.reset()
                self.apple = self.spawn_apple()

            if self.snake.get_head_position() == self.apple:
                self.snake.length += 1
                self.snake.score += 1
                self.apple = self.spawn_apple()

            self.surface.fill(BLACK)
            self.snake.draw(self.surface)
            pygame.draw.rect(self.surface, RED, (self.apple[0], self.apple[1], GRID_SIZE, GRID_SIZE))
            pygame.display.update()
            self.clock.tick(SPEED)