from itertools import count
from itertools import cycle


def init_board(dimension: int):
    counter = count(1)
    return [[counter.__next__() for i in range(dimension)] for j in range(dimension)]

def draw_board(board: list):
    for i in range(len(board)):
        print(board[i])


def convert_number_to_coordinate(ceil_number: int, dimension: int):
    expr = ceil_number % dimension

    if expr == 0:
        row = (ceil_number // dimension) - 1
        col = dimension - 1
    else:
        row = (ceil_number + dimension) // dimension - 1
        col = expr - 1

    return {"row": row, "col": col}


def check_win(board: list, coordinate: dict[str, int], token: str):
    row = coordinate.get("row")
    col = coordinate.get("col")

    horisontal_win = True
    vertical_win = True
    in_main_diagonal = (row == col)
    main_diagonal_win = in_main_diagonal
    in_secondary_diagonal = (row == (len(board) - 1) - col)
    secondary_diagonal_win = in_secondary_diagonal


    for i in range(len(board)):
        if board[row][i] != token:
            horisontal_win = False
            break

    for i in range(len(board)):
        if board[i][col] != token:
            vertical_win = False
            break

    if in_main_diagonal:
        for i in range(len(board)):
            if board[i][i] != token:
                main_diagonal_win = False
                break

    if in_secondary_diagonal:
        for i in range(len(board)):
            if board[i][len(board) - 1 - i] != token:
                secondary_diagonal_win = False
                break

    return horisontal_win or vertical_win or main_diagonal_win or secondary_diagonal_win



dimension = 3 #int(input("Введите размерность сетки: "))
board = init_board(dimension)
round_counter = 0
min_round_count = (dimension * 2) - 1
max_round_count = (dimension * dimension)
is_win = False

tokenIterator = cycle("+-")
for token in tokenIterator:
    draw_board(board)
    print(f"Ход игрока {token}")

    while True:
        ceil_number = int(input(f"Введите номер ячейки для вставки {token} "))
        coordinate = convert_number_to_coordinate(ceil_number, dimension)
        if ceil_number != board[coordinate["row"]][coordinate["col"]]:
            print("Ячейка занята")
            continue
        board[coordinate["row"]][coordinate["col"]] = token
        round_counter = round_counter + 1
        if round_counter >= min_round_count:
            is_win = check_win(board, coordinate, token)
        break

    if is_win:
        draw_board(board)
        print(f"Победу одержал {token}")
        break

    if round_counter == max_round_count:
        draw_board(board)
        print("Ничья")
        break






