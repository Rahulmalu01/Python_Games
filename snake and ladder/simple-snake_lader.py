import random as rm
import os
snake_lader={99:1,38:14,68:25,95:28,80:39,90:51,26:88,60:84,9:48,45:77,2:23,66:94}
play=[chr(991),chr(976),chr(985),chr(952)] ; poss=[0,0,0,0] ; player=[]
def snake_ladder():
    sample();playername();i=1
    while i>0:
        input("Press Enter to roll the dice...")
        dice=rolldice() ; os.system("cls")
        print("You rolled:", dice)
        position(dice,i) ; condition() ; printn() ; result() ; i=i+1
def sample():print("Let's start the game of") ; print("   Snake and Ladders   ")
def playername():
    p=int(input("Enter the number of players : "))
    for i in range(0,p): player.append(input("Enter the player : "))
def rolldice():return rm.randint(1,6)
def position(dice,i):
    a=len(player)
    if a==2:pos1(dice,i)
    elif a==3:pos2(dice,i)
    else:pos3(dice,i)
def pos1(dice,i):
    if i%2==1:
        if poss[0]+dice>100:print(player[0]," position is : ",poss[0])
        else:poss[0]=poss[0]+dice;print(player[0]," position is : ",poss[0])
    else:
        if poss[1]+dice>100:print(player[1]," position is : ",poss[1])
        else:poss[1]=poss[1]+dice;print(player[1]," position is : ",poss[1])
def pos2(dice,i):
    if i%3==1:
        if poss[0]+dice>100:print(player[0]," position is : ",poss[0])
        else:poss[0]=poss[0]+dice;print(player[0]," position is : ",poss[0])
    elif i%3==2:
        if poss[1]+dice>100:print(player[1]," position is : ",poss[1])
        else:poss[1]=poss[1]+dice;print(player[1]," position is : ",poss[1])
    else:
        if poss[2]+dice>100:print(player[2]," position is : ",poss[2])
        else:poss[2]=poss[2]+dice;print(player[2]," position is : ",poss[2])
def pos3(dice,i):
    if i%4==1:
        if poss[0]+dice>100:print(player[0]," position is : ",poss[0])
        else:poss[0]=poss[0]+dice;print(player[0]," position is : ",poss[0])
    elif i%4==2:
        if poss[1]+dice>100:print(player[1]," position is : ",poss[1])
        else:poss[1]=poss[1]+dice;print(player[1]," position is : ",poss[1])
    elif i%4==3:
        if poss[2]+dice>100:print(player[2]," position is : ",poss[2])
        else:poss[2]=poss[2]+dice;print(player[2]," position is : ",poss[2])
    else:
        if poss[3]+dice>100:print(player[3]," position is : ",poss[3])
        else:poss[3]=poss[3]+dice;print(player[3]," position is : ",poss[3])
def condition():
    if poss[0] in snake_lader:
        new_position=poss[0];poss[0]=snake_lader[poss[0]]
        if poss[0] > new_position: print(player[0]," climbed a ladder from ",new_position," to ",poss[0])
        else: print(player[0]," got swallowed by a snake from ",new_position," to ",poss[0])
    if poss[1] in snake_lader:
        new_position=poss[1];poss[1]=snake_lader[poss[1]]
        if poss[1] > new_position: print(player[1]," climbed a ladder from ",new_position," to ",poss[1])
        else: print(player[1]," got swallowed by a snake from ",new_position," to ",poss[1])
    if poss[2] in snake_lader:
        new_position=poss[2];poss[2]=snake_lader[poss[2]]
        if poss[2] > new_position: print(player[2]," climbed a ladder from ",new_position," to ",poss[2])
        else: print(player[2]," got swallowed by a snake from ",new_position," to ",poss[2])
    if poss[3] in snake_lader:
        new_position=poss[3];poss[3]=snake_lader[poss[3]]
        if poss[3] > new_position: print(player[3]," climbed a ladder from ",new_position," to ",poss[3])
        else: print(player[3]," got swallowed by a snake from ",new_position," to ",poss[3])
def printn():
    for i in range(10,0,-2):
        for u in range(0,10):
            if ((i*10)-u)!=100:
                if ((i*10)-u)==poss[0]==poss[1]==poss[2]==poss[3]: print(play[0],play[1],play[2],play[3],end=" ") 
                if ((i*10)-u)==poss[0] or ((i*10)-u)==poss[1] or ((i*10)-u)==poss[2] or ((i*10)-u)==poss[3]:double(u,i,1)
                if poss[0]!=poss[1] or poss[2]!=poss[1] or poss[3]!=poss[1] or poss[0]!=poss[2] or poss[0]!=poss[3] or poss[3]!=poss[2]: single(u,i,1)
                if ((i*10)-u)!=poss[0] and ((i*10)-u)!=poss[1] and ((i*10)-u)!=poss[2] and ((i*10)-u)!=poss[3]: print((i*10)-u,end="   ")
            else: print((i*10)-u,end="  ")
        print("\n")
        for u in range(1,11):
            if (((i-2)*10)+u)==poss[0]==poss[1]==poss[2]==poss[3]: print(play[0],play[1],play[2],play[3],end=" ")
            if (((i-2)*10)+u)==poss[0] or (((i-2)*10)+u)==poss[1] or (((i-2)*10)+u)==poss[2] or (((i-2)*10)+u)==poss[3]:double(u,i,2)
            if poss[0]!=poss[1] or poss[2]!=poss[1] or poss[3]!=poss[1] or poss[0]!=poss[2] or poss[0]!=poss[3] or poss[3]!=poss[2]: single(u,i,2)
            if (((i-2)*10)+u)!=poss[0] and (((i-2)*10)+u)!=poss[1] and (((i-2)*10)+u)!=poss[2] and (((i-2)*10)+u)!=poss[3]: 
                print((i-2)*10+u,end="   ")
                if (i-2)*10 <=10: print(end=" ")
        print("\n")
def single(u,i,count):
    if count==1:
        if ((i*10)-u)==poss[0] and poss[0]!=poss[1] and poss[0]!=poss[2] and poss[0]!=poss[3]:print(play[0],end="    ")
        if ((i*10)-u)==poss[1] and poss[0]!=poss[1] and poss[1]!=poss[2] and poss[1]!=poss[3]:print(play[1],end="    ")
        if ((i*10)-u)==poss[2] and poss[2]!=poss[1] and poss[0]!=poss[2] and poss[2]!=poss[3]:print(play[2],end="    ")
        if ((i*10)-u)==poss[3] and poss[3]!=poss[1] and poss[3]!=poss[2] and poss[0]!=poss[3]:print(play[3],end="    ")
    else:
        if (((i-2)*10)+u)==poss[0] and poss[0]!=poss[1] and poss[0]!=poss[2] and poss[0]!=poss[3]:print(play[0],end="    ")
        if (((i-2)*10)+u)==poss[1] and poss[0]!=poss[1] and poss[1]!=poss[2] and poss[1]!=poss[3]:print(play[1],end="    ")
        if (((i-2)*10)+u)==poss[2] and poss[2]!=poss[1] and poss[0]!=poss[2] and poss[2]!=poss[3]:print(play[2],end="    ")
        if (((i-2)*10)+u)==poss[3] and poss[3]!=poss[1] and poss[3]!=poss[2] and poss[0]!=poss[3]:print(play[3],end="    ")
def double(u,i,count):
    if count==1:
        if   poss[1]==poss[0]==poss[2]==((i*10)-u):print(play[0],play[1],play[2],end=" ")
        elif poss[1]==poss[0]==poss[3]==((i*10)-u):print(play[0],play[1],play[3],end=" ")
        elif poss[3]==poss[0]==poss[2]==((i*10)-u):print(play[0],play[2],play[3],end=" ")
        elif poss[1]==poss[3]==poss[2]==((i*10)-u):print(play[1],play[2],play[3],end=" ")
        elif poss[1]==poss[0]==((i*10)-u) or poss[1]==poss[0]==(((i-2)*10)+u):print(play[0],play[1],end="  ")
        elif poss[2]==poss[0]==((i*10)-u) or poss[2]==poss[0]==(((i-2)*10)+u):print(play[0],play[2],end="  ")
        elif poss[3]==poss[0]==((i*10)-u) or poss[3]==poss[0]==(((i-2)*10)+u):print(play[0],play[3],end="  ")
        elif poss[2]==poss[1]==((i*10)-u) or poss[2]==poss[1]==(((i-2)*10)+u):print(play[1],play[2],end="  ")
        elif poss[3]==poss[1]==((i*10)-u) or poss[3]==poss[1]==(((i-2)*10)+u):print(play[1],play[3],end="  ")
        elif poss[3]==poss[2]==((i*10)-u) or poss[3]==poss[2]==(((i-2)*10)+u):print(play[2],play[3],end="  ")
    else:
        if poss[1]==poss[0]==poss[2]==(((i-2)*10)+u):print(play[0],play[1],play[2],end=" ")
        elif poss[1]==poss[0]==poss[3]==(((i-2)*10)+u):print(play[0],play[1],play[3],end=" ")
        elif poss[3]==poss[0]==poss[2]==(((i-2)*10)+u):print(play[0],play[2],play[3],end=" ")
        elif poss[1]==poss[3]==poss[2]==(((i-2)*10)+u):print(play[1],play[2],play[3],end=" ")
        elif poss[1]==poss[0]==(((i-2)*10)+u):print(play[0],play[1],end="  ")
        elif poss[2]==poss[0]==(((i-2)*10)+u):print(play[0],play[2],end="  ")
        elif poss[3]==poss[0]==(((i-2)*10)+u):print(play[0],play[3],end="  ")
        elif poss[2]==poss[1]==(((i-2)*10)+u):print(play[1],play[2],end="  ")
        elif poss[3]==poss[1]==(((i-2)*10)+u):print(play[1],play[3],end="  ")
        elif poss[3]==poss[2]==(((i-2)*10)+u):print(play[2],play[3],end="  ")
def result():
    if poss[0]==100:print(player[0]," is the winner");exit()
    if poss[1]==100:print(player[1]," is the winner");exit()
    if poss[2]==100:print(player[2]," is the winner");exit()
    if poss[3]==100:print(player[3]," is the winner");exit()
snake_ladder()