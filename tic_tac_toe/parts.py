class Board:
    """Этот класс создаёт новое поле и ставит знак x и 0."""

    def __init__(self):
        """Этот метод создаёт игровое поле 3x3."""

        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        """Этот метод ставит в клетку символ игрока."""

        self.board[row][col] = player

    def display(self):
        """Этот метод отрисовывает визуальные границы игрового поля."""

        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

