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
    pass


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
