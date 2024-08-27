import pygame, sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
        self.direction = Vector2(-1,0)
        self.newblock = False
    def draw_snake(self):
        for block in self.body:
            snake_rect = pygame.Rect(block.x * cellsize, block.y * cellsize,cellsize,cellsize)
            pygame.draw.rect(screen, bluecolor, snake_rect)

    def movement_snake(self):
        if self.newblock == True:
            body_Copy = self.body[:]
            body_Copy.insert (0, body_Copy[0] + self.direction)
            self.body = body_Copy[:]
            self.newblock = False
        else:
             body_Copy = self.body[:-1]
             body_Copy.insert (0, body_Copy[0] + self.direction)
             self.body = body_Copy[:]

    def add_block(self):
        self.newblock = True

class FRUIT:
    def __init__(self):
        self.randomize()
    
    def draw_fruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cellsize, self.pos.y * cellsize, cellsize, cellsize)
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cellnumber - 1)
        self.y = random.randint(0, cellnumber - 1)
        self.pos = Vector2(self.x, self.y)
        

class MAIN:
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def update(self):
        self.snake.movement_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        
    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()

    def game_over(self):
        pygame.quit()
        sys.exit()
    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cellnumber or not 0 <= self.snake.body[0].y < cellnumber:
            self.game_over()
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()




cellsize = 40
cellnumber = 20

greencolor = (175,215, 70)
bluecolor = (0,0, 200)

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((cellsize * cellnumber, cellsize * cellnumber))
pygame.display.set_caption('snake')

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_game.game_over()
        
        if event.type == SCREEN_UPDATE:
            main_game.update()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_RIGHT:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_DOWN:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            

    screen.fill(greencolor) 
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60)
    




