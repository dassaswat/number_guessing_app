import core_game_structure


def start_game():

    print("""
                    ---------------------------------------------
                     Welcome! Lets play the Number Guessing game
                    ---------------------------------------------
    """)
    print("\n")
    core_game_structure.user_name()
    core_game_structure.show_help()
    core_game_structure.game_structure()
    core_game_structure.play_again()


start_game()
