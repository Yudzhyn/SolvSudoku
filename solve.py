import numpy as np


# all possible number in game
NUMBERS_LIST = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.short)

SQUARE_TEST = np.array([[ 0, 0, 4,   0, 0, 0,   0, 6, 7 ],
                        [ 3, 0, 0,   4, 7, 0,   0, 0, 5 ],
                        [ 1, 5, 0,   8, 2, 0,   0, 0, 3 ],

                        [ 0, 0, 6,   0, 0, 0,   0, 3, 1 ],
                        [ 8, 0, 2,   1, 0, 5,   6, 0, 4 ],
                        [ 4, 1, 0,   0, 0, 0,   9, 0, 0 ],

                        [ 7, 0, 0,   0, 8, 0,   0, 4, 6 ],
                        [ 6, 0, 0,   0, 1, 2,   0, 0, 0 ],
                        [ 9, 3, 0,   0, 0, 0,   7, 1, 0 ] ], dtype=np.short)

sub_square_test = SQUARE_TEST[0:3, 0:3]

# створює список підквадратів
def create_list_sub_squares(square):

    sub_squares_list = []
    row_start = 0
    row_finish = 3
    column_start = 0
    column_finish = 3

    for tmp1 in range(0, 3):
        for tmp2 in range(0, 3):
            sub_square = np.array(SQUARE_TEST[row_start : row_finish, column_start : column_finish])
            sub_squares_list.append(sub_square)
            column_start += 3
            column_finish += 3
        column_start = 0
        column_finish = 3
        row_start += 3
        row_finish += 3

    sub_squares_list = np.array(sub_squares_list, dtype=np.short)
    return sub_squares_list

# видає список відсутніх чисел у підквадраті
def determine_missing_numbers_square(sub_square):
    present_numbers = sub_square[sub_square>0]
    return np.setxor1d(NUMBERS_LIST, present_numbers)

create_list_sub_squares(SQUARE_TEST)

