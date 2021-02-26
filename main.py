import numpy as np
from print import print_square

# CONSTANTS
# all possible number in game
NUMBERS_LIST = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=np.short)

# TEST SQUARE
SQUARE_TEST = np.array([[ 0, 0, 4,   0, 0, 0,   0, 6, 7 ],
                        [ 3, 0, 0,   4, 7, 0,   0, 0, 5 ],
                        [ 1, 5, 0,   8, 2, 0,   0, 0, 3 ],

                        [ 0, 0, 6,   0, 0, 0,   0, 3, 1 ],
                        [ 8, 0, 2,   1, 0, 5,   6, 0, 4 ],
                        [ 4, 1, 0,   0, 0, 0,   9, 0, 0 ],

                        [ 7, 0, 0,   0, 8, 0,   0, 4, 6 ],
                        [ 6, 0, 0,   0, 1, 2,   0, 0, 0 ],
                        [ 9, 3, 0,   0, 0, 0,   7, 1, 0 ] ], dtype=np.short)

def main():
    pass

main()

print_square(SQUARE_TEST)