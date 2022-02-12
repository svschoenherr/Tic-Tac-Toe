# Implement board
board = '''
     |     |   
  1  |  2  |  3
_____|_____|____
     |     |   
  4  |  5  |  6
_____|_____|____
     |     |   
  7  |  8  |  9
     |     |
'''

# Implement logo
logo = '''
| | (_)    | |           | |            
| |_ _  ___| |_ __ _  ___| |_ ___   ___ 
| __| |/ __| __/ _` |/ __| __/ _ \ / _ \\
| |_| | (__| || (_| | (__| || (_) |  __/
 \__|_|\___|\__\__,_|\___|\__\___/ \___|
'''
print(logo)

# Implement instructions for player
print("Welcome to Tic Tac Toe! This is a two player game to place your symbol 'X' or 'O' into the grid. The one having three in one row wins! \nPlease choose your position by typing a number between 1 and 9.\n")
print(board)

count = 0

# Ask for players move as long as game has not finished
game_is_finished = False
while not game_is_finished:
    move = input("Please choose between 1 and 9 to set your mark: ")
    count += 1

    # Add players moves to board
    board = board.replace(move, "O")
    print(board)

    if count == 9:
        game_is_finished = True

# TODO Implement game logic to end game

# TODO Feat1
    # Implement input checks for not allowed chars,
    # already blocked positions

# TODO Feat2
    # Implement random "KI" moves