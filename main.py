import sys
import random
from variables import *
from logiques import Snake


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 24, bold=True)
        self.snake = Snake()
        self.direction_lock = False
        self.spawn_apple()
        self.move_delay = 150
        self.last_move = pygame.time.get_ticks()

    def spawn_apple(self):
        while True:
            self.apple = [random.randrange(0, WIDTH, CELL_SIZE),
                          random.randrange(0, HEIGHT, CELL_SIZE)]
            if self.apple not in self.snake.segments: break

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and not self.direction_lock:
                if event.key == UP and self.snake.direction != DOWN:
                    self.snake.direction = UP
                    self.direction_lock = True
                elif event.key == DOWN and self.snake.direction != UP:
                    self.snake.direction = DOWN
                    self.direction_lock = True
                elif event.key == LEFT and self.snake.direction != RIGHT:
                    self.snake.direction = LEFT
                    self.direction_lock = True
                elif event.key == RIGHT and self.snake.direction != LEFT:
                    self.snake.direction = RIGHT
                    self.direction_lock = True

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_move > self.move_delay:
            self.direction_lock = False
            new_head = self.snake.move()

            if self.snake.check_collision(new_head):
                self.snake.reset()
                self.move_delay = 150
            elif new_head == self.apple:
                self.snake.grow(new_head)
                self.spawn_apple()
                self.move_delay = max(100, self.move_delay - 10)
            else:
                self.snake.crawl(new_head)
            self.last_move = now

    def draw(self):
        self.screen.fill(COLOR_BG)
        for y in range(0, HEIGHT, CELL_SIZE):
            for x in range(0, WIDTH, CELL_SIZE):
                if (x // CELL_SIZE + y // CELL_SIZE) % 2 == 0:
                    pygame.draw.rect(self.screen, COLOR_GRID, (x, y, CELL_SIZE, CELL_SIZE))

        pygame.draw.rect(self.screen, COLOR_APPLE, (self.apple[0] + 2, self.apple[1] + 2, CELL_SIZE - 4, CELL_SIZE - 4))


        for i, seg in enumerate(self.snake.segments):
            color = COLOR_SNAKE_HEAD if i == 0 else COLOR_SNAKE_BODY
            pygame.draw.rect(self.screen, color, (seg[0] + 1, seg[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))

        d_score = self.snake.score
        self.screen.blit(self.font.render(f"Score: {d_score}", True, (255, 255, 255)), (10, 10))
        pygame.display.flip()


if __name__ == "__main__":
    Game().run()