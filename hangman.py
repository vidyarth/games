

import random
def hangman():
    list = ['computer','english','apple','education','engineering','microsoft','animal']
    word = random.choice(list)
    valid = set('abcdefghijklmnopqrstuvwxyz')
    guessedWords = ''
    turns = 10
    while len(word)>0:
        main_word = ''

        for letter in word:
            if letter in guessedWords:
                main_word += letter
            else:
                main_word += "_ "
        print(main_word)
        if main_word == word:
            print("YOU WON!!!!!")


            break
        guess = input("Enter your guess...(any letter you like)")

        if guess in valid:
            guessedWords = guessedWords + guess
        else:
            print("invalid input... enter a character between a..to..z")
            contiue


        if guess not in word:
            print("opps! the letter is not there in the word")
            turns = turns-1
        else:
            print("yeah! you got that letter")

        if turns==9:
            print("only 9 turns left")
            print("______________________________________")
        if turns==8:
            print("only 8 turns left")
            print("______________________________________")
            print("               |                      ")
        if turns==7:
            print("only 7 turns left")
            print("______________________________________")
            print("               |                      ")
            print("               O                      ")
        if turns==6:
            print("only 6 turns left")
            print("______________________________________")
            print("               |                      ")
            print("               O                      ")
            print("               |                      ")
        if turns==5:
            print("only 5 turns left")
            print("______________________________________")
            print("               |                      ")
            print("               O                      ")
            print("               |                      ")
            print("              /                      ")
        if turns==4:
            print("only 4 turns left")
            print("______________________________________")
            print("               |                      ")
            print("               O                      ")
            print("               |                      ")
            print("              / \                     ")
        if turns==3:
            print("only 3 turns left")
            print("______________________________________")
            print("               |                      ")
            print("             \ O                      ")
            print("               |                      ")
            print("              / \                     ")
        if turns==2:
            print("only 2 turns left")
            print("______________________________________")
            print("               |                      ")
            print("             \ O /                    ")
            print("               |                      ")
            print("              / \                     ")
        if turns==1:
            print("only 1 turns left")
            print("______________________________________")
            print("               |                      ")
            print("             \ O                     ")
            print("               | \                     ")
            print("              / \                     ")
        if turns==0:
            print("no turns turns left")
            print("______________________________________")
            print("               |                      ")
            print("               O                     ")
            print("             / | \                     ")
            print("              / \                     ")

            print("YOU KILLED A INNOCENT MAN")
            break






name = input("Enter your good name")
print(f"welcome to HANGMAN dear  {name} !!")
print("lets start playing")
print("-----------------------------------------------------------------")

hangman()
ch = input()
if ch=='q':
    exit()