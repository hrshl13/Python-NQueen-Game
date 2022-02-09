#This is the main module
from cgitb import text
from turtle import bgcolor
from py_console import console, bgColor, textColor
import nqueen
import numpy as np
from random import randint
  
console.setShowTimeDefault(False)

__name__="__main__"

def exitGame(t):
    console.log(
        f"-----: {console.highlight('GAME OVER', bgColor=bgColor.RED)} :-----")
    print("\n\n\n")
    if (t):
        exit(1)
    main()
def menu():
    console.log(f"\t:{console.highlight('Menu', bgColor=bgColor.BLUE)}:")
    console.info('1.  Start New Game')
    console.info('2.  Exit')
    print("\n\n")
    console.info("Enter your choice: ")
    try:
        n = int(input())
    except:
        console.error("Please enter correct values!!")
        exitGame(False)
    if n==2:
        exitGame(True)
    if n>2 or n<1:
        console.error("Please enter correct values!!")
        exitGame(False)
    return n

def printboard(l):
    n=len(l)
    print("+", end=" ")
    for k in range(n):
        print(k+1, end=" ")
        if (k==n-1):
            print() 
    for i in range(n):
        print(i+1, end=" ")
        for j in range(n):
            print(l[i][j], end=" ")
        print()

def make(n):
    lst=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        lst.append(l)
    return lst

def printSol(n):
    list1 = nqueen.solveNQ(n)
    print("+", end=" ")
    for k in range(n):
        print(k+1, end=" ")
        if (k==n-1):
            print() 
    for i in range(n):
        print(i+1, end=" ")
        for j in range(n):
            print(list1[i][j], end=" ")
        print()

def check(lst):
    n=len(lst)
    list1 = nqueen.solveNQ(n)
    if np.allclose(lst,list1):
        return True

def ask(l):
    printboard(l)
    n=len(l)
    ans = nqueen.solveNQ(n)
    try:
        console.info('\tWhere will you place you next Queen?', severe=False)
        row = int(input("Enter Row-Position of Queen: "))
        col = int(input("Enter Column-Position of Queen: "))
        if ans[row-1][col-1]==1:
            l[row-1][col-1]=1
            return True
        return False
    except:
        console.error("Please enter correct values!!")
        ask(l)

def hint(Board):
    print("\n")
    console.highlight("\tHINT", bgColor=bgColor.CYAN)
    N=len(Board)
    l=nqueen.solveNQ(N)
    num = randint(0,N-1)
    print(l[num])
    print("\n\n")

def menu2():
    console.log(f"\t:{console.highlight('Menu', bgColor=bgColor.BLUE)}:")
    console.info('1.  Hint(Will provide one random row of the solution)')
    console.info('2.  Continue Game')
    console.info('3.  Solution(This will end the current game)')
    console.info('4.  Exit Game')
    print("\n\n")
    console.info("Enter your choice: ")
    n = int(input())
    return n


def main():
    console.log(
        f"-----: {console.highlight('Welcome', bgColor=bgColor.GREEN)} :-----")
    choice=menu()
    if choice==1:
        console.info("Enter the number of Queens you want to play with: ")
        try:
            N= int(input())
        except:
             console.error("Please enter correct values!!")
             exitGame(False)

        if nqueen.solveNQ(N)==False: 
            console.error("Can't make a board with this number!!")
            exitGame(False)
        print("\n\n")
        console.warn("\t\tGame Started!!", severe=True)
        console.info("Here is you board:-")
        BOARD = make(N)
        printboard(BOARD)
        flag=True
        counter=0
        while True:
            choice2=menu2()
            if choice2==1:
                hint(BOARD)
            elif choice2==3:
                printSol(N)
                exitGame(False)
            elif choice2==4:
                exitGame(False)
            
            flag=ask(BOARD)
            if(flag):
                counter+=1
                console.success("Correct Answer!!")
                console.info(f"You have a streak of {console.highlight(f'{counter}', bgColor=bgColor.GREEN, textColor=textColor.BLACK)} correct answers!!!")
                printboard(BOARD)
                if check(BOARD):
                    console.success("Congratulations!!!You have WON", severe=True)
                    exitGame(True)
            else:
                console.error("Wrong Answer!!!", severe=True)
                BOARD=make(N)
                counter=0
                console.info(f"Better luck next time!!")
                exitGame(False)
        

if __name__=="__main__":
    main()
