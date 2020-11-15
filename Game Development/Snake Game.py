import random, pygame, sys
from pygame.locals import *

FPS = 10
windowwidth = 500
windowheight = 500
cellsize = 20
cellwidth = windowwidth // cellsize
cellheight = windowheight // cellsize

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY = (40, 40, 40)
BGCOLOR = BLACK


def main():
    global fps_clock, display_surf, basic_font
    pygame.init()
    fps_clock = pygame.time.Clock()
    display_surf = pygame.display.set_mode((windowwidth, windowheight))
    basic_font = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Snake Game')

    while True:
        runGame()
        showGameOverScreen()


def runGame():
    startx = random.randint(5, cellwidth - 6)
    starty = random.randint(5, cellheight - 6)
    snake_block = [{'x': startx, 'y': starty},
                   {'x': startx - 1, 'y': starty},
                   {'x': startx - 2, 'y': starty}]

    direction = RIGHT
    apple = getRandomLocation()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

                    # check if the worm has hit itself or edge
        if snake_block[HEAD]['x'] == -1 or \
                snake_block[HEAD]['x'] == cellwidth \
                or snake_block[HEAD]['y'] == -1 or \
                snake_block[HEAD]['y'] == cellheight:
            return  # game over
        for snakebody in snake_block[1:]:
            if snakebody['x'] == snake_block[HEAD]['x'] and \
                    snakebody['y'] == snake_block[HEAD]['y']:
                return  # game over

        # check if worm has eaten an apple
        if snake_block[HEAD]['x'] == apple['x'] and \
                snake_block[HEAD]['y'] == apple['y']:

            # don't remove snake's tail block
            # set a new apple in any random place
            apple = getRandomLocation()
        else:
            del snake_block[-1]  # remove snake's tail block

        # move the worm by adding a block in the direction
        if direction == UP:
            newHead = {'x': snake_block[HEAD]['x'], 'y': snake_block[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': snake_block[HEAD]['x'], 'y': snake_block[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': snake_block[HEAD]['x'] - 1, 'y': snake_block[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': snake_block[HEAD]['x'] + 1, 'y': snake_block[HEAD]['y']}

        snake_block.insert(0, newHead)
        display_surf.fill(BGCOLOR)
        drawGrid()
        drawWorm(snake_block)
        drawApple(apple)
        drawScore(len(snake_block) - 3)
        pygame.display.update()
        fps_clock.tick(FPS)


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, cellwidth - 1),
            'y': random.randint(0, cellheight - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 70)
    gameSurf = gameOverFont.render('Game Over', True, RED)
    gameRect = gameSurf.get_rect()
    gameRect.midtop = (windowheight / 2, 10)
    display_surf.blit(gameSurf, gameRect)
    pygame.display.update()
    pygame.time.wait(500)


def drawScore(score):
    scoreSurf = basic_font.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (windowwidth - 120, 10)
    display_surf.blit(scoreSurf, scoreRect)


def drawWorm(snake_block):
    for coord in snake_block:
        x = coord['x'] * cellsize
        y = coord['y'] * cellsize
        wormSegmentRect = pygame.Rect(x, y, cellsize, cellsize)
        pygame.draw.rect(display_surf, DARKGREEN, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, cellsize - 8,
                                           cellsize - 8)
        pygame.draw.rect(display_surf, GREEN, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * cellsize
    y = coord['y'] * cellsize
    appleRect = pygame.Rect(x, y, cellsize, cellsize)
    pygame.draw.rect(display_surf, RED, appleRect)


def drawGrid():
    for x in range(0, windowwidth, cellsize):  # draw vertical lines
        pygame.draw.line(display_surf, DARKGRAY, (x, 0), (x, windowheight))
    for y in range(0, windowheight, cellsize):  # draw horizontal lines
        pygame.draw.line(display_surf, DARKGRAY, (0, y), (windowwidth, y))


if __name__ == '__main__':
    main()
