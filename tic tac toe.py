import random
def display(og):
    for a in og:
        for b in a:
            if b == 0:
                print("| |",end='')
            elif b==1:
                print("|O|",end='')
            elif b==2:
                print("|X|",end='')
        print()

def rann(g,boxes):
    y=0
    z=0
    random_number = random.randint(1, boxes)
    for fgh in g :
        for fg in fgh:
            y+=1
            if fg==0:
                z+=1
                if z==random_number:
                    return y-1
def optimal(mat):
    pass

def check(num,mat,oo):
    oo=oo*oo*oo
    row = int(num/3)
    column = int(num%3)
    a=1
    for i in range(3):
        a*=mat[row][i]
    if a==oo:return 1
    a=1
    for i in range(3):
        a*=mat[i][column]
    if a==oo:return 1
    if row==column:
        a=1
        for i in range(3):
            a*=mat[i][i]
        if a==oo:return 1
        a=1
        for i in range(3):
            a*=mat[i][2-i]
        if a==oo:return 1
    return 0

  
org=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
boxes =9
b=0
a=input("Chose first or second :")
if a=="2":
    a=rann(org,boxes)
    c=a%10
    org[int(a/3)][a%3]=2
    boxes-=1
display(org)
while  True:
    while True:
        number = int(input("Enter the index of place from 1-9 :"))-1
        if org[int(number/3)][number%3]==0:
            break
    
    org[int(number/3)][number%3]=1
    boxes-=1
    display(org)
    b = check(number,org,1)
    if((boxes==0) or b!=0):
        print("You Won!!!!")
        break
    a=rann(org,boxes)
    org[int((a)/3)][a%3]=2
    boxes-=1
    display(org)
    b = check(number,org,2)
    if((boxes==0) or b!=0):
        print("Computer Won!")
        break
if b==0:
    print("Ohh Itz a draw try again..")




