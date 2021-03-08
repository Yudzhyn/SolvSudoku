import numpy as np

# all possible number in game
NUMBERS_LIST = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.int8)

# розмір матриці NxN
MATRIX_SIZE = 9

MATRIX      = np.array([[ 0, 0, 4,   0, 0, 0,   0, 6, 7 ],
                        [ 3, 0, 0,   4, 7, 0,   0, 0, 5 ],
                        [ 1, 5, 0,   8, 2, 0,   0, 0, 3 ],

                        [ 0, 0, 6,   0, 0, 0,   0, 3, 1 ],
                        [ 8, 0, 2,   1, 0, 5,   6, 0, 4 ],
                        [ 4, 1, 0,   0, 0, 0,   9, 0, 0 ],

                        [ 7, 0, 0,   0, 8, 0,   0, 4, 6 ],
                        [ 6, 0, 0,   0, 1, 2,   0, 0, 0 ],
                        [ 9, 3, 0,   0, 0, 0,   7, 1, 0 ] ], dtype=np.int8)

sub_square_test = MATRIX[0:3, 0:3]

def create_list_sub_squares(square):
    """
        Функція створює та повертає список підматриць.

        Type return: np.array
    """

    sub_squares_list = []
    row_start = 0
    row_finish = 3
    column_start = 0
    column_finish = 3

    for tmp1 in range(0, 3):
        for tmp2 in range(0, 3):
            sub_square = np.array(MATRIX[row_start : row_finish, column_start : column_finish])
            sub_squares_list.append(sub_square)
            column_start += 3
            column_finish += 3
        column_start = 0
        column_finish = 3
        row_start += 3
        row_finish += 3

    sub_squares_list = np.array(sub_squares_list, dtype=np.int8)
    return sub_squares_list


def determine_missing_numbers_square(sub_square):
    """
        Функція видає список відсутніх чисел-елементів у підматриці головної матриці Судоку.

        Type return: np.array
    """
    present_numbers = sub_square[sub_square > 0]
    return np.setxor1d(NUMBERS_LIST, present_numbers)


def check_number_in_row_and_column(checking_number, number_index):
    """
        Дана функція реалізована для переверки наявності аналогічного номеру
        в колонці або рядку.
        Якщо елемент знайдено, то функція повертає True, інакше -- False.

        Type return: bool
    """

    def passing_row():
        # перевірка по колонці
        for i in range(MATRIX_SIZE):
            if MATRIX[i][j_check_index] == checking_number:
                return True

    def passing_column():
        # перевірка по рядку
        for j in range(MATRIX_SIZE):
            if MATRIX[i_check_index][j] == checking_number:
                return True

    # i_index -- row, j_index -- column, elmenent_index -- tuple
    i_check_index, j_check_index = number_index

    # прапорець щодо присутності елемента у рядку або колонці
    number_present_flag = False

    # якщо елемент вже присутній в колонці -- перериваємо функцію і повертаємо True
    if passing_column() == True:
        return True

    # якщо елемент вже присутній в рядку -- перериваємо функцію і повертаємо True
    if passing_row() == True:
        return True

    # якщо елемент відсутній в рядку та в колонці -- функція повертає False
    return False



print(check_number_in_row_and_column(2, (1,1)))
