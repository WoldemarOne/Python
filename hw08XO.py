
class Board:
    def __init__(self, num_squares):
        self.num_squares = num_squares
        self.board = []
        self.wins = []

    def new_board(self):  # Создаем игровое поле
        for i in range(9):
            self.board.append(" ")
        return self.board

    def see_board(self):  # Показываем игровое поле
        print('\n\t', self.board[0], '|', self.board[1], '|', self.board[2])
        print('\t', '---------')
        print('\t', self.board[3], '|', self.board[4], '|', self.board[5])
        print('\t', '---------')
        print('\t', self.board[6], '|', self.board[7], '|', self.board[8], '\n')

    def victory(self):  # Условия победы
        self.wins = [(0, 1, 2),
                     (3, 4, 5),
                     (6, 7, 8),
                     (0, 3, 6),
                     (1, 4, 7),
                     (2, 5, 8),
                     (0, 4, 8),
                     (2, 4, 6)]
        for i in self.wins:
            if self.board[i[0]] == self.board[i[1]] == self.board[i[2]] != ' ':
                victory = self.board[i[1]]
                return victory
        if ' ' not in self.board:
            return draw
        return None

    def legal_moves(self):
        moves = []  # Доступные ходы
        for move in range(self.num_squares):
            if self.board[move] == ' ':
                moves.append(move)
        return moves

    @staticmethod
    def next(turn):  # Переход хода
        if turn == x:
            return o
        else:
            return x


class Player(Board):
    def move(self):  # Ход игрока
        self.board = self.board[:]
        legal = Board.legal_moves(self.board)
        move_player = 0
        while move_player not in legal:
            while move_player not in range(0, self.num_squares):
                move_player = int(input('Выберите одно из полей(0 - 8): '))
            if move_player not in legal:
                print('Поле занято. Выберите другое.\n')
        return move_player


class Computer(Board):
    def move(self):  # Ход компьютера
        self.board = self.board[:]
        best = (4, 0, 2, 6, 8, 1, 3, 5, 7)
        print('Компьютер выбрал', end=' ')
        for move_computer in Board.legal_moves(self.board):
            self.board[move_computer] = computer
            if Board.victory(self.board) == computer:
                print(move_computer)
                return move_computer
            self.board[move_computer] = ' '
        for move_computer in Board.legal_moves(self.board):
            self.board[move_computer] = player
            if Board.victory(self.board) == player:
                print(move_computer)
                return move_computer
            self.board[move_computer] = ' '
        for move_computer in best:
            if move_computer in Board.legal_moves(self.board):
                print(move_computer)
                return move_computer


print('''
    Игра крестики-нолики
    v. 0.2
    Чтобы сделать ход, введите число от 0 до 8.
    Число соответствует полю на доске, как показано ниже:
    
     0 | 1 | 2
     ---------
     3 | 4 | 5
     ---------
     6 | 7 | 8
     
     Пусть победит умнейший!
''')
x = 'X'
o = 'O'
draw = 'Ничья'
answer = ''
while answer not in ('y', 'n'):
    answer = input('Будете играть за крестики? (y/n): ').lower()
if answer == 'y':
    print('Игрок ходит крестиками первым')
    player = x
    computer = o
else:
    print('Компьютер ходит первым. Вы играете за нолики')
    player = o
    computer = x
turn = x
board = Board.new_board
while not Board.victory:
    if turn == player:
        move = Player.move
        board[move] = player
    else:
        move = Computer.move
        board[move] = computer
    print(Board.see_board)
    Board.next(turn)
the_winner = Board.victory
if the_winner == computer:
    print('Победа компьютера!')
elif the_winner == player:
    print('Поздравляю, Вы победили!')
elif the_winner == draw:
    print('Ничья!')
