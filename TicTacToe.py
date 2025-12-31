def main():
    create_board("xoxoxoxox")
    
    
def create_board(board_str): 
    str_to_chars = iter(board_str)
    rows, cols = 3, 3
    board = [[0 for x in range(cols)] for y in range(rows)]

    for row_index in range(rows):
        for column_index in range(cols):
            char = next(str_to_chars)
            if char in 'xo':
                board[row_index][column_index] = char
            else:
                board[row_index][column_index] = ''

    print(board)


if __name__ == "__main__":
    main()