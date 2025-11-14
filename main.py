from colorama import Fore, Style
board = [["-" for _ in range(7)] for _ in range(6)]

def draw_board():
    global board
    for row in board:
        print(" ".join(row))

def player_input(player):
    x = float("inf")
    while True:
        try: x = int(input(f"player {player} turn: Enter x coord (1 - 7): ")) - 1
        except ValueError: print("Value Error")
        if x > -1 and x < 7: break
        else: print("try again")
    return x

def check_win():
    global board
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols - 3):
            if board[r][c] == board[r][c+1] == board[r][c+2] == board[r][c+3] != "-": return board[r][c]
    for r in range(rows - 3):
        for c in range(cols):
            if board[r][c] == board[r+1][c] == board[r+2][c] == board[r+3][c] != "-": return board[r][c]
    for r in range(rows - 3):
        for c in range(cols - 3):
            if board[r][c] == board[r+1][c+1] == board[r+2][c+2] == board[r+3][c+3] != "-": return board[r][c]
    for r in range(3, rows):
        for c in range(cols - 3):
            if board[r][c] == board[r-1][c+1] == board[r-2][c+2] == board[r-3][c+3] != "-": return board[r][c]
    return False

def main():
    player = 1
    while check_win() == False:
        if check_win() == Fore.BLUE + "●" + Style.RESET_ALL or check_win() == Fore.RED + "●" + Style.RESET_ALL: break
        draw_board()
        x = player_input(player)
        for i in range(len(board)):
            if player == 1:
                if board[-i-1][x] == "-":
                    board[-i-1][x] = Fore.RED + "●" + Style.RESET_ALL
                    break
                else: continue
            elif player == 2:
                if board[-i-1][x] == "-":
                    board[-i-1][x] = Fore.BLUE + "●" + Style.RESET_ALL
                    break
                else: continue
        player = 2 if player == 1 else 1
    draw_board()
    return f"player {check_win()} Won!"

if __name__ == "__main__":
    print(main())
