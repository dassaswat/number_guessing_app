import random
import sys

attempt_count = []
name = []


def game_structure():
    random_num = random.randint(0, 20)
    while True:
        try:
            entered_num = input('Kindly enter a number between (0-20):    ')
            entered_num = int(entered_num)
        except ValueError:
            print("Wrong Entry! Try again..")
            continue
        else:
            if entered_num in range(0, 21):
                if entered_num > random_num:
                    print("It is lower")
                    attempt_count.append(int("1"))
                    continue
                elif entered_num < random_num:
                    print("It is higher")
                    attempt_count.append(int("1"))
                    continue
                elif entered_num == random_num:
                    attempt_count.append(int("1"))
                    print("Total attempts : {}".format(attempt_counter()))
                    play_again()
                    break
            else:
                print("Please try again. Enter a number between (0-20)")
                continue


def attempt_counter():
    return sum(attempt_count)


def attempt_count_deleter():
    for attempt in attempt_count.copy():
        attempt_count.remove(attempt)


def play_again():
    while True:
        play_again_request = input("Would you like to play the game again(Yes/No):    ")
        if play_again_request.lower() == "yes":
            print("HIGH SCORE: {}".format(attempt_counter()))
            attempt_count_deleter()
            game_structure()
            break
        elif play_again_request.lower() == "no":
            end_of_game()
            break
        else:
            print("\n")
            print("Kindly make a appropriate request(yes/no)")


def show_help():
    print("""
1. Enter a number between 0-20 in the prompt to see if your guess was right.
2. You will be notified about your status.
    ** For example:
        If your guess was greater than the actual number the prompter will notify ("It is lower")
        If your guess was less than the actual number the prompter will notify ("It is higher")
        Go on trying until the number matches with actual number.
        Finally if you want to play again type "Yes" in the prompt or "NO" to quit.
        Thank You for using...
    """)


def end_of_game():
    print("\n")
    sys.exit("Game Ended! Thank you {} for Playing the game..".format(name.pop()))


def user_name():
    player_name = input("Kindly enter your name to proceed:    ")
    print("Hello {}, Let's play the number guessing game".format(player_name))
    name.append(player_name)


if __name__ == '__main__':
    game_structure()
    attempt_counter()
    attempt_count_deleter()
    play_again()
    show_help()
    end_of_game()
    user_name()
