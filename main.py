def instructions():
    print("Table instructions!")
    print("Here is the cell numbers of the table, remember it before you choose!")
    print("╭───┬───┬───╮")
    print("│ 1 │ 2 │ 3 │")
    print("├───┼───┼───┤")
    print("│ 4 │ 5 │ 6 │")
    print("├───┼───┼───┤")
    print("│ 7 │ 8 │ 9 │")
    print("╰───┴───┴───╯")


def display():
    print("╭───┬───┬───╮")
    print(f"│ {cells['1']} │ {cells['2']} │ {cells['3']} │")
    print("├───┼───┼───┤")
    print(f"│ {cells['4']} │ {cells['5']} │ {cells['6']} │")
    print("├───┼───┼───┤")
    print(f"│ {cells['7']} │ {cells['8']} │ {cells['9']} │")
    print("╰───┴───┴───╯")


def keep_playing():
    answer = None

    while answer not in ["Y", "N"]:
        answer = input("Do you want to keep playing? (Y/N)\n").upper()

        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print(
                "Sorry, I don't understand, type Y if you want to keep playing or N if you don't"
            )


def symbol_choice():
    p1_symbol = None
    p2_symbol = None

    while p1_symbol not in ["X", "O"]:
        p1_symbol = input("Player 1 select your symbol: X or O\n").upper()

        if p1_symbol not in ["X", "O"]:
            print("Sorry, I don't understand, type X or O depending of what you want")

    if p1_symbol == "X":
        p2_symbol = "O"
    else:
        p2_symbol = "X"

    return [p1_symbol, p2_symbol]


# ========================================================== #
#                       MAIN GAME CODE                       #
# ========================================================== #

cells = {
    "1": " ",
    "2": " ",
    "3": " ",
    "4": " ",
    "5": " ",
    "6": " ",
    "7": " ",
    "8": " ",
    "9": " ",
}

restart = True

while restart:

    print("Welcome to the Tic Tac Toe game!")

    symbol_choice()
    print("----------")

    instructions()
    print("----------")
    print("Let's start the game!")

    restart = keep_playing()
    print("\n" * 3)
