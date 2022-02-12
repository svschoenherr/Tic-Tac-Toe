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

def game():
    # Implement board
    global board
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

    print(board)

    # Count used to end game after all 9 moves and to decide who has one, if that's the case
    count = 0

    # Initialise moves dict to track the moves the players have done
    moves = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

    # Ask for players move as long as game has not finished
    game_is_finished = False
    while not game_is_finished:

        # Select player based on move count
        player = count % 2 + 1
        if player == 1:
            player_symbol = "O"
        else:
            player_symbol = "X"

        move_is_valid = False
        # TODO Feat1
        # Implement input checks for not allowed chars,
        while not move_is_valid:
            move = input(f"Player {player}, please choose between 1 and 9 to set your {player_symbol}: ")
            if not move.isdigit() or int(move) < 1 or int(move) > 9:
                print("\nInvalid input! Please enter a number between 1 and 9.\n")
                print(board)
            else:
                # TODO Check for move has been taken
                move_is_valid = True

        # Add players moves to board
        board = board.replace(move, player_symbol)
        moves[int(move)] = player_symbol

        count += 1
 
        print(board)

        # Implement game logic to end game
        # Check if any line contains equal sign
        if moves[1] == moves[2] == moves[3] or \
            moves[4] == moves[5] == moves[6] or \
            moves[7] == moves[8] == moves[9] or \
            moves[1] == moves[4] == moves[7] or \
            moves[2] == moves[5] == moves[8] or \
            moves[3] == moves[6] == moves[9] or \
            moves[1] == moves[5] == moves[9] or \
            moves[3] == moves[5] == moves[7]:
            game_is_finished = True

    # If game is finished due to a completed line, declare winner based on the last move
        if game_is_finished:
            if count % 2 == 1:
                print("Player 1 wins")
            else:
                print("Player 2 wins")

        # End game if no one has won
        if count == 9 and not game_is_finished:
            game_is_finished = True
            print("It's a draw!")

        if game_is_finished and input("\nWanna play again? Y/N ").upper() == "Y":
            game()
game()

# TODO Feat2
    # Implement random "KI" moves