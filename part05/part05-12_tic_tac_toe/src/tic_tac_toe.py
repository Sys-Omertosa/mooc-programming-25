def play_turn(game_board, x, y, piece):
    if 0<=x<=2 and 0<=y<=2 and game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False