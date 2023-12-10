import pygame as pg


pg.init()


SCREEN = (800, 800)

screen = pg.display.set_mode(SCREEN)

clock = pg.time.Clock()


CELL_SIZE = 800 // 20

CELLS = (SCREEN[0] // CELL_SIZE, SCREEN[1] // CELL_SIZE)


class Snake:
    def __init__(self, x, y) -> None:
        self.cells = [(x, y)]

    def draw(self, surface: pg.Surface):
        for x, y in self.cells:
            r = pg.Rect(x * CELL_SIZE + 1, y * CELL_SIZE
                        + 1, CELL_SIZE - 1, CELL_SIZE - 1)
            pg.draw.rect(surface, (255, 0, 0), r)

    def up(self):
        new_element = (self.cells[0][0], self.cells[0][1] - 1)
        self.cells.insert(0, new_element)
        self.cells.pop()

    def down(self):
        new_element = (self.cells[0][0], self.cells[0][1] + 1)
        self.cells.insert(0, new_element)
        self.cells.pop()

    def right(self):
        new_element = (self.cells[0][0] + 1, self.cells[0][1])
        self.cells.insert(0, new_element)
        self.cells.pop()

    def left(self):
        new_element = (self.cells[0][0] - 1, self.cells[0][1])
        self.cells.insert(0, new_element)
        self.cells.pop()


snake: Snake = Snake(CELLS[0]//2, CELLS[1]//2)


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                snake.up()
            if event.key == pg.K_DOWN:
                snake.down()
            if event.key == pg.K_RIGHT:
                snake.right()
            if event.key == pg.K_LEFT:
                snake.left()

    screen.fill((55, 55, 55))

    for y in range(0, SCREEN[1], CELL_SIZE):
        pg.draw.line(screen, (255, 255, 255), (0, y), (SCREEN[0], y))

    for x in range(0, SCREEN[0], CELL_SIZE):
        pg.draw.line(screen, (255, 255, 255), (x, 0), (x, SCREEN[1]))

    snake.draw(screen)  # type: ignore
    pg.display.update()

pg.quit()
