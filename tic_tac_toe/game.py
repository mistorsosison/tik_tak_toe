class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        self.board[row][col] = player

    def display(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)


game = Board()
game.display()
game.make_move(1, 1, 'X')
print('Ход сделан!')
game.display()


from gameparts import Board  # noqa: E402
from gameparts.exceptions import CellOccupiedError, FieldIndexError  # noqa: E402


def save_result(result):
    file = open('results.txt', 'a')
    file.write(result + '\n')
    file.close()


def main():
    game = Board()
    # Первыми ходят крестики.
    current_player = 'X'
    running = True
    game.display()

    while running:

        print(f'Ходит {current_player}')

        while True:
            try:
                row = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except FieldIndexError:
                print(
                    'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значения для строки и столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
                continue
            except ValueError:
                print('Буквы вводить нельзя. Только числа.')
                print('Введите значения для строки и столбца заново.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            result = f'Победили {current_player}.'
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            result = 'Ничья!'
            print(result)
            save_result(result)
            running = False
        current_player = 'O' if current_player == 'X' else 'X'
if __name__ == '__main__':
    main()

while True:
    try:
        column = int(input('Введите номер столбца: '))
        if column < 0 or column >= game.field_size:
            raise FieldIndexError
        break
    except ValueError:
        print('Буквы вводить нельзя. Только числа.')
        print('Пожалуйста, введите значения для строки и столбца заново.')
        continue
    except Exception as e:
        print(f'Возникла ошибка: {e}')

def save_result(result):  # noqa: F811
    with open('results.txt', 'a') as f:
        f.write(result + '\n')

# game.py

import game  # noqa: E402


game.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = game.display.set_mode((WIDTH, HEIGHT))
game.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)


def draw_lines():
    for i in range(1, BOARD_SIZE):
        game.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    # Вертикальные линии.
    for i in range(1, BOARD_SIZE):
        game.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )

# Функция, которая отвечает за отрисовку фигур 
# (крестиков и ноликов) на доске. 
def draw_figures(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                game.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                game.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                game.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


import game  # noqa: E402

from gameparts import Board  # noqa: E402

game.init()

CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

screen = game.display.set_mode((WIDTH, HEIGHT))
game.display.set_caption('Крестики-нолики')
screen.fill(BG_COLOR)

def draw_lines():  # noqa: F811
    for i in range(1, BOARD_SIZE):
        game.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )

    for i in range(1, BOARD_SIZE):
        game.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )

def draw_figures(board):  # noqa: F811
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                game.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                game.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                game.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )

def save_result(result):  # noqa: F811
    with open('results.txt', 'a') as f:
        f.write(result + '\n')
def main():
    game = Board()
    current_player = 'X'
    running = True
    draw_lines()
    while running:
        for event in game.event.get():
            if event.type == game.QUIT:
                running = False
            if event.type == game.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]
                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE
                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)
                    if game.check_win(current_player):
                        result = f'Победили {current_player}.'
                        print(result)
                        save_result(result)
                        running = False
                    elif game.is_board_full():
                        result = 'Ничья!'
                        print(result)
                        save_result(result)
                        running = False
                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)
        game.display.update()
    game.quit()
if __name__ == '__main__':
    main()