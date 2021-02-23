def print_square(square_input):

    def print_long_line():
        print("+-------+-------+-------+")
        return None

    def print_line_with_numbers(n):
        long_line = f'| {n[0]} {n[1]} {n[2]} | {n[3]} {n[4]} {n[5]} | {n[6]} {n[7]} {n[8]} |'
        long_line = long_line.replace('0', '.');
        print(long_line)
        return None


    for line_row_number in range(0, 9):
        if line_row_number % 3 == 0:
            print_long_line()
        print_line_with_numbers(square_input[line_row_number])

    print_long_line()

    return None
