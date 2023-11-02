EMPTY = ' '
INVALID = 'X'
FINAL = 'F'


MOVES = [
    [2, 1],
    [2, -1],
    [-2, 1],
    [-2, -1],
    [1, 2],
    [1, -2],
    [-1, 2],
    [-1, -2]
]


def initialize_board(rows, cols):
    a_board = []
    for row in range(rows):
        a_row = []
        for col in range(cols):
            a_row.append(EMPTY)
        a_board.append(a_row)
    return a_board


def print_board(a_board, message=''):
    print("{} ".format(message).ljust(40, '-'))
    for row in a_board:
        print('| '+' | '.join(map(lambda x: str(x).rjust(2, ' '), row))+' |')


def mark_position(a_board, position, value):
    a_board[position[0]][position[1]] = value


def mark_positions(a_board, positions, value):
    for position in positions:
        if a_board[position[0]][position[1]] != FINAL:
            mark_position(a_board, position, value)


def evaluate_move(a_board, position, move):
    y = position[0] + move[0]
    x = position[1] + move[1]
    if y < 0 or y > len(a_board)-1 or x < 0 or x > len(a_board)-1:
        return INVALID
    return a_board[y][x]


def has_final_position(positions, final_position):
    for position in positions:
        if position[0] == final_position[0] and position[1] == final_position[1]:
            return True
    return False


def find_next_positions(a_board, positions):
    next_positions = []
    for position in positions:
        for move in MOVES:
            status = evaluate_move(a_board, position, move)
            if status == FINAL or status == EMPTY:
                next_positions.append([position[0] + move[0], position[1] + move[1]])
    return next_positions


def play(a_board, final_position, positions, step=0):
    mark_positions(a_board, positions, step)
    print_board(a_board, 'step: {}'.format(step))
    next_positions = find_next_positions(a_board, positions)
    if len(next_positions) <= 0:
        return [-1, None]
    if has_final_position(next_positions, final_position) is True:
        return [0, step + 1]
    return play(a_board, final_position, next_positions, step + 1)

# -----------------------


board = initialize_board(8, 8)

final = [1, 7]
mark_position(board, final, FINAL)

impossibles = [
    [1, 1],[1,2],[1,3],
    [2, 2],[2,1],
    [1, 3],[2, 3],[3, 3],[4, 3],[5, 3],[6, 3]
]
for impossible in impossibles:
    mark_position(board, impossible, INVALID)

# print_board(board)
initial = [0, 0]
print(play(board, final, [initial]))
