from random_word import RandomWords

number_of_tries = 0
game = True
r = RandomWords()


def find_indexes(word, letter):
    indexes = []

    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append(index)

    return indexes


def show_state_of_game():
    print()
    print(user_word)
    print("Remaining trials:", number_of_tries)
    print("Letters used:", used_letters)
    print()


while game:
    used_letters = []
    user_word = []
    word = r.get_random_word().upper()

    for _ in word:
        user_word.append("_")
    while number_of_tries == 0:
        print("Choose a difficulty level")
        print("Easy - 5 chances, Medium - 3 chances, Hard - 1 chance")
        print("E - Easy, M - Medium, H - Hard")
        choice = input("Choice: ").upper()
        if choice == "E":
            number_of_tries = 6
        elif choice == "M":
            number_of_tries = 4
        elif choice == "H":
            number_of_tries = 2
        else:
            print("Incorrect answer")
            print()

    while number_of_tries != 0:
        letter = input("Enter a letter: ").upper()
        if len(letter) != 1:
            print("Wrong length")
            continue
        elif not letter.isalpha():
            print("The character entered is not a letter")
            continue
        elif letter in used_letters:
            print("Letter has already been entered")
            show_state_of_game()
            continue
        used_letters.append(letter)

        found_indexes = find_indexes(word, letter)

        if len(found_indexes) == 0:
            print("Missing letter in the word")
            number_of_tries -= 1

            if number_of_tries == 0:
                print("You lost")
                print("Search word", word)
                next_game = input("Do you want to play again?(Y - yes): ").upper()
                if next_game != "Y":
                    game = False
        else:
            for index in found_indexes:
                user_word[index] = letter
            if "_" not in user_word:
                print("You won! Congratulations!")
                number_of_tries = 0
                next_game = input("Do you want to play again?(Y - yes): ").upper()
                if next_game != "Y":
                    game = False

        show_state_of_game()

print("Thank you for the game :)")
