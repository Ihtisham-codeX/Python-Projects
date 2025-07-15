# libraries

import random
import msvcrt


def clear():
    print("\n" * 100)


def Game_Header():
    print('''
██╗  ██╗ █████╗ ███╗   ██╗ ██████╗     ███╗   ███╗ █████╗ ███╗   ██╗
██║  ██║██╔══██╗████╗  ██║██╔════╝     ████╗ ████║██╔══██╗████╗  ██║
███████║███████║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██╔██╗ ██║
██╔══██║██╔══██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║╚██╗██║
██║  ██║██║  ██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    ''')


def Game_Over():
    print('''
██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗     
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    
██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝    
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗    
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝    
    ''')


def won():
    print('''
██    ██  ██████  ██    ██     ██     ██  ██████  ███    ██        ██  
 ██  ██  ██    ██ ██    ██     ██     ██ ██    ██ ████   ██     ██  ██ 
  ████   ██    ██ ██    ██     ██  █  ██ ██    ██ ██ ██  ██         ██ 
   ██    ██    ██ ██    ██     ██ ███ ██ ██    ██ ██  ██ ██     ██  ██ 
   ██     ██████   ██████       ███ ███   ██████  ██   ████        ██  


    ''')


def Error(flag):
    if flag == False:
        print("Invalid Input ! Enter Only One Alphabet ")


hangman_rope = '''
 _______
|   |
|
|
|
|
|
|
'''
hangman_head = '''
 _______
|   |
| (`_`) 
|   
|
|
|
|
'''
hangman_neck = '''
 _______
|   |
| (`_`) 
|   |
|
|
|
|
'''
hangman_hands = '''
 _______
|   |
| (`_`) 
|   |
| / | \\
|
|
|
'''
hangman_body = '''
 _______
|   |
| (`_`) 
|   |
| / | \\
|   |
|
|
'''
hangman_legs = '''
 _______
|   |     (Tu Vi Kusa e ain)
| (`_`) 
|   |
| / | \\
|   |
|  / \\
|
'''
dictionary = ["anchor", "bakery", "castle", "canyon", "dancer", "engine", "farmer", "galaxy",
              "hunger", "island", "jungle", "kitten", "ladder", "magnet", "napkin", "object",
              "packet", "quartz", "rocket", "saddle", "talent", "unfold", "vacuum", "wallet",
              "yellow", "zigzag", "border", "cabinet", "danger", "eagle", "feather", "gravel",
              "helmet", "ignore", "jumper", "kidney", "lumber", "moment", "native", "option",
              "pastel", "rescue", "signal", "ticket", "update", "vessel", "winner", "wander",
              "yonder", "zephyr"]


def Dash_Printer(word):
    Dash_String = ""
    length = len(word)
    for i in range(length):
        Dash_String = Dash_String + "-"
    return Dash_String


def Word_Selecter(dictioanry):
    random_index = random.randint(0, 49)
    return dictionary[random_index]


def Check_Input_Existence(guess, word):
    for i in range(len(word)):
        if guess == word[i]:
            return True
    return False


def Place_Right_Guess(guess, word, dashes):
    dashes = list(dashes)
    for i in range(len(word)):
        if guess == word[i]:
            dashes[i] = guess
    return ''.join(dashes)


def Complete(word):
    for i in range(len(word)):
        if word[i] == "-":
            return False
    return True


def print_hangman(lives):
    if lives == 5:
        print(hangman_rope)
    elif lives == 4:
        print(hangman_head)
    elif lives == 3:
        print(hangman_neck)
    elif lives == 2:
        print(hangman_hands)
    elif lives == 1:
        print(hangman_body)
    elif lives == 0:
        print(hangman_legs)


def Input_is_Correct(word):
    if len(word) == 1:
        return True
    else:
        return False


# Fetching a Random Word from the dictionary

hangman_word = Word_Selecter(dictionary)
print(hangman_word)

# starting an infinite loop

lives = 5
completed = True
guess = "-"
dashes = Dash_Printer(hangman_word)
flag = True

while Complete(dashes) == False and lives >= 1:
    # Clearing the screen

    clear()

    # if Error in input

    Error(flag)

    # Game Header

    Game_Header()

    # Adding Dashes

    dashes = Place_Right_Guess(guess, hangman_word, dashes)
    print(dashes)

    # Printing the hangman rope

    print_hangman(lives)

    # Taking Input The Guess

    guess = input("Enter your Guess : ")
    if not Input_is_Correct(guess):
        flag = False
        continue
    else:
        flag = True
    completed = Complete(guess)

    # Checking the guess

    Exist = Check_Input_Existence(guess, hangman_word)
    if Exist == False:
        lives -= 1
    elif Exist == True:
        Place_Right_Guess(guess, hangman_word, dashes)

if Complete(dashes):
    won()
else:
    print_hangman(0)
    Game_Over()


