import sys
import random

user1 = input("What's your name?")

player = [
    ["name", 0],
    ["Computer", 0]
]
player[0][0] = user1

i = True
global game
game = 1

def coreGame(u1, u2):
    if u1 == u2:
        return("It's a tie!")
    elif u1 == 'rock':
        if u2 == 'scissors':
            player[0][1] = player[0][1] + 1
            return("Rock wins!")
        else:
            player[1][1] = player[1][1] + 1
            return("Paper wins!")
    elif u1 == 'scissors':
        if u2 == 'paper':
            player[0][1] = player[0][1] + 1
            return("Scissors win!")
        else:
            player[1][1] = player[1][1] + 1
            return("Rock wins!")
    elif u1 == 'paper':
        if u2 == 'rock':
            player[0][1] = player[0][1] + 1
            return("Paper wins!")
        else:
            player[1][1] = player[1][1] + 1
            return("Scissors win!")
    else:
        return(u1,u2)
        sys.exit()

def getThrowP1():
    user1_answer = random.randint(1, 3)
    u1 = 0
    if user1_answer == 1:
        return 'rock'
    elif user1_answer == 2:
        return 'scissors'
    elif user1_answer == 3:
        return 'paper'


def getThrowP2():
    user2_answer = random.randint(1, 3)
    u2 = 0
    if user2_answer == 1:
        return 'rock'
    elif user2_answer == 2:
        return 'scissors'
    elif user2_answer == 3:
        return 'paper'

continueGame = True

def startGame():
    while continueGame is True:
        p1 = getThrowP1()
        p2 = getThrowP2()
        print("###############################################")
        print(player[0][0], "heeft", p1)
        print(player[1][0], "heeft", p2)
        print(coreGame(p1, p2))
        print("_______________________________________________")
        if input("Want to go again?") != 'j':
            print(player[0][0], "heeft", player[0][1])
            print(player[1][0], "heeft", player[1][1])
            break;


startGame()
