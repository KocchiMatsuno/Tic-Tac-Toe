from tkinter import *
import random

def show_game_frame():
    main_menu_frame.pack_forget()
    game_frame.pack()

def start_game():
    show_game_frame()
    if against_ai:
        player = "O"
        ai_move()
    else:
        player = "X"
    label.config(text=f"{player}'s Turn")

def restart_game():
    global player
    player = "O"
    for row in range(3):
        for column in range(3):
            tiles[row][column].config(text="")
            score_display.config(text="")
    reset_board_colors()

def reset_board_colors():
    for row in range(3):
        for column in range(3):
            tiles[row][column].config(bg="#86db9d")

def show_main_menu():
    game_frame.pack_forget()
    main_menu_frame.pack()

def play_against_ai():
    global against_ai
    against_ai = True
    start_game()

def play_against_human():
    global against_ai
    against_ai = False
    start_game()


def nxt_move(row, column):
    global player

    if tiles[row][column]["text"] == "" and win_detect() is False:
        # Human player's move
        tiles[row][column]["text"] = player

        if win_detect() is False:
            # Update the player for the next turn
            player = players[0] if player == players[1] else players[1]

            if against_ai and player == players[1]:
                ai_move()

            label.config(text=f"{player}'s Turn")

            if win_detect() is True:
                label.config(text=(players[1] + " wins"))
            elif win_detect() == "draw":
                label.config(text="Tied!")

def ai_move():
    global player

    ai_symbol = "O" if player[0] == "X" else "X"
    empty_spots = [(r, c) for r in range(3) for c in range(3) if tiles[r][c]["text"] == ""]

    if empty_spots:
        ai_row, ai_column = random.choice(empty_spots)
        tiles[ai_row][ai_column]["text"] = ai_symbol

        if win_detect() is False:
            players[0] = player[0]

def win_detect():
    global tiles

    # VERTICAL CHECKING
    for row in range(3):
        if tiles[row][0]["text"] == tiles[row][1]["text"] == tiles[row][2]["text"] != "":
            tiles[row][0].config(bg="white")
            tiles[row][1].config(bg="white")
            tiles[row][2].config(bg="white")
            return True

    # HORIZONTAL CHECKING
    for column in range(3):
        if tiles[0][column]["text"] == tiles[1][column]["text"] == tiles[2][column]["text"] != "":
            tiles[0][column].config(bg="white")
            tiles[1][column].config(bg="white")
            tiles[2][column].config(bg="white")
            return True

    # DIAGONAL CHECKING
    if tiles[0][0]["text"] == tiles[1][1]["text"] == tiles[2][2]["text"] != "":
        tiles[0][0].config(bg="white")
        tiles[1][1].config(bg="white")
        tiles[2][2].config(bg="white")
        return True

    # DIAGONAL CHECKING (REVERSE)
    elif tiles[2][0]["text"] == tiles[1][1]["text"] == tiles[0][2]["text"] != "":
        tiles[2][0].config(bg="white")
        tiles[1][1].config(bg="white")
        tiles[0][2].config(bg="white")
        return True

    elif draw() is False:
        return "draw"

    else:
        return False

def draw():
    isEmpty = 0

    for row in range(3):
        for column in range(3):
            if tiles[row][column]["text"] != "":
                isEmpty += 1

    if isEmpty == 9:
        tiles[0][0].config(bg="#e84c41")
        tiles[0][1].config(bg="#e84c41")
        tiles[0][2].config(bg="#e84c41")
        tiles[1][0].config(bg="#e84c41")
        tiles[1][1].config(bg="#e84c41")
        tiles[1][2].config(bg="#e84c41")
        tiles[2][0].config(bg="#e84c41")
        tiles[2][1].config(bg="#e84c41")
        tiles[2][2].config(bg="#e84c41")
        return False
    else:
        return True

def create_main_menu_frame():
    main_menu = Frame(window, bg="#86db9d")
    main_menu.pack(expand=True, fill="both")

    title_label = Label(main_menu, text="Tic Tac Toe", font=("Arial", 20, "bold"), bg="#86db9d")
    title_label.pack(pady=20)

    play_human_button = Button(main_menu, text="Play against Human", font=("Arial", 15, "bold"), bg="#789e82", command=play_against_human)
    play_human_button.pack()

    play_ai_button = Button(main_menu, text="Play against AI", font=("Arial", 15, "bold"), bg="#789e82", command=play_against_ai)
    play_ai_button.pack()

    quit_button = Button(main_menu, text="Quit", font=("Arial", 15, "bold"), bg="#789e82", command=window.destroy)
    quit_button.pack(pady=20)

    return main_menu

window = Tk()
window.geometry("330x390")
window.resizable(0, 0)
window.title("Tic Tac Toe")

players = ["X", "O"]
player = "O"
against_ai = False  # Variable to determine whether playing against AI or not

tiles = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

main_menu_frame = create_main_menu_frame()
game_frame = Frame(window)

label = Label(game_frame, text="X's Turn", font=("Arial", 15, "bold"), padx=20)
reset_button = Button(game_frame, text="RESET", font=("Arial", 13, "bold"), bg="#789e82", command=restart_game)
frame = Frame(game_frame)
score_display = Label(game_frame, text="", font=("Arial", 15, "bold"))

for row in range(3):
    for column in range(3):
        tiles[row][column] = Button(frame, text="", font=('consolas', 40), width=3, height=1,
                                    command=lambda row=row, column=column: nxt_move(row, column), bd=3, bg="#86db9d")
        tiles[row][column].grid(row=row, column=column)

reset_button.pack(side=BOTTOM, pady=10)
frame.pack()
score_display.pack()

show_main_menu()

window.mainloop()
