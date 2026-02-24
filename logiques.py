from variables import *

class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        x = (WIDTH // 2 // CELL_SIZE) * CELL_SIZE
        y = (HEIGHT // 2 // CELL_SIZE) * CELL_SIZE

        self.segments = [[x, y], [x - CELL_SIZE, y], [x - 2 * CELL_SIZE, y]]
        self.direction = RIGHT
        self.score = 0

    def move(self):
        head_x, head_y = self.segments[0]
        if self.direction == UP: head_y -= CELL_SIZE
        elif self.direction == DOWN: head_y += CELL_SIZE
        elif self.direction == LEFT: head_x -= CELL_SIZE
        elif self.direction == RIGHT: head_x += CELL_SIZE
        return [head_x, head_y]

    def grow(self, new_head):
        self.segments.insert(0, new_head)
        self.score += 1

    def crawl(self, new_head):
        self.segments.insert(0, new_head)
        self.segments.pop()

    def check_collision(self, head):
        x, y = head
        return (x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or head in self.segments)