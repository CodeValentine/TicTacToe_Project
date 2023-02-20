#Unit1 Project Codecademy, Computer Science Career Path
#import draw_board function from helpers
from helpers import draw_board, check_turn
import os 

spots = {1 : '1', 2 : '2', 3 : '3', 4 : '4', 5 : '5', 6 : '6', 7 : '7', 8 : '8', 9 : '9'}

playing = True
turn = 0
prev_turn = -1


while playing:
    #Reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    #If an invalid turn occurred, let the player know
    if prev_turn == turn:
    print("Invalid spot selected, please pick another.")
    print("Player " + str((turn % 2) +1) + "'s turn: Pick your spot or press q to quit")
    #Get input from player
    choice = input()
    if choice == 'q':
        playing = False
    #Check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        #Check if the spot has already been taken
        if not spots[int(choice)] in {"X", "0"}:
                #Valid input, update the board
                turn += 1
                spots[int(choice)] = check_turn(turn)



