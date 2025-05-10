from itertools import combinations

# Magic square positions (1-indexed)
magic_map = {
    1: 8, 2: 1, 3: 6,
    4: 3, 5: 5, 6: 7,
    7: 4, 8: 9, 9: 2
}

# Preferred move order: center, corners, sides
priority = [5, 1, 3, 7, 9, 2, 4, 6, 8]  # 1-indexed

# Game state
board = [' ' for _ in range(9)]
player_moves = {'X': [], 'O': []}

def display_board():
    print()
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")
    print()

# Place the move on board and update player's list
def go(pos, player):
    idx = pos - 1
    if board[idx] == ' ':
        board[idx] = player
        player_moves[player].append(magic_map[pos])
        return True
    return False

# Check if a player can win in the next move
def posswin(player):
    taken = player_moves[player]
    empty_positions = [i+1 for i in range(9) if board[i] == ' ']
    for pos in empty_positions:
        trial = taken + [magic_map[pos]]
        for combo in combinations(trial, 3):
            if sum(combo) == 15:
                return pos
    return -1

# Choose best move: center → corners → sides
def make2():
    for pos in priority:
        if board[pos - 1] == ' ':
            return pos
    return -1

# Game loop
current_player = 'X'
opponent = 'O'

for turn in range(9):
    display_board()

    # Try to win
    move = posswin(current_player)
    if move != -1:
        go(move, current_player)
    else:
        # Try to block opponent
        move = posswin(opponent)
        if move != -1:
            go(move, current_player)
        else:
            # Otherwise, pick next best
            move = make2()
            go(move, current_player)

    # Check for win
    if len(player_moves[current_player]) >= 3:
        for combo in combinations(player_moves[current_player], 3):
            if sum(combo) == 15:
                display_board()
                print(f"Player {current_player} wins!")
                exit()

    # Switch turns
    current_player, opponent = opponent, current_player

# If loop ends without win
display_board()
print("It's a draw!")
