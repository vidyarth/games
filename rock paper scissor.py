import random
print("GET READY TO PLAY!")
print("valid inputs: rock,paper,scissor")
you = int(0)
me = int(0)
while (True):
    list = ['rock','paper','scissor']
    user = input("What is your go? ")
    if user in list:
        pass
    else:
        print("invalid input")
        continue
    print(f"you have chosen '{user}'")
    computer = random.choice(list)
    print(f"computer has chosen '{computer}'")
    if (user=='rock' and computer=='scissor'):
        print("you won!!")
        you = you + 1
    elif (user=='paper' and computer=='rock'):
        print("you won!!")
        you = you + 1
    elif (user=='scissor' and computer=='paper'):
        print("you won!!")
        you = you + 1
    elif (user == computer):
        print("match draw")
    else:
        print("sorry you have lost the match")
        me += 1
    next = input("Do you want to continue (Y/N)")
    if (next == 'Y' or next == 'y'):
        pass
    elif (next == 'N' or next == 'n'):
        break
    else:
        print("invalid input")
print(f"your score is {you}")
print(f"computer's score is {me}")
if (you > me):
   print("CONGRATS YOU WON!!!")
elif (me > you):
   print("COMPUTER WON")
else:
   print("match draw")

