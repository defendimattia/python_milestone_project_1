def display():
    print("╭───┬───┬───╮")
    print("│   │   │   │")
    print("├───┼───┼───┤")
    print("│   │   │   │")
    print("├───┼───┼───┤")
    print("│   │   │   │")
    print("╰───┴───┴───╯")


def keep_playing():
    answer = None

    while answer not in ["Y","N"]:
        answer = input("Do you want to keep playing? (Y/N)\n").upper()
    
        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Sorry, I don't understand, type Y if you want to keep playing or N if you don't")



# ========================================================== #
#                       MAIN GAME CODE                       #
# ========================================================== #

restart = True

while restart:

    print("Welcome to the Tic Tac Toe game!")

    restart = keep_playing()
    print("\n"*3)

