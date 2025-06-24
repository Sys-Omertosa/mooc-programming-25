def who_won(game_board):
    p1_score, p2_score = 0, 0
    for row in game_board:
        p1_score += row.count(1)
        p2_score += row.count(2)

    if p1_score > p2_score:
        return 1
    elif p2_score > p1_score:
        return 2
    else:
        return 0