import game
game.init()

screen = game.display.set_mode((800, 600))
game.display.set_caption('Пример графического окна Pygame')


running = True

while running:
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
    game.draw.line(screen, (255, 0, 0), (100, 100), (700, 500), 5)
    game.draw.rect(screen, (0, 128, 0), game.Rect(300, 200, 200, 200))
    game.display.update()
game.quit()
