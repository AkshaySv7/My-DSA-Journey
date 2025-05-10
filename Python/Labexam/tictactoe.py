from itertools import combinations

# Mapping cell positions (1–9) to magic square values
magic_square = {
    1: 8, 2: 1, 3: 6,
    4: 3, 5: 5, 6: 7,
    7: 4, 8: 9, 9: 2
}

# Display board (positions 1–9)
def display_board(board):
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

# Check if player has any 3 numbers summing to 15
def check_win(moves):
    for combo in combinations(moves, 3):
        if sum(combo) == 15:
            return True
    return False

# Initialize
board = [' ' for _ in range(9)]
player_moves = {'X': [], 'O': []}
current_player = 'X'

# Game Loop
for turn in range(9):
    display_board(board)
    try:
        move = int(input(f"Player {current_player}, enter your move (1-9): "))
    except ValueError:
        print("Invalid input. Try again.")
        continue
    if move < 1 or move > 9 or board[move - 1] != ' ':
        print("Invalid move. Try again.")
        continue

    board[move - 1] = current_player
    player_moves[current_player].append(magic_square[move])

    if len(player_moves[current_player]) >= 3 and check_win(player_moves[current_player]):
        display_board(board)
        print(f"Player {current_player} wins!")
        break

    # Switch player
    current_player = 'O' if current_player == 'X' else 'X'

else:
    display_board(board)
    print("It's a draw!")
