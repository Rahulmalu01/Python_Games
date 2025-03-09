import os 
def xo():
    xop=[" "] * 9
    sample()
    player1=input('Enter your name player1 : ')
    player2=input('Enter your name player2 : ')
    print('Lets start te game')
    num=1
    while num<10 :
        num+=1
        inpu=int(input('Enter the position : '))
        os.system("cls")
        if xop[inpu-1]==" ":
            if(num%2==1):xop[inpu-1]="X"
            else:xop[inpu-1]="O"
        else:print("The position is already used");num-=1
        board(xop)
        check(player1,player2,xop)
def sample():
    print("The XO Game begins")
    print("Sample XO board")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")
    print("The positions are informed by the numbers repreenting the specific box")
def board(xop):
    print(xop[0],'|',xop[1],'|',xop[2])
    print('--+---+--')
    print(xop[3],'|',xop[4],'|',xop[5])
    print('--+---+--')
    print(xop[6],'|',xop[7],'|',xop[8])
def check(player1,player2,xop):
    if  (xop[0]==xop[1] and xop[1]==xop[2] and xop[1]!=" "):q=xop[0]
    elif(xop[3]==xop[4] and xop[4]==xop[5] and xop[4]!=" "):q=xop[4]
    elif(xop[6]==xop[7] and xop[7]==xop[8] and xop[7]!=" "):q=xop[8]
    elif(xop[0]==xop[3] and xop[3]==xop[6] and xop[0]!=" "):q=xop[3]
    elif(xop[1]==xop[4] and xop[4]==xop[7] and xop[4]!=" "):q=xop[4]
    elif(xop[2]==xop[5] and xop[5]==xop[8] and xop[8]!=" "):q=xop[2]
    elif(xop[0]==xop[4] and xop[4]==xop[8] and xop[0]!=" "):q=xop[1]
    elif(xop[2]==xop[4] and xop[4]==xop[6] and xop[4]!=" "):q=xop[3]
    else:return
    if(q=="X"):print(player2,"is the winner");exit()
    if(q=="O"):print(player1,"is the winner");exit()
xo()