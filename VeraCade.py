# Imports
"""install guizero using the 'pip install guizero' """
from guizero import Text, PushButton, Waffle, TextBox, Window, App
import random

start_page = App(title="Menu", bg="#ff0000", height=400)


def play_codle():  # Caleb Anstey
    # Word Generation
    rand_words = open("rand_words.txt", "r")
    for x in range(0, random.randint(0, 6747)):
        word = rand_words.readline(x)
    letters_caps = word.upper()
    letters = list(letters_caps)
    letters.pop()
    print()
    print(letters)
    print()
    print()

    # Wordle Box Colors
    yellow = "#c9b458"
    green = "#6aaa64"
    # white = "#ffffff"

    # app Initialization
    app = Window(start_page, title="CODLE", bg="white")

    # Functions
    num_guess_list = [1, 2, 3, 4, 5, 6, 7]

    def hide_start_menu():
        title.hide()
        start_button.hide()
        waffle.show()
        guess_button.show()
        guess_box.show()

    def enter_guess():
        guess = guess_box.value
        guess_box.clear()

        if len(guess) != 5:
            error_msg.show()
        else:
            error_msg.hide()
            err_msg.hide()
            val_guess = guess
            val_guess_caps = val_guess.upper()
            val_guess_letters = list(val_guess_caps)
            print(val_guess_letters)
            print()

            # Counting Guesses
            num_guess_list.pop()
            guess_remain = len(num_guess_list)

            # Checking Letters
            if guess_remain == 6:
                if val_guess_letters[0] == letters[0]:
                    waffle.set_pixel(0, 0, green)
                elif val_guess_letters[0] == letters[1]:
                    waffle.set_pixel(0, 0, yellow)
                elif val_guess_letters[0] == letters[2]:
                    waffle.set_pixel(0, 0, yellow)
                elif val_guess_letters[0] == letters[3]:
                    waffle.set_pixel(0, 0, yellow)
                elif val_guess_letters[0] == letters[4]:
                    waffle.set_pixel(0, 0, yellow)
                else:
                    pass

                if val_guess_letters[1] == letters[1]:
                    waffle.set_pixel(1, 0, green)
                elif val_guess_letters[1] == letters[0]:
                    waffle.set_pixel(1, 0, yellow)
                elif val_guess_letters[1] == letters[2]:
                    waffle.set_pixel(1, 0, yellow)
                elif val_guess_letters[1] == letters[3]:
                    waffle.set_pixel(1, 0, yellow)
                elif val_guess_letters[1] == letters[4]:
                    waffle.set_pixel(1, 0, yellow)
                else:
                    pass

                if val_guess_letters[2] == letters[2]:
                    waffle.set_pixel(2, 0, green)
                elif val_guess_letters[2] == letters[0]:
                    waffle.set_pixel(2, 0, yellow)
                elif val_guess_letters[2] == letters[1]:
                    waffle.set_pixel(2, 0, yellow)
                elif val_guess_letters[2] == letters[3]:
                    waffle.set_pixel(2, 0, yellow)
                elif val_guess_letters[2] == letters[4]:
                    waffle.set_pixel(2, 0, yellow)
                else:
                    pass

                if val_guess_letters[3] == letters[3]:
                    waffle.set_pixel(3, 0, green)
                elif val_guess_letters[3] == letters[0]:
                    waffle.set_pixel(3, 0, yellow)
                elif val_guess_letters[3] == letters[1]:
                    waffle.set_pixel(3, 0, yellow)
                elif val_guess_letters[3] == letters[2]:
                    waffle.set_pixel(3, 0, yellow)
                elif val_guess_letters[3] == letters[4]:
                    waffle.set_pixel(3, 0, yellow)
                else:
                    pass

                if val_guess_letters[4] == letters[4]:
                    waffle.set_pixel(4, 0, green)
                elif val_guess_letters[4] == letters[0]:
                    waffle.set_pixel(4, 0, yellow)
                elif val_guess_letters[4] == letters[1]:
                    waffle.set_pixel(4, 0, yellow)
                elif val_guess_letters[4] == letters[2]:
                    waffle.set_pixel(4, 0, yellow)
                elif val_guess_letters[4] == letters[3]:
                    waffle.set_pixel(4, 0, yellow)
                else:
                    pass

            elif guess_remain == 5:
                if val_guess_letters[0] == letters[0]:
                    waffle.set_pixel(0, 1, green)
                elif val_guess_letters[0] == letters[1]:
                    waffle.set_pixel(0, 1, yellow)
                elif val_guess_letters[0] == letters[2]:
                    waffle.set_pixel(0, 1, yellow)
                elif val_guess_letters[0] == letters[3]:
                    waffle.set_pixel(0, 1, yellow)
                elif val_guess_letters[0] == letters[4]:
                    waffle.set_pixel(0, 1, yellow)
                else:
                    pass

                if val_guess_letters[1] == letters[1]:
                    waffle.set_pixel(1, 1, green)
                elif val_guess_letters[1] == letters[0]:
                    waffle.set_pixel(1, 1, yellow)
                elif val_guess_letters[1] == letters[2]:
                    waffle.set_pixel(1, 1, yellow)
                elif val_guess_letters[1] == letters[3]:
                    waffle.set_pixel(1, 1, yellow)
                elif val_guess_letters[1] == letters[4]:
                    waffle.set_pixel(1, 1, yellow)
                else:
                    pass

                if val_guess_letters[2] == letters[2]:
                    waffle.set_pixel(2, 1, green)
                elif val_guess_letters[2] == letters[0]:
                    waffle.set_pixel(2, 1, yellow)
                elif val_guess_letters[2] == letters[1]:
                    waffle.set_pixel(2, 1, yellow)
                elif val_guess_letters[2] == letters[3]:
                    waffle.set_pixel(2, 1, yellow)
                elif val_guess_letters[2] == letters[4]:
                    waffle.set_pixel(2, 1, yellow)
                else:
                    pass

                if val_guess_letters[3] == letters[3]:
                    waffle.set_pixel(3, 1, green)
                elif val_guess_letters[3] == letters[0]:
                    waffle.set_pixel(3, 1, yellow)
                elif val_guess_letters[3] == letters[1]:
                    waffle.set_pixel(3, 1, yellow)
                elif val_guess_letters[3] == letters[2]:
                    waffle.set_pixel(3, 1, yellow)
                elif val_guess_letters[3] == letters[4]:
                    waffle.set_pixel(3, 1, yellow)
                else:
                    pass

                if val_guess_letters[4] == letters[4]:
                    waffle.set_pixel(4, 1, green)
                elif val_guess_letters[4] == letters[0]:
                    waffle.set_pixel(4, 1, yellow)
                elif val_guess_letters[4] == letters[1]:
                    waffle.set_pixel(4, 1, yellow)
                elif val_guess_letters[4] == letters[2]:
                    waffle.set_pixel(4, 1, yellow)
                elif val_guess_letters[4] == letters[3]:
                    waffle.set_pixel(4, 1, yellow)
                else:
                    pass

            elif guess_remain == 4:
                if val_guess_letters[0] == letters[0]:
                    waffle.set_pixel(0, 2, green)
                elif val_guess_letters[0] == letters[1]:
                    waffle.set_pixel(0, 2, yellow)
                elif val_guess_letters[0] == letters[2]:
                    waffle.set_pixel(0, 2, yellow)
                elif val_guess_letters[0] == letters[3]:
                    waffle.set_pixel(0, 2, yellow)
                elif val_guess_letters[0] == letters[4]:
                    waffle.set_pixel(0, 2, yellow)
                else:
                    pass

                if val_guess_letters[1] == letters[1]:
                    waffle.set_pixel(1, 2, green)
                elif val_guess_letters[1] == letters[0]:
                    waffle.set_pixel(1, 2, yellow)
                elif val_guess_letters[1] == letters[2]:
                    waffle.set_pixel(1, 2, yellow)
                elif val_guess_letters[1] == letters[3]:
                    waffle.set_pixel(1, 2, yellow)
                elif val_guess_letters[1] == letters[4]:
                    waffle.set_pixel(1, 2, yellow)
                else:
                    pass

                if val_guess_letters[2] == letters[2]:
                    waffle.set_pixel(2, 2, green)
                elif val_guess_letters[2] == letters[0]:
                    waffle.set_pixel(2, 2, yellow)
                elif val_guess_letters[2] == letters[1]:
                    waffle.set_pixel(2, 2, yellow)
                elif val_guess_letters[2] == letters[3]:
                    waffle.set_pixel(2, 2, yellow)
                elif val_guess_letters[2] == letters[4]:
                    waffle.set_pixel(2, 2, yellow)
                else:
                    pass

                if val_guess_letters[3] == letters[3]:
                    waffle.set_pixel(3, 2, green)
                elif val_guess_letters[3] == letters[0]:
                    waffle.set_pixel(3, 2, yellow)
                elif val_guess_letters[3] == letters[1]:
                    waffle.set_pixel(3, 2, yellow)
                elif val_guess_letters[3] == letters[2]:
                    waffle.set_pixel(3, 2, yellow)
                elif val_guess_letters[3] == letters[4]:
                    waffle.set_pixel(3, 2, yellow)
                else:
                    pass

                if val_guess_letters[4] == letters[4]:
                    waffle.set_pixel(4, 2, green)
                elif val_guess_letters[4] == letters[0]:
                    waffle.set_pixel(4, 2, yellow)
                elif val_guess_letters[4] == letters[1]:
                    waffle.set_pixel(4, 2, yellow)
                elif val_guess_letters[4] == letters[2]:
                    waffle.set_pixel(4, 2, yellow)
                elif val_guess_letters[4] == letters[3]:
                    waffle.set_pixel(4, 2, yellow)
                else:
                    pass

            elif guess_remain == 3:
                if val_guess_letters[0] == letters[0]:
                    waffle.set_pixel(0, 3, green)
                elif val_guess_letters[0] == letters[1]:
                    waffle.set_pixel(0, 3, yellow)
                elif val_guess_letters[0] == letters[2]:
                    waffle.set_pixel(0, 3, yellow)
                elif val_guess_letters[0] == letters[3]:
                    waffle.set_pixel(0, 3, yellow)
                elif val_guess_letters[0] == letters[4]:
                    waffle.set_pixel(0, 3, yellow)
                else:
                    pass

                if val_guess_letters[1] == letters[1]:
                    waffle.set_pixel(1, 3, green)
                elif val_guess_letters[1] == letters[0]:
                    waffle.set_pixel(1, 3, yellow)
                elif val_guess_letters[1] == letters[2]:
                    waffle.set_pixel(1, 3, yellow)
                elif val_guess_letters[1] == letters[3]:
                    waffle.set_pixel(1, 3, yellow)
                elif val_guess_letters[1] == letters[4]:
                    waffle.set_pixel(1, 3, yellow)
                else:
                    pass

                if val_guess_letters[2] == letters[2]:
                    waffle.set_pixel(2, 3, green)
                elif val_guess_letters[2] == letters[0]:
                    waffle.set_pixel(2, 3, yellow)
                elif val_guess_letters[2] == letters[1]:
                    waffle.set_pixel(2, 3, yellow)
                elif val_guess_letters[2] == letters[3]:
                    waffle.set_pixel(2, 3, yellow)
                elif val_guess_letters[2] == letters[4]:
                    waffle.set_pixel(2, 3, yellow)
                else:
                    pass

                if val_guess_letters[3] == letters[3]:
                    waffle.set_pixel(3, 3, green)
                elif val_guess_letters[3] == letters[0]:
                    waffle.set_pixel(3, 3, yellow)
                elif val_guess_letters[3] == letters[1]:
                    waffle.set_pixel(3, 3, yellow)
                elif val_guess_letters[3] == letters[2]:
                    waffle.set_pixel(3, 3, yellow)
                elif val_guess_letters[3] == letters[4]:
                    waffle.set_pixel(3, 3, yellow)
                else:
                    pass

                if val_guess_letters[4] == letters[4]:
                    waffle.set_pixel(4, 3, green)
                elif val_guess_letters[4] == letters[0]:
                    waffle.set_pixel(4, 3, yellow)
                elif val_guess_letters[4] == letters[1]:
                    waffle.set_pixel(4, 3, yellow)
                elif val_guess_letters[4] == letters[2]:
                    waffle.set_pixel(4, 3, yellow)
                elif val_guess_letters[4] == letters[3]:
                    waffle.set_pixel(4, 3, yellow)
                else:
                    pass

            elif guess_remain == 2:
                if val_guess_letters[0] == letters[0]:
                    waffle.set_pixel(0, 4, green)
                elif val_guess_letters[0] == letters[1]:
                    waffle.set_pixel(0, 4, yellow)
                elif val_guess_letters[0] == letters[2]:
                    waffle.set_pixel(0, 4, yellow)
                elif val_guess_letters[0] == letters[3]:
                    waffle.set_pixel(0, 4, yellow)
                elif val_guess_letters[0] == letters[4]:
                    waffle.set_pixel(0, 4, yellow)
                else:
                    pass

                if val_guess_letters[1] == letters[1]:
                    waffle.set_pixel(1, 4, green)
                elif val_guess_letters[1] == letters[0]:
                    waffle.set_pixel(1, 4, yellow)
                elif val_guess_letters[1] == letters[2]:
                    waffle.set_pixel(1, 4, yellow)
                elif val_guess_letters[1] == letters[3]:
                    waffle.set_pixel(1, 4, yellow)
                elif val_guess_letters[1] == letters[4]:
                    waffle.set_pixel(1, 4, yellow)
                else:
                    pass

                if val_guess_letters[2] == letters[2]:
                    waffle.set_pixel(2, 4, green)
                elif val_guess_letters[2] == letters[0]:
                    waffle.set_pixel(2, 4, yellow)
                elif val_guess_letters[2] == letters[1]:
                    waffle.set_pixel(2, 4, yellow)
                elif val_guess_letters[2] == letters[3]:
                    waffle.set_pixel(2, 4, yellow)
                elif val_guess_letters[2] == letters[4]:
                    waffle.set_pixel(2, 4, yellow)
                else:
                    pass

                if val_guess_letters[3] == letters[3]:
                    waffle.set_pixel(3, 4, green)
                elif val_guess_letters[3] == letters[0]:
                    waffle.set_pixel(3, 4, yellow)
                elif val_guess_letters[3] == letters[1]:
                    waffle.set_pixel(3, 4, yellow)
                elif val_guess_letters[3] == letters[2]:
                    waffle.set_pixel(3, 4, yellow)
                elif val_guess_letters[3] == letters[4]:
                    waffle.set_pixel(3, 4, yellow)
                else:
                    pass

                if val_guess_letters[4] == letters[4]:
                    waffle.set_pixel(4, 4, green)
                elif val_guess_letters[4] == letters[0]:
                    waffle.set_pixel(4, 4, yellow)
                elif val_guess_letters[4] == letters[1]:
                    waffle.set_pixel(4, 4, yellow)
                elif val_guess_letters[4] == letters[2]:
                    waffle.set_pixel(4, 4, yellow)
                elif val_guess_letters[4] == letters[3]:
                    waffle.set_pixel(4, 4, yellow)
                else:
                    pass

            elif guess_remain == 1:
                if val_guess_letters[0] == letters[0]:
                    waffle.set_pixel(0, 5, green)
                elif val_guess_letters[0] == letters[1]:
                    waffle.set_pixel(0, 5, yellow)
                elif val_guess_letters[0] == letters[2]:
                    waffle.set_pixel(0, 5, yellow)
                elif val_guess_letters[0] == letters[3]:
                    waffle.set_pixel(0, 5, yellow)
                elif val_guess_letters[0] == letters[4]:
                    waffle.set_pixel(0, 5, yellow)
                else:
                    pass

                if val_guess_letters[1] == letters[1]:
                    waffle.set_pixel(1, 5, green)
                elif val_guess_letters[1] == letters[0]:
                    waffle.set_pixel(1, 5, yellow)
                elif val_guess_letters[1] == letters[2]:
                    waffle.set_pixel(1, 5, yellow)
                elif val_guess_letters[1] == letters[3]:
                    waffle.set_pixel(1, 5, yellow)
                elif val_guess_letters[1] == letters[4]:
                    waffle.set_pixel(1, 5, yellow)
                else:
                    pass

                if val_guess_letters[2] == letters[2]:
                    waffle.set_pixel(2, 5, green)
                elif val_guess_letters[2] == letters[0]:
                    waffle.set_pixel(2, 5, yellow)
                elif val_guess_letters[2] == letters[1]:
                    waffle.set_pixel(2, 5, yellow)
                elif val_guess_letters[2] == letters[3]:
                    waffle.set_pixel(2, 5, yellow)
                elif val_guess_letters[2] == letters[4]:
                    waffle.set_pixel(2, 5, yellow)
                else:
                    pass

                if val_guess_letters[3] == letters[3]:
                    waffle.set_pixel(3, 5, green)
                elif val_guess_letters[3] == letters[0]:
                    waffle.set_pixel(3, 5, yellow)
                elif val_guess_letters[3] == letters[1]:
                    waffle.set_pixel(3, 5, yellow)
                elif val_guess_letters[3] == letters[2]:
                    waffle.set_pixel(3, 5, yellow)
                elif val_guess_letters[3] == letters[4]:
                    waffle.set_pixel(3, 5, yellow)
                else:
                    pass

                if val_guess_letters[4] == letters[4]:
                    waffle.set_pixel(4, 5, green)
                elif val_guess_letters[4] == letters[0]:
                    waffle.set_pixel(4, 5, yellow)
                elif val_guess_letters[4] == letters[1]:
                    waffle.set_pixel(4, 5, yellow)
                elif val_guess_letters[4] == letters[2]:
                    waffle.set_pixel(4, 5, yellow)
                elif val_guess_letters[4] == letters[3]:
                    waffle.set_pixel(4, 5, yellow)
                else:
                    pass

                guess_button.disable()
                guess_box.disable()
                cont_button.show()

            else:
                print("Unexpected Error")

        if val_guess_letters == letters:
            correct_msg.show()
            guess_button.hide()
            guess_box.hide()
            cont_button.show()

    def cont():
        app.destroy()

    # Title Page
    title = Text(app, text="CODLE", color="black", align="top", height="10", size="40", font="Public Pixel")
    start_button = PushButton(app, text="START", command=hide_start_menu)
    start_button.font = "Public Pixel"

    # Waffle
    waffle = Waffle(app, height=6, width=5)
    waffle.pixel_size = 55
    waffle.hide()

    # TextBox
    guess_box = TextBox(app)
    guess_box.hide()

    # Guess Button
    guess_button = PushButton(app, text="Guess", command=enter_guess)
    guess_button.hide()
    guess_button.font = "Public Pixel"

    # Error Message
    error_msg = Text(app, color="red", text="Invalid Input - Be sure to guess a word with 5 letters!")
    error_msg.hide()

    # Err Msg 2
    err_msg = Text(app, color="red", text="Guess a different word!")
    err_msg.hide()

    # Correct Guess
    correct_msg = Text(app, color="green", text=f"Congratulations, you correctly guessed {word} Good Job!")
    correct_msg.hide()

    # Continue Button
    cont_button = PushButton(app, text="Menu", command=cont)
    cont_button.hide()
    cont_button.font = "Public Pixel"

    # Display app (guizero)
    app.show()


def tictactoe_multiplayer():  # Caleb Anstey
    tac_window = Window(start_page, title="Tic-Tac-Toe Multiplayer", layout="grid", height=325, width=565, bg="white")

    plays_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def but_1():
        if len(plays_list) % 2 != 0:
            button_1.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_1.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_1.disable()
        check_for_winner()

    def but_2():
        if len(plays_list) % 2 != 0:
            button_2.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_2.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_2.disable()
        check_for_winner()

    def but_3():
        if len(plays_list) % 2 != 0:
            button_3.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_3.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_3.disable()
        check_for_winner()

    def but_4():
        if len(plays_list) % 2 != 0:
            button_4.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_4.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_4.disable()
        check_for_winner()

    def but_5():
        if len(plays_list) % 2 != 0:
            button_5.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_5.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_5.disable()
        check_for_winner()

    def but_6():
        if len(plays_list) % 2 != 0:
            button_6.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_6.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_6.disable()
        check_for_winner()

    def but_7():
        if len(plays_list) % 2 != 0:
            button_7.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_7.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_7.disable()
        check_for_winner()

    def but_8():
        if len(plays_list) % 2 != 0:
            button_8.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_8.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_8.disable()
        check_for_winner()

    def but_9():
        if len(plays_list) % 2 != 0:
            button_9.text = "X"
            plays_list.pop()
        elif len(plays_list) % 2 == 0:
            button_9.text = "O"
            plays_list.pop()
        else:
            print("Error")

        button_9.disable()
        check_for_winner()

    # buttons
    button_1 = PushButton(tac_window, grid=[0, 0], width=15, height=5, text=" ", command=but_1)
    button_2 = PushButton(tac_window, grid=[1, 0], width=15, height=5, text=" ", command=but_2)
    button_3 = PushButton(tac_window, grid=[2, 0], width=15, height=5, text=" ", command=but_3)
    button_4 = PushButton(tac_window, grid=[0, 1], width=15, height=5, text=" ", command=but_4)
    button_5 = PushButton(tac_window, grid=[1, 1], width=15, height=5, text=" ", command=but_5)
    button_6 = PushButton(tac_window, grid=[2, 1], width=15, height=5, text=" ", command=but_6)
    button_7 = PushButton(tac_window, grid=[0, 2], width=15, height=5, text=" ", command=but_7)
    button_8 = PushButton(tac_window, grid=[1, 2], width=15, height=5, text=" ", command=but_8)
    button_9 = PushButton(tac_window, grid=[2, 2], width=15, height=5, text=" ", command=but_9)

    def return_too_menu():
        win_window.destroy()
        tac_window.destroy()

    def check_for_winner():
        def winner1():
            winner = Text(win_window, text="Player 1 wins!", font="Public Pixel", color="white", size=20)
            Text(win_window, text=" ")
            return_menu_button = PushButton(win_window, text="Menu", command=return_too_menu)
            return_menu_button.show()
            winner.show()
            win_window.show()
            button_1.disable()
            button_2.disable()
            button_3.disable()
            button_4.disable()
            button_5.disable()
            button_6.disable()
            button_7.disable()
            button_8.disable()
            button_9.disable()

        def winner2():
            winner = Text(win_window, text="Player 2 wins!", font="Public Pixel", color="white", size=20)
            Text(win_window, text=" ")
            return_menu_button = PushButton(win_window, text="Menu", command=return_too_menu)
            return_menu_button.show()
            winner.show()
            win_window.show()
            button_1.disable()
            button_2.disable()
            button_3.disable()
            button_4.disable()
            button_5.disable()
            button_6.disable()
            button_7.disable()
            button_8.disable()
            button_9.disable()

        def tied_match():
            winner = Text(win_window, text="Tied Game", font="Public Pixel", color="white", size=20)
            Text(win_window, text=" ")
            return_menu_button = PushButton(win_window, text="Menu", command=return_too_menu)
            return_menu_button.show()
            winner.show()
            win_window.show()
            button_1.disable()
            button_2.disable()
            button_3.disable()
            button_4.disable()
            button_5.disable()
            button_6.disable()
            button_7.disable()
            button_8.disable()
            button_9.disable()

        if button_1.text and button_2.text and button_3.text == "X":
            if button_1.text == "X":
                if button_2.text == "X":
                    if button_3.text == "X":
                        winner1()

        if button_4.text and button_5.text and button_6.text == "X":
            if button_4.text == "X":
                if button_5.text == "X":
                    if button_6.text == "X":
                        winner1()

        if button_7.text and button_8.text and button_9.text == "X":
            if button_7.text == "X":
                if button_8.text == "X":
                    if button_9.text == "X":
                        winner1()

        if button_1.text and button_4.text and button_7.text == "X":
            if button_1.text == "X":
                if button_4.text == "X":
                    if button_7.text == "X":
                        winner1()

        if button_2.text and button_5.text and button_8.text == "X":
            if button_2.text == "X":
                if button_5.text == "X":
                    if button_8.text == "X":
                        winner1()

        if button_3.text and button_6.text and button_9.text == "X":
            if button_3.text == "X":
                if button_6.text == "X":
                    if button_9.text == "X":
                        winner1()

        if button_1.text and button_5.text and button_9.text == "X":
            if button_1.text == "X":
                if button_5.text == "X":
                    if button_9.text == "X":
                        winner1()

        if button_3.text and button_5.text and button_7.text == "X":
            if button_3.text == "X":
                if button_5.text == "X":
                    if button_7.text == "X":
                        winner1()

        """WINNER 2"""

        if button_1.text and button_2.text and button_3.text == "O":
            if button_1.text == "O":
                if button_2.text == "O":
                    if button_3.text == "O":
                        winner2()

        if button_4.text and button_5.text and button_6.text == "O":
            if button_4.text == "O":
                if button_5.text == "O":
                    if button_6.text == "O":
                        winner2()

        if button_7.text and button_8.text and button_9.text == "O":
            if button_7.text == "O":
                if button_8.text == "O":
                    if button_9.text == "O":
                        winner2()

        if button_1.text and button_4.text and button_7.text == "O":
            if button_1.text == "O":
                if button_4.text == "O":
                    if button_7.text == "O":
                        winner2()

        if button_2.text and button_5.text and button_8.text == "O":
            if button_2.text == "O":
                if button_5.text == "O":
                    if button_8.text == "O":
                        winner2()

        if button_3.text and button_6.text and button_9.text == "O":
            if button_3.text == "O":
                if button_6.text == "O":
                    if button_9.text == "O":
                        winner2()

        if button_1.text and button_5.text and button_9.text == "O":
            if button_1.text == "O":
                if button_5.text == "O":
                    if button_9.text == "O":
                        winner2()

        if button_3.text and button_5.text and button_7.text == "O":
            if button_3.text == "O":
                if button_5.text == "O":
                    if button_7.text == "O":
                        winner2()

        """TIED"""

        if len(plays_list) == 0:
            tied_match()

    win_window = Window(start_page, title="Winner", height=100, bg="#ff0000")
    win_window.hide()


one_hangman = "_"
two_hangman = "_"
three_hangman = "_"
four_hangman = "_"
five_hangman = "_"


def play_hangman():  # Caleb Anstey
    app = Window(start_page, title="Hangman", width=325, height=400, layout="grid", bg="white")

    rand_words = open("rand_words.txt", "r")
    for x in range(0, random.randint(0, 6747)):
        word = rand_words.readline(x)
    letters_caps = word.upper()
    letters = list(letters_caps)
    letters.pop()
    print(letters)

    remaining_turns = [1, 2, 3, 4, 5, 6]

    def check():
        global one_hangman
        global two_hangman
        global three_hangman
        global four_hangman
        global five_hangman
        global letter_guessed

        letter_guessed = letter_guess.value.upper()
        # print(letter_guessed)
        letter_guess.clear()
        if len(letter_guessed) == 1:

            app.width = 325

            invalid_letter.hide()
            if letter_guessed in letters:

                if letter_guessed == letters[0]:
                    # print("correct 1")
                    one_hangman = letter_guessed
                    letters_correct.value = f"{one_hangman} {two_hangman} {three_hangman} {four_hangman} {five_hangman}"

                if letter_guessed == letters[1]:
                    # print("correct 2")
                    two_hangman = letter_guessed
                    letters_correct.value = f"{one_hangman} {two_hangman} {three_hangman} {four_hangman} {five_hangman}"

                if letter_guessed == letters[2]:
                    # print("correct 3")
                    three_hangman = letter_guessed
                    letters_correct.value = f"{one_hangman} {two_hangman} {three_hangman} {four_hangman} {five_hangman}"

                if letter_guessed == letters[3]:
                    # print("correct 4")
                    four_hangman = letter_guessed
                    letters_correct.value = f"{one_hangman} {two_hangman} {three_hangman} {four_hangman} {five_hangman}"

                if letter_guessed == letters[4]:
                    # print("correct 5")
                    five_hangman = letter_guessed
                    letters_correct.value = f"{one_hangman} {two_hangman} {three_hangman} {four_hangman} {five_hangman}"

                if one_hangman and two_hangman and three_hangman and four_hangman and five_hangman != "_":
                    if one_hangman == letters[0]:
                        if two_hangman == letters[1]:
                            if three_hangman == letters[2]:
                                if four_hangman == letters[3]:
                                    if five_hangman == letters[4]:
                                        congrats_msg = Text(app,
                                                            text=f"Congrats, you correctly guessed {word} Good job!",
                                                            grid=(1, 4))
                                        congrats_msg.show()
                                        enter_butt0n.disable()
                                        letter_guess.disable()
                                        home_button.show()

                                        one_hangman = "_"
                                        two_hangman = "_"
                                        three_hangman = "_"
                                        four_hangman = "_"
                                        five_hangman = "_"

                                        app.width = 415
            else:
                incorrect_message = Text(app, text=f"{letter_guessed} is not in the word.", grid=(1, 4))
                incorrect_message.show()
                remaining_turns.pop()
        else:
            invalid_letter.show()

            app.width = 400

        if len(remaining_turns) == 6:
            hangman = Text(app, text="  ______ \n"
                                     "  |    | \n"
                                     "  |    | \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "__|__", grid=(1, 5))
            hangman.show()
        if len(remaining_turns) == 5:
            hangman = Text(app, text="  ______ \n"
                                     "  |    | \n"
                                     "  |    | \n"
                                     "  |    0 \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "__|__", grid=(1, 5))
            hangman.show()
        if len(remaining_turns) == 4:
            hangman = Text(app, text="  ______ \n"
                                     "  |    | \n"
                                     "  |    | \n"
                                     "  |    0 \n"
                                     "  |    | \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "__|__", grid=(1, 5))
            hangman.show()
        if len(remaining_turns) == 3:
            hangman = Text(app, text="  ______ \n"
                                     "  |    | \n"
                                     "  |    | \n"
                                     "  |    0 \n"
                                     "  |   /|\ \n"
                                     "  |      \n"
                                     "  |      \n"
                                     "__|__", grid=(1, 5))
            hangman.show()
        if len(remaining_turns) == 2:
            hangman = Text(app, text="  ______ \n"
                                     "  |    | \n"
                                     "  |    | \n"
                                     "  |    0 \n"
                                     "  |   /|\ \n"
                                     "  |   /  \n"
                                     "  |      \n"
                                     "__|__", grid=(1, 5))
            hangman.show()
        if len(remaining_turns) == 1:
            hangman = Text(app, text="  ______ \n"
                                     "  |    | \n"
                                     "  |    | \n"
                                     "  |    0 \n"
                                     "  |   /|\ \n"
                                     "  |   / \ \n"
                                     "  |      \n"
                                     "__|__", grid=(1, 5))
            hangman.show()

            Text(app, text="You Lost", color="red", size=18, grid=(1, 6), font="Public Pixel")

            app.width = 375

            enter_butt0n.disable()
            letter_guess.disable()
            home_button.show()

            one_hangman = "_"
            two_hangman = "_"
            three_hangman = "_"
            four_hangman = "_"
            five_hangman = "_"

    Text(app, text="Please guess a letter:", grid=(0, 1))
    invalid_letter = Text(app, text=f"Invalid Input: Please enter one letter!", grid=(1, 8))
    letter_guess = TextBox(app, grid=(1, 1))
    enter_butt0n = PushButton(app, text="Enter", command=check, grid=(2, 1))
    enter_butt0n.font = "Public Pixel"
    enter_butt0n.text_size = 10
    letters_correct = Text(app, text=f"{one_hangman} {two_hangman} {three_hangman} {four_hangman} {five_hangman}",
                           grid=(1, 0), size=10, font="Public Pixel")

    def menu_main():
        app.destroy()

    home_button = PushButton(app, text="Menu", command=menu_main, grid=(1, 7))
    home_button.hide()
    home_button.font = "Public Pixel"
    home_button.text_size = 10
    letters_correct.show()
    invalid_letter.hide()


def play_rock_paper_scissors():  # Logan Corbett / Ty Freda
    rock_paper = Window(start_page, title="Rock Paper Scissors", height=300)

    plays = ["scissors", "rock", "paper"]

    def ai_text():
        if choice.value.lower() in plays:
            ai_choice = random.choice(plays)

            ai_text.value = f"AI chose {ai_choice}"

            if choice.value.lower() == ai_choice:
                winning_player.value = f"Both players selected {choice.value.lower()}. It's a tie!"

            elif choice.value.lower() == "rock":
                if ai_choice == "scissors":
                    winning_player.value = "Rock smashes scissors! You win!"
                else:
                    winning_player.value = "Paper covers rock! You lose."
            elif choice.value.lower() == "paper":
                if ai_choice == "rock":
                    winning_player.value = "Paper covers rock! You win!"
                else:
                    winning_player.value = "Scissors cuts paper! You lose."
            elif choice.value.lower() == "scissors":
                if ai_choice == "paper":
                    winning_player.value = "Scissors cuts paper! You win!"
                else:
                    winning_player.value = "Rock smashes scissors! You lose."
            else:
                print("Error")

    text = Text(rock_paper, text="Welcome to rock paper scissors! Please input your move.")
    text.show()
    choice = TextBox(rock_paper)
    select = PushButton(rock_paper, text="Click me when you have made your selection", command=ai_text)
    select.show()

    Text(rock_paper, text=" ")

    ai_text = Text(rock_paper, text=" ", font="Public Pixel")
    winning_player = Text(rock_paper, text=" ")

    Text(rock_paper, text=" ")

    def return_to_menu():
        rock_paper.destroy()

    menu_button = PushButton(rock_paper, text="Menu", command=return_to_menu)
    menu_button.font = "Public Pixel"


Text(start_page, text=" ", color="#ff0000", bg="#ff0000")

Text(start_page, text="VERACADE", color="white", bg="#ff0000", size=30, font="Public Pixel")

Text(start_page, text=" ", color="#ff0000", bg="#ff0000")
Text(start_page, text=" ", color="#ff0000", bg="#ff0000")

codle_button = PushButton(start_page, text="Play Codle", command=play_codle, width=25)
Text(start_page, text=" ", color="#ff0000", bg="#ff0000")
codle_button.font = "Public Pixel"

tictactoe_multi_button = PushButton(start_page, text="Play Tic-Tac-Toe", command=tictactoe_multiplayer, width=25)
Text(start_page, text=" ", color="#ff0000", bg="#ff0000")
tictactoe_multi_button.font = "Public Pixel"

hangman_button = PushButton(start_page, text="Play Hangman", command=play_hangman, width=25)
Text(start_page, text=" ", color="#ff0000", bg="#ff0000")
hangman_button.font = "Public Pixel"

rock_paper_button = PushButton(start_page, text="Play Rock-Paper-Scissors", command=play_rock_paper_scissors, width=25)
Text(start_page, text=" ", color="#ff0000", bg="#ff0000")
rock_paper_button.font = "Public Pixel"

start_page.display()
