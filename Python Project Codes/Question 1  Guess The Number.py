import random

def fun(sc):
    x = random.randint(1, 10)
    for i in range(5):
        ch = int(input("\t\tEnter a number between 1 to 10: "))
        if ch != x:
            print("\n\t\t\t Wrong Guess! Please Try again...\n")
            sc -= 50
        else:
            print("\n\t\tCongratulations , you guessed it!\n")
            sc += 100
            break
    else:
        print("\n Game over. The correct answer was", x)
        sc = 0
    return sc 

print('\n\n---------*****-----Welcome to Guess The Number-----*****----------\n\n')
print('Rule of the game are : \n\t You have five chance to guess a number.\n\n')
sc = 20
sc = fun(sc)
print("Final score : ", sc)

