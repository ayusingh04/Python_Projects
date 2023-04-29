import random 

print('\n\n-----*****-----Welcome to The Game of Dice-----*****-----\n')
name = input('Enter your Good name :  ')
print(f"\nHello! {name} Let's Start This !!..")
ch = 'Y'
l = []
while ch == 'Y' or ch == 'y':
    print('\n1. Roll\n2. Exit')
    x = int(input('\nEnter Your Choice: '))
    c1= random.choice([1,2,3,4,5,6])
    c2= random.choice([1,2,3,4,5,6])
    if x == 1:
        print('\nNumber on the dices are: ',c1,c2)
        l.append([c1,c2])
    elif x == 2:
        print('\nTotal outcomes: ',l)
        print('\n\t\tThank You')
    else:
        print('\nEnter valid choice')
        x = int(input('\n Enter Your Choice : '))
    ch = input("\nDo you want to continue(Y/N): ")
else:
    print('\nTotal outcomes: ',l)
    print('\n\t\t...Thank You for Playing...')
