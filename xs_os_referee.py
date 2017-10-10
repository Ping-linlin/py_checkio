def checkio(game_result):
    # i hava no idear
    rows = game_result
    # print(zip(*rows))
    cols = map(''.join, zip(*rows))
    # print(cols)
    # exit(2)
    # for i, r in enumerate(rows):
    #     print(i, r)
    diags = map(''.join, zip(*[(r[i], r[2 - i]) for i, r in enumerate(rows)]))
    lines = rows + list(cols) + list(diags)
    return 'X' if ('XXX' in lines) else 'O' if ('OOO' in lines) else 'D'

# speedy
def checkio(game_result):
    for i in range(3):
        if (game_result[i][0] in ['O', 'X']) and (game_result[i][0] == game_result[i][1] == game_result[i][2]):
            return game_result[i][0]
        if (game_result[0][i] in ['O', 'X']) and (game_result[0][i] == game_result[1][i] == game_result[2][i]):
            return game_result[0][i]
    if (game_result[1][1] in ['O', 'X']) and ((game_result[0][0] == game_result[1][1] == game_result[2][2]) or (game_result[0][2] == game_result[1][1] == game_result[2][0])):
        return game_result[1][1]
    return "D"

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")