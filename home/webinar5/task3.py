from itertools import count

dimension = 3
counter = count(1)
board = [[counter.__next__() for i in range(dimension)] for j in range(dimension)]


def draw_board(board):
    for i in range(dimension):
        print(board[i])


def coordinate(ceil_number: int, dimension: int):
    expr = ceil_number % dimension

    if expr == 0:
        row = (ceil_number // dimension) - 1
        col = dimension - 1
    else:
        row = (ceil_number + dimension) // dimension - 1
        col = expr - 1

    return {"row": row, "col": col}


draw_board(board)
print(coordinate(4, dimension))
