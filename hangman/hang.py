import numpy as np
import os
li = chr(2)
life = [li,li,li,li,li,li,li]
player1=input("Enter the first player name : ")
player2=input("Enter the second player name : ")
def sample():
    print("The rule for the game is : ")
    print("1. The player1 has to enter a word related to some general thing and give a reference of the word")
    print("2. The player2 has to guess the word by entering alphabet")
def words():
    inp=input("Enter a word : ").lower()
    related=input("Enter a related word for the above word enetred : ")
    os.system("cls")
    print(related)
    arra=np.array(['_' for a in range(0,len(inp))])
    count=7
    for i1 in range(0,len(inp)*100):
        man()
        println(arra)
        coun,cou,a =len(inp),len(inp),-1
        wor=input("Enter a letter : ").lower()
        for i in inp:
            a+=1
            if wor==i: arra[a]=wor
            else: cou-=1
        if cou==0: count-=1
        if count!=7: life[count]= chr(1)
        if count==0: man();print(player1," wins the game");exit()
        for i in arra:
            if i!="_": coun-=1
        if coun==0: print(player2," wins the game");exit()
def println(arra):
    for i in arra: print(i , end=" ")
    print("\n")

def man():
    print('  ------')
    print('  |',end="")
    if life[6] == chr(1):
        print('  |',end="")
    print()
    print('  |',end="")
    if life[5] == chr(1):
        print('  O',end="")
    print()
    print('  |',end="")
    if life[4] == chr(1):
        print(' /',end="")
    if life[3] == chr(1):
        print('|',end="")
    if life[2] == chr(1):
        print('\\',end="")
    print()
    print('  |',end="")
    if life[1] == chr(1):
        print(' /',end="")
    if life[0] == chr(1):
        print(' \\',end="")
    print()
    print('  |')
    print('-----')

def hangman():
    sample()
    words()
hangman()
