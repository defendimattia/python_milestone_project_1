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


def win_or_draw_check():

    for a, b, c in winning_lines:
        if cells[a] == cells[b] == cells[c] and cells[a] in ("X", "O"):
            return 1 if cells[a] == p1_symbol else 2

    if " " not in cells.values():
        return 0


def player_move(player_playing):
    p_cell = None

    while (
        p_cell not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        or cells[p_cell] != " "
    ):
        p_cell = input("Type a number from 1 to 9 to choose an empty cell\n")

        if (
            p_cell not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            or cells[p_cell] != " "
        ):
            print("Wrong input! Type a number from 1 to 9 to choose an empty cell\n")

    if player_playing == 1:
        cells[p_cell] = p1_symbol
        player_playing = 2
    else:
        cells[p_cell] = p2_symbol
        player_playing = 1

    return player_playing


def reset():
    win_or_draw = False
    player_playing = 1
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

    return win_or_draw, player_playing, cells


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

winning_lines = [
    ("1", "2", "3"),
    ("4", "5", "6"),
    ("7", "8", "9"),
    ("1", "4", "7"),
    ("2", "5", "8"),
    ("3", "6", "9"),
    ("1", "5", "9"),
    ("3", "5", "7"),
]


restart = True
win_or_draw = False
player_playing = 1

# ========================================================== #
#                       MAIN GAME CODE                       #
# ========================================================== #


while restart:

    win_or_draw, player_playing, cells = reset()
    print("Welcome to the Tic Tac Toe game!")

    p1_symbol, p2_symbol = symbol_choice()
    print("----------")

    instructions()
    print("----------")
    print("Let's start the game!")

    while not win_or_draw:
        print(f"Player {player_playing} turn!")

        display()
        player_playing = player_move(player_playing)

        check = win_or_draw_check()

        if check == 1:
            display()
            print("Player 1 wins!")
            win_or_draw = True

        elif check == 2:
            display()
            print("Player 2 wins!")
            win_or_draw = True

        elif check == 0:
            display()
            print("Draw!")
            win_or_draw = True

    restart = keep_playing()
    print("\n" * 3)
