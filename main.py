
# prints the board
def display_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('-----------')
    print(f' {board[3]} | {board[4]} | {board[5] }')
    print('-----------')
    print(f' {board[6]} | {board[7]} | {board[8]} ')


# receives the players choice
def player_choice():
    choice = 'Wrong'

    # exception handling to ensure choice is a playable position
    in_range = False
    while not in_range:
        choice = input("Please select a square (1-9): ")

        if choice.isdigit() and 0 < int(choice) < 10:
            in_range = True
        else: print('Sorry, that is an invalid input!')

    return int(choice)


# place the current players mark at the selected position
def make_move(board, position, mark):
    board[position-1] = mark
    return board


# checks the availability of a given position on the board
def is_available(board, position):
    return board[position-1].isdigit()


# switches players between turns
def switch_players(current):
    if current == 1: return 2
    else: return 1


# checks if the board is filled to handle a tie condition
def board_full(board):
    filled = True
    for entry in board:
        if entry.isdigit(): filled = False
    return filled


# checks if there has been a winner
def is_winner(board):

    # possible win sequences
    wins = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
    scores = {1: set(), 2: set()}

    # creates a set with the positional values for each player
    for i in range(len(board)):
        if board[i] == 'X': scores[1].add(i+1)
        elif board[i] == 'O': scores[2].add(i+1)

    # compares the sets to see if they include any winning combinations
    for possibility in wins:
        if scores[1].issuperset(possibility) or scores[2].issuperset(possibility): return True
    return False


# determines whether game continues to run or end
def game_on(board):
    return not(is_winner(board) or board_full(board))


# combines previous elements to run the game from start to finish
def run_game():

    # initializes player index, board, and marks
    current_player = 2
    game_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    player_marks = {1: 'X', 2: 'O'}

    # runs the game as long as there is no winner or a filled board
    while game_on(game_board):

        # displays the board and switches to the next player
        display_board(game_board)
        current_player = switch_players(current_player)

        # receives a valid and available input from the player and makes the move on the board
        choice = player_choice()
        while not is_available(game_board, choice):
            print('Sorry, this spot is not available!')
            choice = player_choice()
        else:
            make_move(game_board, choice, player_marks[current_player])
            # loops for the next players turn if game does not end
    else:

        # shows the final board and states who the winner is or whether it was a time
        display_board(game_board)
        if is_winner(game_board): print(f'Player {current_player} wins!')
        else: print('The game is a tie!')


if __name__ == '__main__':
    run_game()

