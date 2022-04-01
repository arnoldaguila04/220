def get_words(file_name):
    x = open(file_name, "r")
    return x.readlines()


def get_random_word(words):
    from random import randint
    return words[randint(0, len(words) - 1)].strip()


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True

    return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True

    return False


def make_hidden_secret(secret_word, guesses):
    blank = "_" * len(secret_word)
    list_blank = list(blank)
    for i in guesses:
        for j in range(len(secret_word)):
            if secret_word[j] == i:
                list_blank[j] = i
    return " ".join(list_blank)


def won(guessed):
    if guessed.count("_") == 0:
        return True

    return False


def play_graphics(secret_word):
    from graphics import *

    guesses = []
    remaining_guesses_number = 7  # number set to seven cause of program bug
    x = 1
    letter = ""

    # Graphics
    win = GraphWin("hangman", 500, 500)
    vertical_line = Line(Point(250, 150), Point(250, 350))  # Pole
    base_line = Line(Point(150, 350), Point(300, 350))  # Pole
    top_horizontal_line = Line(Point(250, 150), Point(150, 150))  # Pole
    rope = Line(Point(150, 150), Point(150, 200))  # Pole
    underscored_text = Text(Point(250, 400), make_hidden_secret(secret_word, guesses))  # starting underscore
    won_text = Text(Point(250, 400), "You Won!")  # winning text
    lose_text = Text(Point(250, 400), "You Lose. The word was " + secret_word)  # losing text
    input_box = Entry(Point(250, 450), 10)  # User Input
    patch = Line(Point(0, 0), Point(0, 0))  # quick Fix
    head = Circle(Point(150, 220), 20)  # Body
    body = Line(Point(150, 240), Point(150, 280))  # Body
    right_leg = Line(Point(150, 280), Point(170, 310))  # Body
    left_leg = Line(Point(150, 280), Point(130, 310))  # Body
    right_arm = Line(Point(150, 245), Point(170, 275))  # Body
    left_arm = Line(Point(150, 245), Point(130, 275))  # Body
    vertical_line.draw(win)  # Pole
    base_line.draw(win)  # Pole
    top_horizontal_line.draw(win)  # Pole
    rope.draw(win)  # Pole
    input_box.draw(win)  # User Input
    underscored_text.draw(win)
    hanged_body = [left_arm, right_arm, left_leg, right_leg, body, head, patch]  # hangman body part list + patch

    # process
    while x != 0:
        if won(make_hidden_secret(secret_word, guesses)) is True:
            won_text.draw(win)
            win.close()
            break
        if remaining_guesses_number == 0:
            lose_text.draw(win)
            win.close()
            print("loss")
            break
        if letter_in_secret_word(letter, secret_word) and already_guessed(letter, guesses):
            # color guess letter
            underscored_text.setText(make_hidden_secret(secret_word, guesses))
        else:
            remaining_guesses_number = remaining_guesses_number - 1
            hanged_body[remaining_guesses_number].draw(win)  # hangman body
            underscored_text.setText(make_hidden_secret(secret_word, guesses))
            # color guess letter
        letter = input_box.getText()
        guesses.append(letter)
        win.getKey()


def play_command_line(secret_word):
    guesses = []
    remaining_guesses_number = 7
    letter = ""
    while remaining_guesses_number != 0:
        if won(make_hidden_secret(secret_word, guesses)) is True:
            print("winner!")
            print("the secret word was ", secret_word)
            break
        if remaining_guesses_number == 0:
            print("sorry you did not guess the word.")
            print("the secret word was ", secret_word)
            break
        if letter_in_secret_word(letter, secret_word) and already_guessed(letter, guesses):
            print("already guessed: ", guesses)
            print(remaining_guesses_number)
            print(make_hidden_secret(secret_word, guesses))
        else:
            remaining_guesses_number = remaining_guesses_number - 1
            print("already guessed: ", guesses)
            print(remaining_guesses_number)
            print(make_hidden_secret(secret_word, guesses))
        letter = input("guess a letter: ")
        guesses.append(letter)


if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    # play_graphics(secret_word)
