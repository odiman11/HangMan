HANGMAN_win_loss = {
"lose":'''
\033[0;33m  ___________\033[0;0m..\033[0;33m_______
\033[0;33m| .__________\033[0;0m))\033[0;33m______|
\033[0;33m| | / /      \033[0;0m||
\033[0;33m| |/ /       \033[0;0m||
\033[0;33m| | /        \033[0;0m||.-''.
\033[0;33m| |/         \033[0;0m|/  _  \\
\033[0;33m| |          \033[0;0m||  `/,|
\033[0;33m| |          \033[0;0m(\\`_.'
\033[0;33m| |         \033[0;0m.-`--'.
\033[0;33m| |        \033[0;0m/Y . . Y\\
\033[0;33m| |       \033[0;0m// |   | \\\\
\033[0;33m| |      \033[0;0m//  | . |  \\\\
\033[0;33m| |     \033[0;0m')   |   |   (`
\033[0;33m| |          \033[0;0m||'||
\033[0;33m| |          \033[0;0m|| ||
\033[0;33m| |          \033[0;0m|| ||
\033[0;33m| |          \033[0;0m|| ||
\033[0;33m| |         \033[0;0m/ | | \\
\033[0;33m""""""""""|_\033[0;0m`-' `-' \033[0;33m|"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : :  
. .          `'       . .
\033[0;0m __    _____ _____ _____ 
|  |  |     |   __|   __|
|  |__|  |  |__   |   __|
|_____|_____|_____|_____|                           
''',
"win":"""
\033[0;35m      :::       ::: ::::::::::: ::::    ::: 
      :+:       :+:     :+:     :+:+:   :+: 
      +:+       +:+     +:+     :+:+:+  +:+ 
      +#+  +:+  +#+     +#+     +#+ +:+ +#+ 
      +#+ +#+#+ +#+     +#+     +#+  +#+#+# 
       #+#+# #+#+#      #+#     #+#   #+#+# 
        ###   ###   ########### ###    #### \033[0;0m
                                       .''.
       .''.             *''*    :_\/_:     . 
      :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
 :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
 : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
  '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
      *        __*..* |  |     :      |.   |' .---"|
       _*   .-'   '-. |  |     .--'|  ||   | _|    |
    .-'|  _.|  |    ||   '-__  |   |  |    ||      |
    |' | |.    |    ||       | |   |  |    ||      |
 ___|  '-'     '    ""       '-'   '-.'    '`      |____
\033[2;36m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[0;0m
"""
}


def print_hangman(num_of_tries):
    """
    Return a stage of hangman according to the num_of_tires.
    :param print_hangman: numver 1-6
    :type print_hangman: int
    :return: hangman
    :rtype: str
    """
    HANGMAN_PHOTOS = {
    "state_0":
    """
    \033[2;33mx-------x\033[0;0m
            
            
            
            
            
    """,
    "state_1":
    """
    \033[2;33mx-------x
    |
    |
    |
    |
    |\033[0;0m
    """,
    "state_2":
    """
    \033[2;33mx-------x
    |       |
    |\033[0;0m       0
    \033[2;33m|
    |
    |\033[0;0m
    """,
    "state_3":
    """
    \033[2;33mx-------x
    |       |
    |\033[0;0m       0
    \033[2;33m|\033[0;0m       |
    \033[2;33m|
    |\033[0;0m
    """,
    "state_4":
    """
    \033[2;33mx-------x
    |       |
    |\033[0;0m       0
    \033[2;33m|\033[0;0m      /|\\
    \033[2;33m|
    |\033[0;0m
    """,
    "state_5":
    """
    \033[2;33mx-------x
    |       |
    |\033[0;0m       0
    \033[2;33m|\033[0;0m      /|\\
    \033[2;33m|\033[0;0m      /
    \033[2;33m|\033[0;0m
    """,
    "state_6":
    """\033[2;33mx-------x
    |       |
    |\033[0;0m       0
    \033[2;33m|\033[0;0m      /|\\
    \033[2;33m|\033[0;0m      / \\
    \033[2;33m|\033[0;0m
    """}
    return(HANGMAN_PHOTOS[f"state_{num_of_tries}"])
    
    
def score_print(win_lose_dict, name):
    """
    Print the score.
    :param win_lose_dict: player win lose score
    :param name: name of player
    :type win_lose_dict: dictionary
    :type name: str
    :return: player score
    :rtype: str
    """
    return (f"{name}- Wins: {win_lose_dict[name][1]}\t Loses: {win_lose_dict[name][3]}")


def choose_word(file_path, index):
    """
    read file and return a tuple containing words count and word from index.
    :param file_path: file location
    :param index: number from 1 and above
    :type file_path: str
    :type index: int
    :return: word count in file and a word from index
    :rtype: tuple
    """
    with open(file_path, "r") as file:
        file_content = file.read()
    file_list = file_content.split(" ")
    word_count = len(set(file_list))
    word_chosen = file_list[(index - 1) % len(file_list)]   
    return (word_count, word_chosen)          

                                                              
def is_name_valid(name):
    """
    Check if name is vaild (2-8 english chr),
    returns a proper messege if not.
    :param name: name
    :type name: str
    :return: false or true boolean with error messege
    :rtype: str
    :rtype: boolean
    """
    alphabetic = name.isalpha()
    text_limit = len(name) <= 8 and len(name) >= 2
    if (not text_limit) and (alphabetic):
        print('Text lengh incorrect')
        return False
    elif (not alphabetic) and (text_limit):
        print('Improper Symbol.')
        return False
    elif (not text_limit) and (not alphabetic):
        print('Unintelligible Text.')
        return False
    else:
        return True


def welcome_screen(name, max_lives):
    """
    function will print a welcome screen built from: user name (param) on top, ascii art title later, and game guide on buttom.
    :param name: user name
    :param max_lives: max amount of player lives
    :type name: str
    :type max_lives: int
    :return: prints title screen
    :rtype: str
    """
    welcome_text = f"Welcome {name}, To The Game:\n"
    ascii_title ="\n\t _    _\n\t| |  | |\n\t| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __\n\t|  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_  \\\n\t| |  | | (_| | | | | (_| | | | | | | (_| | | | |\n\t|_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n\t                    __/ /\n\t                   |___/\n"
    game_guide = f"\nGuess the word before the stickman gets it\nYou have: {max_lives} attempts"
    return f"{welcome_text} {ascii_title} {game_guide}\n"
    

def clear():
    """Clears the interperter"""
    print('\n' * 200)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks guess validity and return true or false with proper messege.
    :param letter_guessed: text
    :param old_letters_guesses: a list of valid inputs
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: true or false with proper error messege
    :rtype: str
    :rtype: boolean
    """
    alphabetic = letter_guessed.isalpha()
    text_limit = len(letter_guessed) == 1
    was_used = letter_guessed in old_letters_guessed
    print(letter_guessed)
    if not(text_limit) and (alphabetic):
        print('Text too long.')
        return False
    elif (not(alphabetic)) and (text_limit):
        print('Improper Symbol.')
        return False
    elif (not(text_limit)) and (not(alphabetic)):
        print('Unintelligible Text.')
        return False
    elif was_used:
        print("Already did that letter")
        return False
    else:
        return True

    
def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    Checks if input valid and adds it to old_letters_guessed.
    :param letter_guessed: english letter
    :param old_letters_guessed: a list of single english letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: false or true if letter was added to list 
    :trype: boolean
    :return: list of used letters
    :rtype: str
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print("-> ".join(filter(str.isalpha, str(sorted(old_letters_guessed)))))
        return False
    
    
def show_hidden_word(secret_word, old_letters_guessed):
    """
    Returns the secret_word with unguessed letters, hidden.
    :param secret_word: a word of english letterts
    :param old_letters_guessed: list of letters
    :type secren_word: str
    :type old_letters_guessed: list
    :return: letters not in list replaced with "_"
    :rtype: str
    """
    for letter in secret_word:
        if letter == " " or letter == "-":
            secret_word = secret_word.replace(letter, "-")
        elif letter not in old_letters_guessed:
            secret_word = secret_word.replace(letter, "_")
    return " ".join(secret_word)


def check_win(secret_word, old_letters_guessed):
    """
    return True or False depending if all the letters in secret_word are in old_letters_guessed.
    :param secret_word: an english word
    :param old_letters_list: a list of letters
    type secren_word: str
    type old_letters_list: list
    :return: true or false if all letters in word are in list
    :rtype: boolean
    """
    status = []
    for letter in secret_word:
        if letter == " " or letter == "-":
            status.append(True)
        else:
            status.append(letter in old_letters_guessed)
    return False not in status
    
 
def main(): 
    clear()
    users_dict = {}
    MAX_TRIES = 6
    word = "default"
    
    # Programn ask for user name and adds the new user into a dictionary to keep score.
    user_name = input ("Please Enter Your Name: ").capitalize()
    while is_name_valid(user_name) != True:
        user_name = input ("Please Enter Your Name, but do it correctly: ").capitalize()
    users_dict[user_name] = ["WINS", 0, "LOSES", 0] 
    
    clear()  
    print(welcome_screen(user_name, MAX_TRIES))
    
    while True: # Loop to keep program running.
        print(score_print(users_dict, user_name))
        choice = (input ("1: New Game\n2: Change User\n3: Load Words File\n")) #Main menu
        
        if choice == '1': #Game
            clear()
            letter_guessed_list = []
            num_of_fails = 0
            
            clear()
            # Loop until players fail to guess a letter 6 times or find all the hidden words.
            while (num_of_fails < MAX_TRIES) and (check_win(word, letter_guessed_list) != True): 
                # Prints the hangman status, secret word with hidden letters
                # and save guess from player into a variable.
                print(print_hangman(num_of_fails)) 
                print(show_hidden_word(word, letter_guessed_list)) 
                player_guess = input("Guess a Letter: ").lower() 
                
                # Loop until player_guess is a valid input and adds it into letter_guess_list. 
                while try_update_letter_guessed(player_guess, letter_guessed_list) != True: 
                    player_guess = input("Guess a Letter, but correctly...: ").lower()
        
                # If guess is wrong, a fail is added to num_of_fails and sad-face is printed.
                clear()
                if player_guess not in word:
                    num_of_fails += 1
                    print(":(")
            clear()
            
            # After game has ended, program updates the score and selects a screen to show according to if player won or lost.
            if num_of_fails >= MAX_TRIES:
                print(HANGMAN_win_loss["lose"] + "\nWord Was:", word + "\n")
                users_dict[user_name][3] += 1
            elif check_win(word, letter_guessed_list):
                print(HANGMAN_win_loss["win"] + "\nWord Was:", word + "\n")
                users_dict[user_name][1] += 1
         
    
        elif choice == '2': # Change User
        # Change the user_name variable
            clear()
            user_name = user_name = input ("Please Enter Your Name: ").capitalize()
            while is_name_valid(user_name) != True:
                user_name = input ("Please Enter Your Name, but do it correctly: ").capitalize()
            # Add a new user into users_dict.
            if user_name not in users_dict:
                users_dict[user_name] = ["WINS", 0, "LOSES", 0]
            clear()
          
        
        elif choice == '3': # Load Word File
            clear()
            path = input("Enter File Path:\n")
            word_index = int(input("Enter Index Number:\n"))
            total_words, chosen_word = choose_word(path, word_index)
            word = chosen_word
            clear()
            print(f"\nFile Loaded\nFile Has {total_words} words\n")
        
        else: #Any other input will close the game
            break


if __name__ == "__main__":
    main()

    
